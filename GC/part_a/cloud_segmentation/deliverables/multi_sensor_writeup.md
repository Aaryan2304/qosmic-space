# Extending the Single-Sensor Prototype to Multi-Sensor Architecture

## 1. Why Not Separate Models Per Sensor

Training one model per sensor sounds simpler but fails operationally. Cloud physics is universal — the spectral signature of an ice cloud, a water cloud, or thin cirrus is determined by the physics of light scattering, not by which satellite carries the sensor. A model trained on Sentinel-2 band 4 (665nm) has already learned something about how clouds look at that wavelength; INSAT-3D's visible band at 650nm observes the same physics. Throwing that knowledge away to train a separate model from scratch wastes data, compute, and time.

More practically: a single model deployed in production means one inference pipeline, one set of weights to update, one ONNX export to validate. Three separate models means three of everything. For a startup with a small engineering team, this matters.

## 2. Architecture: Spectrum-Aware Projection

The current prototype is a U-Net with an EfficientNet-B0 encoder, taking 3-channel RGB input [B, 3, 384, 384] and producing 2-class logits [B, 2, 384, 384]. The encoder expects 3 channels fixed at the first conv layer.

To accept variable-band inputs, we insert a projection layer before the encoder:

```
Input: [B, C, H, W] where C varies per sensor (4 for Landsat 8, 13 for Sentinel-2, 6 for INSAT-3D)
    │
    ▼
Spectral Projection:
  Per-band 1×1 Conv → LayerNorm → ReLU
  Each of the C bands is processed independently through a shared-weight
  conv that maps a single band to a D-dimensional feature map.
  Output: [B, C, D, H, W]
    │
    ▼
Band Pooling:
  Mean over the C dimension → [B, D, H, W]
  This makes the representation invariant to the number of input bands.
  A sensor with 13 bands and a sensor with 4 bands both produce [B, D, H, W].
    │
    ▼
1×1 Conv → [B, 3, H, W] (match EfficientNet-B0 input channels)
    │
    ▼
Encoder (EfficientNet-B0, ImageNet pretrained weights)
```

The key detail: each band carries a spectral position embedding — a learned vector tied to the central wavelength of the band. Band 4 of Sentinel-2 (665nm) and the visible band of INSAT-3D (~650nm) get similar embeddings. Band 12 of Sentinel-2 (2190nm SWIR) and a thermal band (10.8µm) get very different ones. The encoder learns that "bands at this spectral position behave like this for cloud detection."

## 3. Handling Missing Bands

A sensor without thermal bands (Sentinel-2) should still produce reasonable predictions. The band pooling handles this naturally — it averages over whatever bands are available. If thermal bands are present, the model learns to use them. If absent, the mean pool still produces a valid D-dimensional vector, just one that contains less information about cloud-top temperature.

Training with random band dropout (drop each band with 10% probability during training) forces the model to not become dependent on any single band. This is the same technique used in sensor-agnostic remote sensing work.

## 4. Data Requirements

To train the multi-sensor model, we need co-located, co-timestamped image pairs from multiple sensors. The ideal setup:

- **Sentinel-2:** ~50,000 patches from diverse geographies, labelled with SCL-derived cloud masks. 10-60m resolution. 5-day revisit. 13 spectral bands including VIS, NIR, SWIR.
- **INSAT-3D:** ~10,000 patches over India, labelled from the same SCL-derived masks where S2 passes overlap within 30 minutes. 1-4km resolution. 15-30 minute revisit. 6 bands including two thermal IR channels (10.8µm, 12.0µm).
- **Landsat 8/9:** ~10,000 patches. 30m resolution. 16-day revisit. Adds thermal band (TIRS) which neither S2 nor INSAT-3D alone provides.

The challenge is resolution: 10m S2 patches at 384×384 cover a 3.84 km area, while 1km INSAT-3D data at the same patch size covers 384 km. Training at native resolution would mean the S2 encoder sees trees and roads while INSAT-3D sees weather systems. The solution is to train the spectral projection layer on downsampled S2 (to match INSAT resolution) and the segmentation head on both scales.

## 5. Training Pipeline

1. Pre-train the encoder + decoder on Sentinel-2 alone (large dataset, no spectral projection needed). This is what the current prototype does.
2. Freeze encoder and decoder weights.
3. Insert the spectral projection layer. Train it on mixed S2 + INSAT-3D data while keeping everything else frozen. The projection layer learns to map arbitrary-band inputs to the feature space the encoder expects.
4. Unfreeze the decoder. Fine-tune all layers jointly on mixed data with a lower learning rate (1e-4).
5. Evaluate on held-out test pairs from each sensor separately and on cross-sensor pairs.

## 6. Expected Failure Modes

**Resolution mismatch.** The 100× resolution gap between S2 (10m) and INSAT-3D (1km) means the model sees fundamentally different spatial structures. A cloud that covers a few S2 pixels might fill an entire INSAT-3D pixel. Mitigation: train on S2 downsampled to 1km for the joint training phase. Use full-resolution S2 only for the pre-training phase.

**Band absence.** A sensor without SWIR (like INSAT-3D) cannot distinguish thin cirrus from clear sky — cirrus is transparent in VIS but visible in SWIR. The model should output lower confidence when SWIR bands are absent. This can be trained by randomly dropping SWIR bands during training so the model learns to calibrate its confidence to available bands.

**Temporal misalignment.** S2 passes every 5 days; INSAT-3D images every 15 minutes. A cloud at 10:00 on INSAT-3D will have moved or dissipated by the next S2 overpass. Temporal consistency across the high-cadence INSAT frames can serve as a self-supervised signal — the model can be trained to produce cloud masks that are temporally smooth between consecutive INSAT frames.

## 7. Evaluation Plan

| Scenario | Train set | Test set | Expected mIoU |
|---|---|---|---|
| Same-sensor | S2 only | S2 (held-out) | 0.78-0.85 |
| Cross-sensor (easy) | S2 only | Landsat 8 | 0.65-0.75 |
| Cross-sensor (hard) | S2 only | INSAT-3D | 0.45-0.60 |
| Multi-sensor trained | S2 + INSAT | INSAT-3D | 0.65-0.78 |
| Multi-sensor trained | S2 + INSAT + L8 | All test sets | 0.70-0.80 |

Metrics beyond mIoU: false negative rate on thin cirrus (the operational risk), calibration error per sensor, and inference time per patch on a CPU (since INSAT-3D processing might not have GPU access).

---

*This write-up describes the architecture to extend the Landsat 8 prototype (Section 2) to multiple sensors. The prototype achieved 82.2% validation mIoU on a single sensor and revealed a 65% false negative rate on clouds in the held-out test set. The multi-sensor architecture addresses this weakness by leveraging INSAT-3D's high temporal frequency (15-minute updates) to improve cloud detection confidence through temporal consistency, and Sentinel-2's dense spectral coverage to better characterise thin cirrus and cloud edges.*
