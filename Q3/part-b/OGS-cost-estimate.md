# Part B: Optical Ground Station Cost Estimate

## Context
Cost to build a single 50cm-class ground station with tracking mount, adaptive optics, and fiber coupling. The brief asks for estimates within 2x of reality.

**Reference point:** A peer-reviewed paper states "in Europe, the cost estimation for an OGS is approximately $2 million per station, with a range of $1–5 million for LEO-to-ground link stations" (arXiv:2410.23470v2, Aug 2025).

QOSMIC's build in India should be at the lower end of this range due to lower labour and construction costs, but component costs (optics, AO) are globally priced.

---

## Bill of Materials Breakdown

| Line Item | Description | Low Estimate | High Estimate | Notes |
|-----------|-------------|-------------|--------------|-------|
| **1. Telescope** | 50cm aperture, observatory-grade, Cassegrain or Ritchey-Chretien, with primary mirror coatings | $150,000 | $350,000 | PlaneWave CDK 500 or similar. For an OGS, you need a telescope that can track fast-moving LEO objects, not just stare at stars. Observatory-grade mounts cost more than astronomy hobbyist ones. |
| **2. Tracking Mount** | Alt-azimuth, arcsecond tracking accuracy, with encoder feedback | $80,000 | $180,000 | ASTELCO (same as KSAT uses) or ASA. Must track LEO satellites at angular rates up to 1°/sec. Sub-5 arcsecond tracking error required. |
| **3. Adaptive Optics System** | Deformable mirror, wavefront sensor, real-time control computer | $200,000 | $500,000 | ALPAO, BMC, or GA-Synopta. DM with 100+ actuators. WFS running at 1+ kHz. For 50cm aperture seeing correction at 1550nm. This is the most expensive single component and the hardest to estimate without a specific vendor quote. |
| **4. Fiber Coupling Optics** | Free-space to fiber coupler, polarization optics, beam steering | $50,000 | $120,000 | Thorlabs, Oz Optics, or custom. Must couple 1550nm free-space beam into single-mode fiber with <1dB loss. Requires precision alignment mechanics. |
| **5. Detector / Modem** | Photodetector + modem for at least 3 Gbps | $100,000 | $200,000 | Work Microwave (KSAT uses theirs for 3 Gbps). Alternatively, a custom solution. Modems for optical communications are not COTS — they're specialised. |
| **6. Control Electronics** | Servers, networking, power supplies, UPS | $40,000 | $80,000 | Industrial PCs for AO control, tracking control, network interface. Redundant power. |
| **7. Software** | Tracking, AO control, scheduling, monitoring | $80,000 | $150,000 | Custom or adapted from astronomical observatory software. Must interface with satellite TLE data, predict passes, acquire target, close tracking loop, manage data flow. |
| **8. Site Preparation** | Concrete pad, weather enclosure, fibre internet, power installation | $50,000 | $120,000 | Depends heavily on site. Greenfield: more. Rooftop at existing facility: less. Fibre internet connection to a local data centre is a recurring cost buried here. |
| **9. Shipping, Customs, Insurance** | International shipping of precision optics, import duties into India | $40,000 | $80,000 | Optical components require special handling. Customs duties at ~27-31% for optical instruments (HS 9013/9002). |
| **10. Installation & Commissioning** | On-site assembly, alignment, calibration, testing | $40,000 | $80,000 | 2-3 weeks on site with a specialist team. Includes proving tracking accuracy and link closure with a test satellite or airborne target. |
| **11. Contingency (15%)** | Unforeseen costs | $120,000 | $250,000 | 15% on subtotal. |

---

## Total Cost Range

| | Low Case | High Case |
|---|----------|-----------|
| Component total (items 1-10) | $830,000 | $1,860,000 |
| Contingency (15%) | $124,500 | $279,000 |
| **Grand total** | **$954,500** | **$2,139,000** |

**Rounded: $1.0M – $2.1M per station.**

## How This Compares

| Source | Estimate | Variance from QOSMIC |
|--------|----------|---------------------|
| arXiv:2410.23470v2 (Europe) | ~$2M ($1-5M range) | Within range ✓ |
| KSAT's half-meter (Greece) | Not disclosed, but KSAT states "comparable to RF" | An RF ground station antenna of equivalent capability costs ~$500K-1M installed |
| Cailabs Tilba-L10 (commercial) | Not disclosed, but they are scaling to 50/yr — implies target cost <$500K per unit at volume | At volume, a single station would be cheaper than first-of-a-kind |

**Key caveat:** This is a first-unit estimate. The first station always costs more than subsequent ones (non-recurring engineering, tooling, lessons learned). At a production run of 10 units, per-unit cost drops by an estimated 20-30%.

## India-Specific Adjustments

| Factor | Impact on Cost |
|--------|---------------|
| Labour cost (installation, site prep) | 40-60% lower than European equivalent |
| Import duties on optics (HS 9013, 9002) | +27-31% on imported components (BCD + SWS + IGST) |
| Fibre internet in metro areas (Bengaluru, Hyderabad) | Comparable to global prices (~$500-1000/month for business-grade symmetric 1Gbps) |
| Fibre in remote locations (Ladakh, Rajasthan) | Can be 5-10x more expensive or require satellite backhaul |
| Real estate / lease cost | Significantly lower than European equivalents |

**Net effect:** Building in India costs about the same as Europe for the hardware (globally priced components + duties), but 40-60% less for site preparation and installation. The total range of $1.0-2.1M reflects this.

## Could It Be Cheaper?

Yes, if:
- Using a smaller aperture (30-40cm) for LEO-only — reduces telescope cost 40-50%
- Forgoing adaptive optics and relying on tip-tilt only — reduces AO cost 60-70% but limits performance
- Building multiple stations (bulk purchase discount on optics, shared engineering)
- Using a simpler modem (lower data rate target)

The $1.0-2.1M range assumes a fully capable station for LEO-to-ground at 3+ Gbps, with AO. A minimal "good enough" station could be built for $500-700K. The PDF asks for 50cm-class with AO and fiber coupling — that's the specification we've costed.
