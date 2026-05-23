---
type: physics
name: Coma Aberration in Optical Systems
domain: optics
description: A third-order optical aberration where off-axis point sources appear as comet-shaped blurs. RC telescopes eliminate coma using hyperbolic mirrors; SCTs do not.
key_equations: "Transverse coma = (3 theta) / (16 F^2)  where theta is field angle and F is focal ratio"
---

# Coma Aberration in Optical Systems

## Description

Coma affects telescopes when light enters at an angle to the optical axis. Instead of focusing to a point, an off-axis source focuses to a comet-shaped blur. The blur grows linearly with field angle and inversely with the square of the focal ratio.

A classical Cassegrain telescope has significant coma. The Schmidt-Cassegrain reduces it with a corrector plate but does not eliminate it. The Ritchey-Chretien uses two hyperbolic mirrors chosen to cancel third-order coma, providing a wide, sharp field of view.

## Key Equations

- Transverse coma: (3 * theta) / (16 * F^2)
- For f/8: angular coma ~ 0.13 arcmin per arcmin of field angle

## Relevance to QOSMIC

During satellite acquisition, the target may be several arcminutes off-axis before the tracking loop closes. Coma blur on the tracking sensor reduces SNR and slows acquisition. The RC design's coma-free field ensures sharp off-axis images, enabling faster acquisition. This was the primary reason for selecting RC over SCT.

## Related Decisions

- [[Why Ritchey-Chretien over Schmidt-Cassegrain]]
- [[Single-Mode vs Multi-Mode Fiber Coupling]]

## References

- [[Cailabs OGS Technical Reference]]
