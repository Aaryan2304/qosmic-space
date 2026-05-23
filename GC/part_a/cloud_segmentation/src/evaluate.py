"""
Computes: mIoU, precision, recall, F1, accuracy, confusion matrix, false negative rate, confidence calibration (ECE).

Generates figures:
- Confusion matrix heatmap
- 5 sample predictions with overlay
- Per-class metrics bar chart
"""
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import torch
from tqdm import tqdm

sys.path.insert(0, str(Path(__file__).resolve().parent))

from model import CloudSegNet
from data_utils import get_dataloaders
from config import CHECKPOINT_DIR, FIGURE_DIR, NUM_CLASSES


def compute_metrics(pred: torch.Tensor, target: torch.Tensor, num_classes: int = 2):
    """
    Compute per-class and aggregate metrics.

    Returns dict with: mIoU, precision, recall, f1, accuracy, ious (list),
    conf_matrix (2D), fn_rate, fp_rate
    """
    pred = pred.flatten()
    target = target.flatten()

    conf = torch.zeros(num_classes, num_classes, dtype=torch.int64)
    for t in range(num_classes):
        for p in range(num_classes):
            conf[t, p] = ((target == t) & (pred == p)).sum()

    ious = []
    precisions = []
    recalls = []
    for c in range(num_classes):
        tp = conf[c, c].float()
        fp = conf[:, c].sum() - tp
        fn = conf[c, :].sum() - tp
        tn = conf.sum() - tp - fp - fn

        iou = tp / (tp + fp + fn + 1e-8)
        prec = tp / (tp + fp + 1e-8)
        rec = tp / (tp + fn + 1e-8)
        f1 = 2 * prec * rec / (prec + rec + 1e-8)

        ious.append(iou.item())
        precisions.append(prec.item())
        recalls.append(rec.item())

    miou = np.mean(ious)
    precision = np.mean(precisions)
    recall = np.mean(recalls)
    f1 = 2 * precision * recall / (precision + recall + 1e-8)
    accuracy = (conf.diag().sum().float() / conf.sum()).item()

    # Cloud class (class 1) FN rate
    fn_rate = 1.0 - recalls[1]
    fp_rate = 1.0 - precisions[1]

    return {
        "mIoU": miou,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "accuracy": accuracy,
        "class_ious": ious,
        "class_precisions": precisions,
        "class_recalls": recalls,
        "false_negative_rate": fn_rate,
        "false_positive_rate": fp_rate,
        "confusion_matrix": conf.numpy().tolist(),
    }


@torch.no_grad()
def evaluate(model: torch.nn.Module, loader, device: torch.device):
    """Run evaluation on a DataLoader, return metrics + visual samples + probs for ECE."""
    model.eval()
    all_preds = []
    all_targets = []
    all_probs = []
    sample_patches = []

    for images, masks in tqdm(loader, desc="Evaluating"):
        images = images.to(device, non_blocking=True)
        masks = masks.to(device, non_blocking=True)

        logits = model(images)
        probs = torch.softmax(logits, dim=1)
        preds = logits.argmax(dim=1)

        all_preds.append(preds.cpu())
        all_targets.append(masks.cpu())
        all_probs.append(probs.cpu())

        if len(sample_patches) < 5:
            for i in range(min(images.size(0), 5 - len(sample_patches))):
                sample_patches.append((
                    images[i].cpu(),
                    masks[i].cpu(),
                    preds[i].cpu(),
                ))

    pred = torch.cat(all_preds)
    target = torch.cat(all_targets)
    probs_all = torch.cat(all_probs)
    metrics = compute_metrics(pred, target)
    return metrics, sample_patches, probs_all, target


def compute_ece(pred_probs: torch.Tensor, target: torch.Tensor, n_bins: int = 10):
    """
    Expected Calibration Error. Bins predicted probabilities and measures
    the gap between predicted confidence and actual accuracy.
    """
    confidences = pred_probs.max(dim=1).values
    predictions = pred_probs.argmax(dim=1)
    accuracies = (predictions == target).float()

    bin_boundaries = torch.linspace(0, 1, n_bins + 1)
    ece = 0.0
    for i in range(n_bins):
        in_bin = (confidences > bin_boundaries[i]) & (confidences <= bin_boundaries[i + 1])
        if in_bin.sum() > 0:
            bin_acc = accuracies[in_bin].mean()
            bin_conf = confidences[in_bin].mean()
            ece += (in_bin.sum().float() / confidences.numel()) * abs(bin_acc - bin_conf)
    return ece.item()


def plot_confusion_matrix(conf: np.ndarray, class_names: list[str], save_path: Path):
    """Plot normalized confusion matrix heatmap."""
    conf_norm = conf.astype(float) / conf.sum(axis=1, keepdims=True).clip(min=1)

    fig, ax = plt.subplots(figsize=(5, 4))
    im = ax.imshow(conf_norm, cmap="Blues", vmin=0, vmax=1)

    ax.set_xticks(range(len(class_names)))
    ax.set_yticks(range(len(class_names)))
    ax.set_xticklabels(class_names)
    ax.set_yticklabels(class_names)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("True")

    for i in range(len(class_names)):
        for j in range(len(class_names)):
            val = conf_norm[i, j]
            ax.text(j, i, f"{val:.2f}\n({int(conf[i, j])})",
                    ha="center", va="center",
                    color="white" if val > 0.5 else "black", fontsize=9)

    plt.colorbar(im, label="Normalized count")
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  Saved confusion matrix: {save_path}")


def plot_samples(samples: list, save_path: Path):
    """Plot 5 samples with image, GT, prediction, and error overlay."""
    fig, axes = plt.subplots(5, 4, figsize=(12, 12))
    class_names = ["Clear", "Cloud"]

    for row, (img, target, pred) in enumerate(samples):
        # Handle both torch tensors and numpy arrays
        if hasattr(img, "permute"):
            img_np = img.permute(1, 2, 0).numpy()
        else:
            img_np = img.transpose(1, 2, 0)
        img_np = (img_np - img_np.min()) / (img_np.max() - img_np.min() + 1e-8)

        # Convert to numpy if needed
        if hasattr(target, "numpy"):
            target_np = target.numpy()
            pred_np = pred.numpy()
        else:
            target_np = target
            pred_np = pred

        # Error overlay: red = FP (predicted cloud, actually clear)
        #                blue = FN (predicted clear, actually cloud)
        fp = (pred_np == 1) & (target_np == 0)
        fn = (pred_np == 0) & (target_np == 1)
        overlay = np.zeros((*target_np.shape, 3), dtype=np.float32)
        overlay[fp] = [1, 0, 0]   # red
        overlay[fn] = [0, 0, 1]   # blue

        axes[row, 0].imshow(img_np)
        axes[row, 0].set_title("Image")
        axes[row, 0].axis("off")

        axes[row, 1].imshow(target_np, cmap="Blues", vmin=0, vmax=1)
        axes[row, 1].set_title("Ground Truth")
        axes[row, 1].axis("off")

        axes[row, 2].imshow(pred_np, cmap="Blues", vmin=0, vmax=1)
        axes[row, 2].set_title("Prediction")
        axes[row, 2].axis("off")

        axes[row, 3].imshow(img_np * 0.3 + 0.7 * overlay)
        axes[row, 3].set_title("Errors: R=FP, B=FN")
        axes[row, 3].axis("off")

    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  Saved sample predictions: {save_path}")


def plot_metrics_bar(metrics: dict, save_path: Path):
    """Bar chart of key metrics."""
    names = ["mIoU", "Precision", "Recall", "F1", "Accuracy"]
    values = [metrics["mIoU"], metrics["precision"],
              metrics["recall"], metrics["f1"], metrics["accuracy"]]

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(names, values, color=["#2e86ab", "#36a2eb", "#ff6384", "#4bc0c0", "#ffce56"])
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
                f"{val:.4f}", ha="center", va="bottom", fontsize=9)
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("Score")
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  Saved metrics bar chart: {save_path}")


def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    # Load model with best checkpoint
    ckpt_path = CHECKPOINT_DIR / "best_model.pt"
    print(f"Loading checkpoint: {ckpt_path}")
    ckpt = torch.load(ckpt_path, map_location=device)
    model = CloudSegNet().to(device)
    model.load_state_dict(ckpt["model_state"])
    print(f"  Epoch {ckpt['epoch']}, val_mIoU = {ckpt['val_miou']:.4f}")
    print()

    # Data
    _, _, test_dl = get_dataloaders()
    print()

    # Evaluate
    metrics, samples, probs_all, target_all = evaluate(model, test_dl, device)
    print()

    # Confusion matrix
    conf = np.array(metrics["confusion_matrix"])
    print("Confusion matrix:")
    print(f"           Pred Clear  Pred Cloud")
    print(f"True Clear {conf[0, 0]:>6d}  {conf[0, 1]:>6d}")
    print(f"True Cloud {conf[1, 0]:>6d}  {conf[1, 1]:>6d}")
    print()

    # Print metrics
    print(f"mIoU:               {metrics['mIoU']:.4f}")
    print(f"Precision (macro):  {metrics['precision']:.4f}")
    print(f"Recall (macro):     {metrics['recall']:.4f}")
    print(f"F1 (macro):         {metrics['f1']:.4f}")
    print(f"Accuracy:           {metrics['accuracy']:.4f}")
    print(f"Cloud IoU:          {metrics['class_ious'][1]:.4f}")
    print(f"Clear IoU:          {metrics['class_ious'][0]:.4f}")
    print(f"Cloud precision:    {metrics['class_precisions'][1]:.4f}")
    print(f"Cloud recall:       {metrics['class_recalls'][1]:.4f}")
    print(f"FN rate (cloud):    {metrics['false_negative_rate']:.4f}")
    print(f"FP rate (cloud):    {metrics['false_positive_rate']:.4f}")
    print()

    # Confidence calibration
    ece = compute_ece(probs_all, target_all)
    print(f"ECE (Expected Calibration Error): {ece:.4f}")
    print()

    # Generate figures
    print("Generating figures...")
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    plot_confusion_matrix(conf, ["Clear", "Cloud"], FIGURE_DIR / "confusion_matrix.png")
    plot_samples(samples, FIGURE_DIR / "sample_predictions.png")
    plot_metrics_bar(metrics, FIGURE_DIR / "metrics_bar.png")
    print()

    # Save metrics as JSON
    report = {k: v for k, v in metrics.items() if k != "confusion_matrix"}
    report["ece"] = ece
    report_path = CHECKPOINT_DIR.parent / "logs" / "metrics.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"Saved metrics report: {report_path}")
    print("Done.")


if __name__ == "__main__":
    main()
