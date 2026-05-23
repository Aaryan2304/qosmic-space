---
type: subsystem
name: Fiber Coupling Module
description: Couples the free-space received beam into a single-mode fiber for delivery to the receiver electronics. Requires precise alignment to within ~1 micron.
status: active
parent:
---

# Fiber Coupling Module

## Overview

After the telescope collects and the AO system cleans up the beam, the light must be coupled into a single-mode fiber. This is the interface between the optical front-end and the receiver electronics.

For a standard SMF-28 fiber at 1550 nm, the mode field diameter is approximately 10.4 microns. The focused spot must match this size and be centered on the fiber core to within ~1 micron. Atmospheric turbulence, residual tracking errors, and optical aberrations all reduce coupling efficiency.

We chose single-mode over multi-mode coupling despite more stringent alignment requirements because our detector is fiber-coupled and designed for single-mode operation.

## Key Functions

- Couple free-space beam into single-mode fiber with maximum efficiency
- Maintain alignment during satellite tracking maneuvers
- Provide a beam sampler for wavefront sensing

## Related Design Decisions

- [[Single-Mode vs Multi-Mode Fiber Coupling]]

## Requirements Addressed

- [[REQ-001: 1 Gbps Downlink Rate]]

## Dependencies

- Depends on: [[Adaptive Optics System]]
- Depends on: [[Pointing and Tracking System]]

## References

- [[Cailabs OGS Technical Reference]]
