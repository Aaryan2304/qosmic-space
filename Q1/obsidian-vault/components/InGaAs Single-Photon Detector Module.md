---
type: component
name: InGaAs Single-Photon Detector Module
vendor: ID Quantique (or Micro Photon Devices)
part_number: ID230 (or PDM-R)
cost_inr: 1200000
lead_time_weeks: 12
datasheet_url: https://www.idquantique.com/quantum-sensing/products/id230/
status: active
---

# InGaAs Single-Photon Detector Module

## Specifications

| Parameter | Value |
|-----------|-------|
| Type | InGaAs/InP SPAD (gated mode) |
| Model | ID230 (ID Quantique) or PDM-R (MPD) |
| Spectral range | 900 - 1650 nm |
| Peak PDE at 1550 nm | 10 - 25% |
| Dark count rate | 1 - 10 kHz (at 10% PDE, 223 K) |
| Dead time | 10 - 20 us |
| Time resolution | < 200 ps |
| Operating temperature | 223 K (thermoelectric cooling) |
| Price (2025) | ~Rs. 12,00,000 |

## Usage in System

This is the primary photon detector for both classical communication and QKD receiver channels at 1550 nm. It is fiber-coupled (single-mode fiber input) and operates in gated Geiger mode for single-photon sensitivity.

For QKD (BB84 protocol), the detector must time-stamp individual photon arrivals with sub-nanosecond precision. The ID230's time resolution of < 200 ps is sufficient.

The PDE of 10-25% at 1550 nm is significantly lower than silicon MPPCs achieve at visible wavelengths, but this is the physical limit for InGaAs detectors at telecom wavelengths. For higher PDE, a superconducting nanowire single-photon detector (SNSPD) would be needed, but at much higher cost and complexity.

## Related Design Decisions

- [[Single-Mode vs Multi-Mode Fiber Coupling]]

## Used By

- [[Receiver Electronics]]
- [[Fiber Coupling Module]]

## Substitutes

- Excelitas SPCM (silicon SPAD, but only works to ~1000 nm — not suitable for 1550 nm)
- ID Quantique ID281 SNSPD (superconducting, > 80% PDE at 1550 nm, cryogenic at 0.8 K, ~Rs. 25,00,000)
- Micro Photon Devices PDM-R series (similar performance to ID230, ~Rs. 10,00,000)
