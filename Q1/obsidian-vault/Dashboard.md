# QOSMIC Knowledge Graph Dashboard

## Overview

This is the entry point for the QOSMIC organizational knowledge graph. Use this dashboard to navigate the vault and understand the current state of the system design.

## Quick Stats

| Category | Count |
|----------|-------|
| Subsystems | 7 |
| Design Decisions | 5 |
| Physics Concepts | 4 |
| Components | 2 |
| Requirements | 2 |
| References | 2 |
| **Total Notes** | **22** |

## Subsystems

- [[Telescope Assembly]]
- [[Pointing and Tracking System]]
- [[Adaptive Optics System]]
- [[Fiber Coupling Module]]
- [[Receiver Electronics]]
- [[Control Software]]
- [[Site Infrastructure]]

## Design Decisions

- [[Why Ritchey-Chretien over Schmidt-Cassegrain]]
- [[FSM 400 Hz Bandwidth Requirement]]
- [[Piezoelectric vs Voice-Coil FSM Actuator]]
- [[Adaptive Optics: Tip-Tilt vs Higher-Order Correction]]
- [[Single-Mode vs Multi-Mode Fiber Coupling]]

## Physics Concepts

- [[Atmospheric Turbulence: Kolmogorov Model]]
- [[Coma Aberration in Optical Systems]]
- [[BB84 Decoy-State Protocol]]
- [[LEO Satellite Orbital Mechanics]]

## Requirements

- [[REQ-001: 1 Gbps Downlink Rate]]
- [[REQ-002: Pointing Accuracy < 10 urad]]

## Components

- [[Thorlabs PIA13 Actuator]]
- [[InGaAs Single-Photon Detector Module]]

## Key References

- [[Fine Pointing Control Paper (Moll 2015)]]
- [[Cailabs OGS Technical Reference]]

## Onboarding Paths

### New engineer assigned to Telescope Subsystem
1. Start with [[Telescope Assembly]] subsystem overview
2. Read [[Coma Aberration in Optical Systems]] for the physics background
3. Read [[Why Ritchey-Chretien over Schmidt-Cassegrain]] for the key design decision
4. Review [[REQ-002: Pointing Accuracy < 10 urad]] for driving requirements

### New engineer assigned to Tracking Subsystem
1. Start with [[Pointing and Tracking System]] subsystem overview
2. Read [[LEO Satellite Orbital Mechanics]] for orbital mechanics background
3. Read [[FSM 400 Hz Bandwidth Requirement]] and [[Piezoelectric vs Voice-Coil FSM Actuator]]
4. Read [[Atmospheric Turbulence: Kolmogorov Model]] for disturbance environment
5. Review [[Fine Pointing Control Paper (Moll 2015)]]
