---
type: physics
name: LEO Satellite Orbital Mechanics
domain: orbital
description: Describes LEO satellite motion and how ground stations predict and track passes. Uses SGP4 orbit propagation with TLE data.
key_equations: "T = 2pi sqrt(a^3 / mu_E);  v = sqrt(mu_E / a);  T_pass ~ 2(R_E + h)/v_sat * sin(el_min)"
---

# LEO Satellite Orbital Mechanics

## Description

LEO satellites orbit at 200-2000 km altitude. At 500 km, orbital period is ~94 minutes and velocity is ~7.5 km/s. From a ground station, the satellite sweeps across the sky, visible for ~10-12 minutes, with ~7 minutes above 20 degrees elevation.

The station predicts passes using Two-Line Element (TLE) data and SGP4 propagation. TLEs contain orbital elements at a specific epoch. SGP4 accounts for Earth oblateness (J2) and atmospheric drag. Accuracy: 1-3 km over 24 hours.

## Key Equations

- Orbital period: T = 2pi sqrt(a^3 / mu_E), mu_E = 3.986e14 m^3/s^2
- Orbital velocity: v = sqrt(mu_E / a)
- Max pass duration: T_pass ~ 2(R_E + h)/v_sat * sin(el_min)

For 500 km altitude at 10 deg minimum elevation: T_pass ~ 7 minutes.

## Relevance to QOSMIC

SGP4 pass predictions drive the observation schedule: when to open the dome, slew the telescope, start tracking, and expect signal. TLE accuracy is sufficient for initial acquisition; the fine tracking loop takes over once the beacon is detected.

## Related Decisions

- [[FSM 400 Hz Bandwidth Requirement]]

## References

- [[Fine Pointing Control Paper (Moll 2015)]]
- [[Control Software]]
