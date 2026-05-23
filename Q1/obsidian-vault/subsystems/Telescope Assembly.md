---
type: subsystem
name: Telescope Assembly
description: The optical front-end of the ground station. Collects incoming laser light from satellites and focuses it into the fiber coupling module.
status: active
parent:
---

# Telescope Assembly

## Overview

The telescope assembly is the optical front-end of the ground station. Its job: collect as much of the incoming laser signal as possible and deliver it, with minimal loss and distortion, to the fiber coupling module behind it.

Our station uses a 50 cm class Ritchey-Chretien telescope. The choice of RC over Schmidt-Cassegrain was one of the earliest and most consequential design decisions.

## Key Functions

- Collect incoming photons from the satellite laser link
- Focus the collimated beam onto the fiber coupling unit
- Provide a stable optical bench for downstream subsystems

## Optical Specifications

| Parameter | Value |
|-----------|-------|
| Aperture | 50 cm |
| Design | Ritchey-Chretien (RC) |
| Focal ratio | f/8 (nominal) |
| Field of view | ~0.5 degrees (coma-free) |
| Mirror coating | Protected silver (optimized for 1550 nm) |

## Related Design Decisions

- [[Why Ritchey-Chretien over Schmidt-Cassegrain]]

## Requirements Addressed

- [[REQ-001: 1 Gbps Downlink Rate]]
- [[REQ-002: Pointing Accuracy < 10 urad]]

## Dependencies

- Depends on: [[Pointing and Tracking System]]
- Depends on: [[Site Infrastructure]]

## References

- [[Cailabs OGS Technical Reference]]
