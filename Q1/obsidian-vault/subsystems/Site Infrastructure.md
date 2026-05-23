---
type: subsystem
name: Site Infrastructure
description: Physical infrastructure supporting the ground station. Includes observatory enclosure, power systems, fiber backhaul, and environmental monitoring. Site selection driven by atmospheric conditions and cloud cover.
status: active
parent:
---

# Site Infrastructure

## Overview

A ground station is only as good as its site. The two most important selection criteria are atmospheric conditions (cloud cover, seeing, aerosol loading) and fiber backhaul connectivity.

Our primary site is at Challakere, Karnataka (14.32 deg N, 76.65 deg E, ~600 m elevation). This location was selected after evaluating cloud cover statistics from INSAT-3D imagery and atmospheric turbulence measurements from the IISc atmospheric observatory at the same site.

## Key Functions

- Observatory enclosure with retractable dome
- Uninterruptible power supply and backup generator
- Fiber backhaul connectivity (minimum 10 Gbps to nearest PoP)
- Environmental monitoring (weather station, cloud sensor, seeing monitor)

## Site Parameters (Challakere)

| Parameter | Value |
|-----------|-------|
| Latitude | 14.32 deg N |
| Longitude | 76.65 deg E |
| Elevation | ~600 m ASL |
| Mean annual cloud cover | ~55% (monsoon peaks at ~85%) |
| Clear nights per year | ~120 |
| Median seeing | ~1.5 arcsec (at 500 nm) |

## Requirements Addressed

- [[REQ-001: 1 Gbps Downlink Rate]]

## References

- [[Atmospheric Turbulence: Kolmogorov Model]]
- [[LEO Satellite Orbital Mechanics]]
