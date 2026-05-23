---
type: requirement
id: REQ-001
text: The ground station shall achieve a minimum downlink data rate of 1 Gbps from LEO satellites at 500 km altitude under clear-sky conditions.
source: customer
priority: critical
verification_method: test
---

# REQ-001: 1 Gbps Downlink Rate

## Statement

The ground station shall achieve a minimum downlink data rate of 1 Gbps from LEO satellites at 500 km altitude under clear-sky conditions (cloud optical depth < 0.3).

## Rationale

The primary mission requires daily download of ~50 GB from a LEO imaging satellite. With ~4 passes/day and ~7 minutes of contact per pass, the link must sustain 1 Gbps to transfer the required data within available contact time.

This requirement drives telescope aperture, adaptive optics, fiber coupling, receiver sensitivity, and data processing throughput.

## Verification

End-to-end link testing using a calibrated optical source at far field (5 km terrestrial range or cooperative satellite pass). Measure sustained data rate over a complete pass, confirm BER < 10^{-9}.

## Allocated To

- [[Telescope Assembly]]
- [[Adaptive Optics System]]
- [[Fiber Coupling Module]]
- [[Receiver Electronics]]
- [[Control Software]]

## Related Decisions

- [[Why Ritchey-Chretien over Schmidt-Cassegrain]]
- [[Adaptive Optics: Tip-Tilt vs Higher-Order Correction]]
- [[Single-Mode vs Multi-Mode Fiber Coupling]]

## Tested By

- [[Cailabs OGS Technical Reference]]
