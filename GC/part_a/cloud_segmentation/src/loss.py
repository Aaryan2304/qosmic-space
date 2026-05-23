"""
Combined loss: Dice + Focal for binary cloud segmentation.

Dice loss handles class imbalance well. Focal loss downweights easy examples and focuses on hard-to-classify pixels (cloud edges, thin cirrus).
"""
import torch
import torch.nn as nn
import torch.nn.functional as F

from config import DICE_WEIGHT, FOCAL_WEIGHT, FOCAL_GAMMA, FOCAL_ALPHA


class DiceLoss(nn.Module):
    """Soft Dice loss for binary segmentation."""

    def __init__(self, smooth: float = 1.0):
        super().__init__()
        self.smooth = smooth

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        """
        Args:
            logits: [B, 2, H, W] raw logits
            targets: [B, H, W] long tensor (0 or 1)
        """
        probs = F.softmax(logits, dim=1)[:, 1]
        targets_f = targets.float()

        intersection = (probs * targets_f).sum()
        union = probs.sum() + targets_f.sum()

        dice = (2.0 * intersection + self.smooth) / (union + self.smooth)
        return 1.0 - dice


class FocalLoss(nn.Module):
    """Focal loss for binary segmentation. Downweights easy examples."""

    def __init__(self, gamma: float = FOCAL_GAMMA, alpha: float = FOCAL_ALPHA):
        super().__init__()
        self.gamma = gamma
        self.alpha = alpha

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        """
        Args:
            logits: [B, 2, H, W] raw logits
            targets: [B, H, W] long tensor (0 or 1)
        """
        ce = F.cross_entropy(logits, targets, reduction="none")
        pt = torch.exp(-ce)
        alpha_t = self.alpha * targets.float() + (1 - self.alpha) * (1 - targets.float())
        focal = alpha_t * (1 - pt) ** self.gamma * ce
        return focal.mean()


class CloudSegLoss(nn.Module):
    """Combined Dice + Focal loss."""

    def __init__(self):
        super().__init__()
        self.dice = DiceLoss()
        self.focal = FocalLoss()

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        return DICE_WEIGHT * self.dice(logits, targets) + FOCAL_WEIGHT * self.focal(logits, targets)
