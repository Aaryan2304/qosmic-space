---
type: subsystem
name: Adaptive Optics System
description: Measures and corrects atmospheric turbulence-induced wavefront distortions in real time. Uses a tip-tilt mirror for fast jitter correction.
status: active
parent:
---

# Adaptive Optics System

## Overview

Even with perfect pointing, the signal arriving at the ground station has been distorted by atmospheric turbulence. Variations in the refractive index along the beam path cause the wavefront to arrive corrugated rather than flat, reducing coupling efficiency into the single-mode fiber.

The AO system measures these distortions and corrects them using deformable optical elements. For our ground station, the minimum viable AO system is tip-tilt correction -- removing the lowest-order aberration caused by turbulence. Higher-order correction using a deformable mirror is an upgrade path for higher data rates.

## Key Functions

- Measure incoming wavefront distortion using a wavefront sensor
- Correct tip-tilt errors using a fast steering mirror
- Optionally correct higher-order aberrations using a deformable mirror
- Maintain correction bandwidth of ~100 Hz

## Related Design Decisions

- [[Adaptive Optics: Tip-Tilt vs Higher-Order Correction]]

## Requirements Addressed

- [[REQ-001: 1 Gbps Downlink Rate]]

## Dependencies

- Depends on: [[Telescope Assembly]]
- Depends on: [[Fiber Coupling Module]]

## References

- [[Cailabs OGS Technical Reference]]
