"""
Dataset utilities for 38-Cloud cloud segmentation.

38-Cloud structure (from Kaggle, verified 2026-05-18):
    archive/
        38-Cloud_training/
            train_red/       → Red band (band 4) patches, 16-bit TIFF, 384x384
            train_green/     → Green band (band 3) patches
            train_blue/      → Blue band (band 2) patches
            train_nir/       → NIR band (band 5) patches
            train_gt/        → Binary cloud masks (0=clear, 255=cloud), 8-bit
            training_patches_38-Cloud.csv   → patch names (col 0)
            training_sceneids_38-Cloud.csv  → scene IDs (col 0 = name, col 1 = id)
        38-Cloud_test/
            test_red/, test_green/, test_blue/, test_nir/
            NO test_gt/  → Test set has no per-patch labels.
                          Only full-scene GTs in Entire_scene_gts/

I split the 18 training scenes into train/val/test geographically:
    Train: 12 scenes  (~5,500 patches)
    Val:   3 scenes   (~1,350 patches)
    Test:  3 scenes   (~1,550 patches)

Each band is stored as a separate 16-bit TIFF. I stack R+G+B into a 3-channel float tensor and normalize by /65535.0.
"""
import csv
import re
from pathlib import Path

import numpy as np
import torch
from PIL import Image
from torch.utils.data import Dataset, DataLoader

from config import (
    DATA_DIR, BATCH_SIZE, NUM_WORKERS, PIN_MEMORY,
    RANDOM_CROP_SIZE, HORIZONTAL_FLIP_PROB, VERTICAL_FLIP_PROB,
    ROTATION_DEGREES, VAL_SCENE_IDS, TEST_SCENE_IDS, SEED,
)


TRAIN_DIR = DATA_DIR / "archive" / "38-Cloud_training"


def read_patch_csv(path: Path) -> list[str]:
    """Read patch names from 38-Cloud CSV, skipping header."""
    with open(path, "r") as f:
        reader = csv.reader(f)
        next(reader)
        return [row[0] for row in reader]


def extract_scene_id_from_patch_name(patch_name: str) -> str:
    """
    Extract Landsat scene ID from CSV patch name.

    CSV patch name format:
        patch_1_1_by_1_LC08_L1TP_002053_20160520_20170324_01_T1
    The scene ID is everything after the coordinate pattern "by_N_".
    """
    parts = patch_name.split("_")
    by_idx = parts.index("by")
    return "_".join(parts[by_idx + 2:])


def build_scene_split(
    patch_ids: list[str],
    val_scenes: set[str],
    test_scenes: set[str] | None = None,
):
    """
    Split patches by scene ID for geographic separation.

    Returns:
        train_ids, val_ids, (test_ids or None)
    """
    if test_scenes is None:
        test_scenes = set()

    train_ids, val_ids, test_ids = [], [], []
    for pid in patch_ids:
        sid = extract_scene_id_from_patch_name(pid)
        if sid in test_scenes:
            test_ids.append(pid)
        elif sid in val_scenes:
            val_ids.append(pid)
        else:
            train_ids.append(pid)
    return train_ids, val_ids, test_ids


def filter_nonempty_patches(root_dir: Path, patch_ids: list[str]) -> list[str]:
    """
    Remove patches where ALL pixels in the red band are zero.
    These are border patches with no data (common in 38-Cloud).
    """
    filtered = []
    for pid in patch_ids:
        tif = f"red_{pid}.TIF"
        img = np.array(Image.open(root_dir / "train_red" / tif))
        if img.max() > 0:
            filtered.append(pid)
    return filtered


class Cloud38Dataset(Dataset):
    """
    Loads R+G+B band patches from 38-Cloud as 3-channel tensors.

    Args:
        root_dir: Path to 38-Cloud_training/
        patch_ids: List of CSV patch names (without band prefix or extension)
        transform: Albumentations transform pipeline
    """

    def __init__(self, root_dir: Path, patch_ids: list[str], transform=None):
        self.root_dir = Path(root_dir)
        self.patch_ids = patch_ids
        self.transform = transform

    def __len__(self) -> int:
        return len(self.patch_ids)

    def __getitem__(self, idx: int):
        csv_name = self.patch_ids[idx]

        # Build filenames from CSV patch name
        # CSV: patch_1_1_by_1_LC08_...
        # Band: red_patch_1_1_by_1_LC08_...TIF
        # GT:   gt_patch_1_1_by_1_LC08_...TIF
        tif_name = f"{csv_name}.TIF"
        red = np.array(Image.open(self.root_dir / "train_red" / f"red_{tif_name}"))
        green = np.array(Image.open(self.root_dir / "train_green" / f"green_{tif_name}"))
        blue = np.array(Image.open(self.root_dir / "train_blue" / f"blue_{tif_name}"))
        gt = np.array(Image.open(self.root_dir / "train_gt" / f"gt_{tif_name}"))

        # Stack bands → [3, H, W] float, normalize 16-bit to [0, 1]
        image = np.stack([red, green, blue], axis=0).astype(np.float32) / 65535.0

        # Binary mask: cloud=1, clear=0
        mask = (gt > 127).astype(np.float32)

        # Apply transforms
        if self.transform:
            augmented = self.transform(image=image.transpose(1, 2, 0), mask=mask)
            return augmented["image"], augmented["mask"].long()

        return torch.from_numpy(image), torch.from_numpy(mask).long()


def build_transforms(is_train: bool = True):
    """Build albumentations transforms."""
    import albumentations as A
    from albumentations.pytorch import ToTensorV2

    if is_train:
        return A.Compose([
            A.RandomCrop(RANDOM_CROP_SIZE, RANDOM_CROP_SIZE),
            A.HorizontalFlip(p=HORIZONTAL_FLIP_PROB),
            A.VerticalFlip(p=VERTICAL_FLIP_PROB),
            A.Rotate(limit=ROTATION_DEGREES),
            A.Normalize(mean=[0.485, 0.456, 0.406],
                        std=[0.229, 0.224, 0.225]),
            ToTensorV2(),
        ])
    return A.Compose([
        A.Normalize(mean=[0.485, 0.456, 0.406],
                    std=[0.229, 0.224, 0.225]),
        ToTensorV2(),
    ])


def get_dataloaders():
    """
    Build train/val/test DataLoaders with geographic split.

    Splits:  12 train scenes, 3 val scenes, 3 test scenes
    All from the 18 training scenes (test set has no per-patch GTs).
    """
    all_train_ids = read_patch_csv(TRAIN_DIR / "training_patches_38-Cloud.csv")

    train_ids, val_ids, test_ids = build_scene_split(
        all_train_ids,
        val_scenes=set(VAL_SCENE_IDS),
        test_scenes=set(TEST_SCENE_IDS),
    )

    # Remove empty border patches
    train_ids = filter_nonempty_patches(TRAIN_DIR, train_ids)
    val_ids = filter_nonempty_patches(TRAIN_DIR, val_ids)
    test_ids = filter_nonempty_patches(TRAIN_DIR, test_ids)

    # Build datasets
    train_ds = Cloud38Dataset(TRAIN_DIR, train_ids, transform=build_transforms(True))
    val_ds = Cloud38Dataset(TRAIN_DIR, val_ids, transform=build_transforms(False))
    test_ds = Cloud38Dataset(TRAIN_DIR, test_ids, transform=build_transforms(False))

    # Build dataloaders
    train_dl = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True,
                          num_workers=NUM_WORKERS, pin_memory=PIN_MEMORY, drop_last=True)
    val_dl = DataLoader(val_ds, batch_size=BATCH_SIZE, shuffle=False,
                        num_workers=NUM_WORKERS, pin_memory=PIN_MEMORY)
    test_dl = DataLoader(test_ds, batch_size=BATCH_SIZE, shuffle=False,
                         num_workers=NUM_WORKERS, pin_memory=PIN_MEMORY)

    print(f"Train: {len(train_ds)} patches | Val: {len(val_ds)} | Test: {len(test_ds)}")
    return train_dl, val_dl, test_dl

