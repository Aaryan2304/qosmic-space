---
type: requirement
id: REQ-002
text: The ground station shall achieve a pointing accuracy of less than 10 microradians (RMS) during satellite tracking.
source: physics
priority: critical
verification_method: test
---

# REQ-002: Pointing Accuracy < 10 urad

## Statement

The ground station shall achieve a pointing accuracy of less than 10 microradians (RMS) during satellite tracking, measured at the telescope output focal plane.

## Rationale

The communication beam divergence is on the order of 10-20 microradians. To maintain link, the pointing error must be a small fraction of this. Additionally, the single-mode fiber coupling efficiency drops significantly if the beam is misaligned by more than a fraction of the mode field radius at the fiber, which corresponds to ~5 microradians at the telescope output.

This requirement drives the FSM bandwidth, tracking sensor noise, control loop design, and mechanical vibration isolation.

## Verification

Measured by recording the tracking sensor error signal during a satellite pass and computing the RMS pointing residual after removing the known trajectory. Must be < 10 urad RMS over 90% of the pass duration.

## Allocated To

- [[Telescope Assembly]]
- [[Pointing and Tracking System]]
- [[Control Software]]

## Related Decisions

- [[FSM 400 Hz Bandwidth Requirement]]
- [[Piezoelectric vs Voice-Coil FSM Actuator]]
- [[Why Ritchey-Chretien over Schmidt-Cassegrain]]

## Tested By

- [[Fine Pointing Control Paper (Moll 2015)]]
