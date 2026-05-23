"""
Training loop for cloud segmentation model.

Runs on GPU with AMP (torch.amp). Logs loss and mIoU per epoch.
Saves checkpoint with best validation mIoU.
"""
import os
import time
from pathlib import Path

import torch
from torch.optim import AdamW
from torch.optim.lr_scheduler import CosineAnnealingLR
from torch.utils.data import DataLoader
from tqdm import tqdm

from config import (
    EPOCHS, BATCH_SIZE, LEARNING_RATE, WEIGHT_DECAY,
    SEED, CHECKPOINT_DIR, LOG_DIR, FIGURE_DIR, SAVE_BEST_ONLY,
)
from model import build_model
from loss import CloudSegLoss
from data_utils import get_dataloaders


def compute_iou(pred: torch.Tensor, target: torch.Tensor, num_classes: int = 2):
    """
    Per-class IoU and mean IoU.

    Args:
        pred: [B, H, W] long tensor of predicted class indices
        target: [B, H, W] long tensor of ground truth (0 or 1)
    Returns:
        ious: [num_classes] tensor of per-class IoU
        miou: scalar mean IoU
    """
    ious = []
    for c in range(num_classes):
        p = (pred == c)
        t = (target == c)
        inter = (p & t).sum().float()
        union = (p | t).sum().float()
        ious.append(inter / (union + 1e-8))
    ious = torch.stack(ious)
    return ious, ious.mean()


def train_one_epoch(
    model: torch.nn.Module,
    loader: DataLoader,
    optimizer: torch.optim.Optimizer,
    loss_fn: torch.nn.Module,
    scaler: torch.amp.GradScaler,
    device: torch.device,
) -> float:
    model.train()
    total_loss = 0.0
    batches = len(loader)

    pbar = tqdm(loader, desc="Train", leave=False)
    for images, masks in pbar:
        images = images.to(device, non_blocking=True)
        masks = masks.to(device, non_blocking=True)

        optimizer.zero_grad()

        with torch.amp.autocast("cuda"):
            logits = model(images)
            loss = loss_fn(logits, masks)

        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()

        total_loss += loss.item()
        pbar.set_postfix(loss=f"{loss.item():.4f}")

    return total_loss / batches


@torch.no_grad()
def validate(
    model: torch.nn.Module,
    loader: DataLoader,
    loss_fn: torch.nn.Module,
    device: torch.device,
) -> tuple[float, float]:
    model.eval()
    total_loss = 0.0
    total_miou = 0.0
    batches = len(loader)

    for images, masks in tqdm(loader, desc="Val", leave=False):
        images = images.to(device, non_blocking=True)
        masks = masks.to(device, non_blocking=True)

        with torch.amp.autocast("cuda"):
            logits = model(images)
            loss = loss_fn(logits, masks)

        preds = logits.argmax(dim=1)
        _, miou = compute_iou(preds, masks)

        total_loss += loss.item()
        total_miou += miou.item()

    return total_loss / batches, total_miou / batches


def train():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device} ({torch.cuda.get_device_name(0)})")
    print()

    # Data
    train_dl, val_dl, _ = get_dataloaders()
    print()

    # Model
    model = build_model(device)
    loss_fn = CloudSegLoss()

    # Optimiser & scheduler
    optimizer = AdamW(model.parameters(), lr=LEARNING_RATE, weight_decay=WEIGHT_DECAY)
    scheduler = CosineAnnealingLR(optimizer, T_max=EPOCHS, eta_min=1e-6)
    scaler = torch.amp.GradScaler("cuda")

    # Training loop
    best_miou = 0.0
    history = {"train_loss": [], "val_loss": [], "val_miou": []}
    start_time = time.time()

    for epoch in range(1, EPOCHS + 1):
        epoch_start = time.time()
        print(f"\nEpoch {epoch}/{EPOCHS}")

        train_loss = train_one_epoch(model, train_dl, optimizer, loss_fn, scaler, device)
        val_loss, val_miou = validate(model, val_dl, loss_fn, device)

        history["train_loss"].append(train_loss)
        history["val_loss"].append(val_loss)
        history["val_miou"].append(val_miou)

        epoch_time = time.time() - epoch_start
        print(
            f"  train_loss={train_loss:.4f}  val_loss={val_loss:.4f}  "
            f"val_mIoU={val_miou:.4f}  lr={scheduler.get_last_lr()[0]:.2e}  "
            f"took={epoch_time:.0f}s"
        )

        # Checkpoint
        if val_miou > best_miou:
            best_miou = val_miou
            ckpt_path = CHECKPOINT_DIR / "best_model.pt"
            torch.save(
                {
                    "epoch": epoch,
                    "model_state": model.state_dict(),
                    "val_miou": val_miou,
                },
                ckpt_path,
            )
            print(f"  New best model saved to {ckpt_path} (mIoU={val_miou:.4f})")

        scheduler.step()

    total_time = time.time() - start_time
    print(f"\nTraining complete. Best val mIoU: {best_miou:.4f}")
    print(f"Total time: {total_time / 60:.1f} minutes")

    return history


if __name__ == "__main__":
    train()
