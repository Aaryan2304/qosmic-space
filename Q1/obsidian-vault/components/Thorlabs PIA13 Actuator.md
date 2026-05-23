---
type: component
name: Thorlabs PIA13 Actuator
vendor: Thorlabs
part_number: PIA13
cost_inr: 55000
lead_time_weeks: 6
datasheet_url: https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=10000&pn=PIA13
status: active
---

# Thorlabs PIA13 Actuator

## Specifications

| Parameter | Value |
|-----------|-------|
| Type | Piezoelectric inertia actuator |
| Travel | 13 mm |
| Mounting | 3/8" barrel |
| Step size | < 0.5 um |
| Max velocity | ~2 mm/s |
| Price (2025) | ~$650 USD (~Rs. 55,000) |

## Usage in System

The PIA13 is a piezoelectric screw actuator used for precision positioning of optical elements. In our ground station, it serves as the fine steering mirror actuator in the PAT system, providing the angular resolution and bandwidth needed for 10 urad pointing accuracy.

Note: The PIA13 is a representative component. The actual FSM for our system would be a custom piezoelectric tip-tilt mirror (similar to the design in Moll et al. 2015) rather than a stock Thorlabs actuator. The PIA13 illustrates the actuator class and cost range.

## Related Design Decisions

- [[FSM 400 Hz Bandwidth Requirement]]
- [[Piezoelectric vs Voice-Coil FSM Actuator]]

## Used By

- [[Pointing and Tracking System]]

## Substitutes

- Physik Instrumente (PI) S-330 series (higher performance, higher cost)
- Piezosystem jena custom FSM
