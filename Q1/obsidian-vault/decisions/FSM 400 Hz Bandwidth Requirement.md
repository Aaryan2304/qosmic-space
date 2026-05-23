---
type: decision
title: FSM 400 Hz Bandwidth Requirement
status: accepted
date: 2025-07-01
author: Aaryan
subsystem: [[Pointing and Tracking System]]
alternatives_considered:
  - 200 Hz bandwidth FSM
  - 400 Hz bandwidth FSM
  - 1 kHz bandwidth FSM
tradeoffs: Higher bandwidth means better disturbance rejection but requires more expensive actuators and faster control electronics. 400 Hz is the minimum to suppress gimbal vibration and atmospheric tip-tilt.
physics_rationale: The PAT system must suppress disturbances from gimbal mechanical resonance (typically 50-200 Hz) and atmospheric tip-tilt (power spectrum extends to ~100 Hz). A 400 Hz control bandwidth provides > 20 dB rejection at 100 Hz.
---

# FSM 400 Hz Bandwidth Requirement

## Context

Driven by REQ-002: Pointing Accuracy < 10 urad. The fine steering mirror must correct residual pointing errors faster than the disturbances from gimbal vibration and atmospheric turbulence.

## Alternatives Evaluated

### 200 Hz bandwidth
- **Pros:** Lower cost, simpler controller
- **Cons:** Insufficient rejection of gimbal vibration harmonics. Pointing error would exceed 10 urad during tracking.

### 400 Hz bandwidth
- **Pros:** Adequate rejection of all major disturbance sources. Moll et al. (2015) demonstrated this is achievable with piezoelectric actuators.
- **Cons:** Requires piezoelectric (not voice-coil) actuators. Control loop must run at 10+ kHz.

### 1 kHz bandwidth
- **Pros:** Margin for future higher-accuracy requirements
- **Cons:** Significantly more expensive. Diminishing returns since atmospheric tip-tilt power drops above 100 Hz.

## Decision

Selected 400 Hz. This is the minimum bandwidth that provides adequate disturbance rejection for 10 urad pointing. Moll et al. demonstrated a piezoelectric FSM exceeding 400 Hz with flexible hinge design.

## Derives From

- [[REQ-002: Pointing Accuracy < 10 urad]]

## Justified By

- [[Atmospheric Turbulence: Kolmogorov Model]]

## Implemented By

- [[Thorlabs PIA13 Actuator]]

## References

- [[Fine Pointing Control Paper (Moll 2015)]]
