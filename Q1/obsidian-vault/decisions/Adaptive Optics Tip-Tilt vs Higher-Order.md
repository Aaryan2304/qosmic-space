---
type: decision
title: Adaptive Optics - Tip-Tilt vs Higher-Order Correction
status: accepted
date: 2025-07-20
author: Aaryan
subsystem: [[Adaptive Optics System]]
alternatives_considered:
  - Tip-tilt correction only (1 actuator)
  - Higher-order correction (40+ actuator deformable mirror)
tradeoffs: Tip-tilt removes ~60% of turbulence-induced wavefront error at low cost. Higher-order correction removes 90%+ but adds significant complexity, cost, and alignment sensitivity.
physics_rationale: Atmospheric turbulence tip-tilt accounts for ~60% of total wavefront variance (Noll 1976). For our initial deployment, recovering 60% of the turbulence loss is sufficient to meet REQ-001. Higher-order correction is deferred to a future upgrade.
---

# Adaptive Optics - Tip-Tilt vs Higher-Order Correction

## Context

Driven by REQ-001: 1 Gbps Downlink Rate. Atmospheric turbulence reduces fiber coupling efficiency. The question is how much correction is needed for the initial deployment.

## Alternatives Evaluated

### Tip-tilt only
- **Pros:** Simple (single actuator), low cost, proven technology, low latency
- **Cons:** Corrects only ~60% of turbulence wavefront error. Residual higher-order aberrations still reduce coupling efficiency.

### Higher-order (40+ actuator DM)
- **Pros:** Corrects 90%+ of turbulence wavefront error. Significantly better coupling efficiency.
- **Cons:** Expensive (deformable mirror ~Rs. 15L+), complex wavefront sensor required, higher latency, more alignment-sensitive.

## Decision

Selected tip-tilt only for initial deployment. This recovers the majority of the turbulence-induced coupling loss at manageable cost. Higher-order correction is a planned upgrade path once the basic link is operational.

## Trade-offs

| Criterion | Tip-tilt (Chosen) | Higher-order (Deferred) |
|-----------|-------------------|------------------------|
| Wavefront correction | ~60% | ~90%+ |
| Cost | ~Rs. 5L | ~Rs. 20L+ |
| Complexity | Low | High |
| Latency | < 1 ms | ~5 ms |

## Derives From

- [[REQ-001: 1 Gbps Downlink Rate]]

## Justified By

- [[Atmospheric Turbulence: Kolmogorov Model]]

## References

- [[Cailabs OGS Technical Reference]]
