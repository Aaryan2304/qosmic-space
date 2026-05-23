"""
Cloud segmentation model: U-Net with EfficientNet-B0 backbone.

Uses segmentation_models_pytorch for the decoder. Encoder is pretrained on ImageNet. Input is 3-channel RGB (Landsat 8 bands 2,3,4).

For the multi-sensor extension (mentioned in the write-up), the encoder's first conv layer would be replaced to accept variable channel counts, and a spectral projection layer would map arbitrary bands to a shared latent space.
"""
import torch
import torch.nn as nn
import segmentation_models_pytorch as smp

from config import BACKBONE, IN_CHANNELS, NUM_CLASSES, ENCODER_WEIGHTS


class CloudSegNet(nn.Module):
    """
    U-Net for binary cloud segmentation.

    Args:
        backbone: Encoder name (e.g. 'efficientnet-b0')
        in_channels: Number of input bands (3 for RGB)
        num_classes: Number of output classes (2: clear, cloud)
        encoder_weights: Pretrained weights ('imagenet' or None)
    """

    def __init__(
        self,
        backbone: str = BACKBONE,
        in_channels: int = IN_CHANNELS,
        num_classes: int = NUM_CLASSES,
        encoder_weights: str = ENCODER_WEIGHTS,
    ):
        super().__init__()
        self.model = smp.Unet(
            encoder_name=backbone,
            encoder_weights=encoder_weights,
            in_channels=in_channels,
            classes=num_classes,
            activation=None,  # Raw logits; softmax applied in loss
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: [B, 3, H, W] — normalized RGB image
        Returns:
            logits: [B, 2, H, W] — raw logits per class
        """
        return self.model(x)

    def predict(self, x: torch.Tensor) -> torch.Tensor:
        """Return class predictions (argmax)."""
        with torch.no_grad():
            logits = self.forward(x)
            return logits.argmax(dim=1)

    def count_parameters(self) -> int:
        return sum(p.numel() for p in self.model.parameters() if p.requires_grad)


def build_model(device: torch.device = torch.device("cuda")) -> CloudSegNet:
    """Build model and move to device."""
    model = CloudSegNet()
    model = model.to(device)
    print(f"Model: {BACKBONE} U-Net, {model.count_parameters():,} trainable params")
    return model
