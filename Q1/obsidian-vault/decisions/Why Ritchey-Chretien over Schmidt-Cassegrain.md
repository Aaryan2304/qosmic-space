---
type: decision
title: Why Ritchey-Chretien over Schmidt-Cassegrain
status: accepted
date: 2025-06-15
author: Aaryan
subsystem: [[Telescope Assembly]]
alternatives_considered:
  - Schmidt-Cassegrain (SCT)
  - Ritchey-Chretien (RC)
  - Maksutov-Cassegrain
tradeoffs: RC has higher manufacturing cost but eliminates coma across the field of view, critical for off-axis satellite tracking. SCT is cheaper but introduces coma at field edges.
physics_rationale: RC uses hyperbolic primary and secondary mirrors to eliminate third-order coma, providing a wider usable field of view. For satellite tracking where the target may be off-axis during acquisition, this is essential.
---

# Why Ritchey-Chretien over Schmidt-Cassegrain

## Context

This decision was driven by REQ-002: Pointing Accuracy < 10 urad. During satellite acquisition, the target may be several arcminutes off-axis before the tracking loop closes. If the telescope has significant coma, the blurred image on the tracking sensor reduces SNR and slows acquisition.

## Alternatives Evaluated

### Schmidt-Cassegrain (SCT)
- **Pros:** Lower cost, simpler alignment, widely available
- **Cons:** Residual coma limits useful field of view to ~15 arcmin. Corrector plate adds a glass surface (light loss, thermal sensitivity).

### Ritchey-Chretien (RC)
- **Pros:** Coma-free field of view (~30 arcmin or more). No corrector plate (all-reflective, lower loss, works at 1550 nm without chromatic issues).
- **Cons:** Higher manufacturing cost (hyperbolic mirrors are harder to fabricate and test). More sensitive to mirror misalignment.

### Maksutov-Cassegrain
- **Pros:** Compact, sealed tube, good correction
- **Cons:** Heavy corrector lens, thermal mass, not ideal for rapid pointing changes

## Decision

Selected Ritchey-Chretien. The coma-free field directly supports faster satellite acquisition and better off-axis tracking performance. The all-reflective design is better suited for 1550 nm operation (no chromatic aberration from corrector elements).

## Trade-offs

| Criterion | RC (Chosen) | SCT (Rejected) |
|-----------|-------------|----------------|
| Cost | Higher (~2x) | Lower |
| Field of view | Coma-free, ~30+ arcmin | Limited by coma, ~15 arcmin |
| 1550 nm performance | Excellent (all-reflective) | Good (corrector chromatic effects) |
| Alignment sensitivity | Higher | Lower |

## Derives From

- [[REQ-002: Pointing Accuracy < 10 urad]]

## Justified By

- [[Coma Aberration in Optical Systems]]

## References

- [[Cailabs OGS Technical Reference]]
