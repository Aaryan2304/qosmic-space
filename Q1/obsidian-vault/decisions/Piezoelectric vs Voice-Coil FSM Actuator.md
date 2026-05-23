---
type: decision
title: Piezoelectric vs Voice-Coil FSM Actuator
status: accepted
date: 2025-07-10
author: Aaryan
subsystem: [[Pointing and Tracking System]]
alternatives_considered:
  - Voice-coil actuator
  - Piezoelectric actuator
tradeoffs: Piezoelectric offers higher bandwidth and resolution but smaller range and requires high-voltage drive. Voice-coil offers larger range but lower bandwidth and is sensitive to magnetic fields.
physics_rationale: Piezoelectric actuators achieve bandwidths of 400+ Hz with sub-microradian resolution. Voice-coil actuators are limited to ~200 Hz by coil inductance and are susceptible to magnetic interference from the gimbal motors.
---

# Piezoelectric vs Voice-Coil FSM Actuator

## Context

The FSM 400 Hz bandwidth requirement eliminates voice-coil actuators as a viable option. This decision confirms piezoelectric as the actuator technology.

## Alternatives Evaluated

### Voice-coil
- **Pros:** Large actuation range (+/- 5 mrad), simple drive electronics, no high voltage
- **Cons:** Bandwidth limited to ~200 Hz by coil inductance. Sensitive to magnetic interference from gimbal motors. Lower resolution.

### Piezoelectric
- **Pros:** Bandwidth exceeding 400 Hz, sub-microradian resolution, immune to magnetic fields
- **Cons:** Smaller range (+/- 2.5 mrad), requires high-voltage drive (0-150 V), hysteresis requires closed-loop control

## Decision

Selected piezoelectric. The 400 Hz bandwidth requirement is the deciding factor. Voice-coil actuators cannot meet this due to fundamental inductance limitations.

## Trade-offs

| Criterion | Piezo (Chosen) | Voice-coil (Rejected) |
|-----------|----------------|----------------------|
| Bandwidth | 400+ Hz | ~200 Hz max |
| Range | +/- 2.5 mrad | +/- 5 mrad |
| Resolution | Sub-urad | ~1 urad |
| Drive voltage | 0-150 V | 0-24 V |
| Magnetic immunity | Yes | No |

## Derives From

- [[REQ-002: Pointing Accuracy < 10 urad]]
- [[FSM 400 Hz Bandwidth Requirement]]

## Implemented By

- [[Thorlabs PIA13 Actuator]]

## References

- [[Fine Pointing Control Paper (Moll 2015)]]
