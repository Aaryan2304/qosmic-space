---
type: decision
title: Single-Mode vs Multi-Mode Fiber Coupling
status: accepted
date: 2025-08-01
author: Aaryan
subsystem: [[Fiber Coupling Module]]
alternatives_considered:
  - Multi-mode fiber (50-62.5 micron core)
  - Single-mode fiber (9 micron core, SMF-28)
tradeoffs: Single-mode gives better detector compatibility and no modal noise but requires alignment to ~1 micron. Multi-mode is more forgiving (~10 micron tolerance) but introduces modal noise and is incompatible with our fiber-coupled InGaAs detector.
physics_rationale: Our InGaAs single-photon detector is fiber-coupled with single-mode fiber input. Using multi-mode fiber would require a mode-matching interface that adds loss and complexity. Single-mode coupling is the natural choice given our detector.
---

# Single-Mode vs Multi-Mode Fiber Coupling

## Context

Driven by REQ-001: 1 Gbps Downlink Rate. The fiber coupling interface must deliver maximum optical power to the receiver detector.

## Alternatives Evaluated

### Multi-mode fiber (50-62.5 micron core)
- **Pros:** Alignment tolerance ~10 microns (easier to maintain during tracking). Larger capture area.
- **Cons:** Modal noise degrades signal quality at high data rates. Incompatible with our fiber-coupled InGaAs single-photon detector without additional mode-matching optics.

### Single-mode fiber (9 micron core, SMF-28)
- **Pros:** No modal noise. Directly compatible with our fiber-coupled InGaAs single-photon detector. Cleaner signal for both classical and quantum detection.
- **Cons:** Alignment tolerance ~1 micron (requires more precise tracking and AO correction).

## Decision

Selected single-mode fiber (SMF-28). The detector compatibility is the deciding factor. Our InGaAs single-photon detector has a single-mode fiber input, and adding a mode-matching interface for multi-mode would introduce unnecessary loss and complexity.

The tighter alignment requirement is managed by the AO system (tip-tilt correction) and the FSM tracking loop.

## Trade-offs

| Criterion | Single-mode (Chosen) | Multi-mode (Rejected) |
|-----------|---------------------|----------------------|
| Alignment tolerance | ~1 micron | ~10 microns |
| Modal noise | None | Present at high data rates |
| Detector compatibility | Direct | Requires mode-matching |
| Coupling efficiency (with AO) | 60-70% | 70-80% |

## Derives From

- [[REQ-001: 1 Gbps Downlink Rate]]

## Justified By

- [[Coma Aberration in Optical Systems]]

## Implemented By

- [[InGaAs Single-Photon Detector Module]]

## References

- [[Cailabs OGS Technical Reference]]
