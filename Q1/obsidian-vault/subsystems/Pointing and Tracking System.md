---
type: subsystem
name: Pointing and Tracking System
description: Acquires and maintains optical link with LEO satellites. Three-stage architecture -- coarse gimbal, fine steering mirror, and tracking sensors -- achieves sub-microradian pointing accuracy.
status: active
parent:
---

# Pointing and Tracking System

## Overview

The PAT system keeps a laser beam, only a few microradians wide, aimed precisely at a satellite moving at roughly 7.5 km/s across the sky. For a LEO satellite at 500 km altitude, the pass lasts approximately 7 minutes. During that entire window, the PAT system must acquire the satellite, close the tracking loop, and maintain lock despite disturbances from wind, mechanical vibration, and atmospheric refraction.

Three-stage architecture:

1. **Coarse pointing**: Azimuth-elevation gimbal slews the telescope toward the predicted satellite position. Accuracy ~1 milliradian. Speed up to 20 deg/s in azimuth.
2. **Fine steering mirror (FSM)**: A piezoelectric actuator corrects residual pointing errors in a closed loop. The FSM needs at least 400 Hz bandwidth to suppress tracking disturbances.
3. **Tracking sensor**: A quad-cell detector measures the satellite beacon position error and feeds it back to the FSM controller at kHz rates.

## Key Functions

- Coarse satellite acquisition using ephemeris-based pointing
- Fine tracking via closed-loop FSM control
- Beacon signal detection and error measurement

## Related Design Decisions

- [[FSM 400 Hz Bandwidth Requirement]]
- [[Piezoelectric vs Voice-Coil FSM Actuator]]

## Requirements Addressed

- [[REQ-002: Pointing Accuracy < 10 urad]]

## Dependencies

- Depends on: [[Telescope Assembly]]
- Depends on: [[Site Infrastructure]]
- Depends on: [[Control Software]]

## References

- [[Fine Pointing Control Paper (Moll 2015)]]
