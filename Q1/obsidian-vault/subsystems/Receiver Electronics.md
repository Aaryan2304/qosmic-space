---
type: subsystem
name: Receiver Electronics
description: Detects the incoming optical signal after fiber coupling. Uses single-photon avalanche photodiodes for quantum-limited detection of weak laser signals from LEO satellites.
status: active
parent:
---

# Receiver Electronics

## Overview

The receiver electronics sit downstream of the fiber coupling module. At 1 Gbps with a 1550 nm laser, we are detecting on the order of hundreds of photons per bit after all the losses. For QKD applications, the receiver must detect individual photons with precise time-tagging.

## Key Functions

- Photon detection with high quantum efficiency at 1550 nm
- Time-stamping of detected photons for QKD post-processing
- Signal demodulation for classical communication channels

## Detector Specifications

| Parameter | Value |
|-----------|-------|
| Detector type | InGaAs/InP SPAD (gated mode) |
| Model | ID230 (ID Quantique) |
| Spectral range | 900 - 1650 nm |
| PDE at 1550 nm | 10 - 25% |
| Dark count rate | 1 - 10 kHz |
| Time resolution | < 200 ps |
| Operating temp | 223 K (thermoelectric) |

## Requirements Addressed

- [[REQ-001: 1 Gbps Downlink Rate]]

## Dependencies

- Depends on: [[Fiber Coupling Module]]
- Depends on: [[Control Software]]

## References

- [[BB84 Decoy-State Protocol]]
