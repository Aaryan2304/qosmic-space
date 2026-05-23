---
type: physics
name: Atmospheric Turbulence - Kolmogorov Model
domain: atmospheric
description: Statistical model describing how refractive index fluctuations in the atmosphere distort optical wavefronts. Characterized by the structure parameter Cn^2.
key_equations: "D_phi(r) = 6.88 (r/r_0)^(5/3);  r_0 = [0.423 k^2 sec(gamma) integral Cn^2(h) dh]^(-3/5)"
---

# Atmospheric Turbulence - Kolmogorov Model

## Description

When a laser beam travels through the atmosphere, it encounters random refractive index variations caused by temperature and humidity fluctuations. These distort the wavefront, causing the beam to spread, wander, and scintillate. The Kolmogorov model provides a statistical framework for describing these distortions.

The key parameter is Cn^2(h), the refractive index structure parameter as a function of altitude. Typical values range from 10^{-17} m^{-2/3} at high altitude to 10^{-13} m^{-2/3} near the surface.

The Fried parameter r_0 represents the effective aperture diameter over which wavefront distortion is ~1 radian RMS. For r_0 = 10 cm at 1550 nm, a 50 cm telescope is severely turbulence-limited and requires adaptive optics.

## Key Equations

- Phase structure function: D_phi(r) = 6.88 (r/r_0)^(5/3)
- Fried parameter: r_0 = [0.423 k^2 sec(gamma) integral Cn^2(h) dh]^(-3/5)
- Rytov variance: sigma_R^2 = 1.23 Cn^2 k^(7/6) L^(11/6)

## Relevance to QOSMIC

Atmospheric turbulence is the single largest factor degrading our link budget. It reduces fiber coupling efficiency, causes beam wander, and produces intensity scintillation. Typical nighttime Cn^2 at Challakere is ~10^{-15} m^{-2/3}, giving r_0 ~ 8-12 cm at 1550 nm.

## Related Decisions

- [[Adaptive Optics: Tip-Tilt vs Higher-Order Correction]]

## References

- [[Cailabs OGS Technical Reference]]
- [[Fine Pointing Control Paper (Moll 2015)]]
