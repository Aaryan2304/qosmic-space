# Incoming Inspection Checklists

## 1. Custom-Machined Parts Inspection Checklist

Every incoming custom-machined part must go through this checklist before acceptance. If any item in the Critical section fails, the part is rejected outright. Items in the Warning section allow conditional acceptance with documented deviation.

### Critical (Mandatory Pass)
| # | Check | Method | Pass/Fail | Notes |
|---|-------|--------|-----------|-------|
| 1 | Quantity matches PO | Count by hand | | Record actual vs. ordered |
| 2 | Visual inspection: no major defects | Visual — naked eye under good lighting | | Deep scratches, cracks, dents, burrs, discolouration |
| 3 | Dimensional check: mounting surfaces | Calliper / micrometre against drawing | | Measure at 3 points per dimension, record min/max |
| 4 | Dimensional check: critical hole positions | Pin gauge or calliper | | Relative to drawing datums |
| 5 | Thread gauge check | Go/No-Go gauge | | M6, M4, M3, etc. — verify each threaded hole |
| 6 | Surface finish on optical mounting faces | Surface roughness comparator or profilometer | | Ra target per drawing (±20% tolerance) |
| 7 | Material certification provided | Check cert against PO spec | | Cert must state alloy/grade, temper, batch number |

### Warning (Document if Failed)
| # | Check | Method | Notes |
|---|-------|--------|-------|
| 8 | Edge break / chamfer dimensions | Visual + calliper | If missing but functional, document and accept |
| 9 | Colour/anodise consistency | Visual comparison to reference | Batch variation is expected. Flag if dramatically different |
| 10 | Surface finish on non-functional surfaces | Visual + roughness comparator | If higher Ra than spec but outside optical path, may accept |
| 11 | Burr check on tapped holes | Visual + finger test | Small burrs can be removed with a hand chamfer tool |
| 12 | Packaging adequacy | Visual | Should prevent abrasion between parts. If poor, photograph and feedback to vendor |

### Inspection Result Flow
- **All Critical pass:** Part is Accepted. Move to stock.
- **Any Critical fail:** Part is Rejected. Initiate rejection workflow (rejection-workflow.md).
- **Critical pass but Warning fail(s):** Conditional Accept with documented deviation. Flag in vendor scorecard.

---

## 2. Precision Optical Components Inspection Checklist

Optical components require different inspection methods than machined parts. The key parameters that matter for QOSMIC's application (1064 nm free-space optical links, Cassegrain telescope, fiber coupling) are described below with their practical significance.

### Why These Parameters Matter

| Parameter | Why It Matters to QOSMIC | What Happens If Off-Spec |
|-----------|--------------------------|-------------------------|
| **Surface quality (scratch-dig)** | Scratches scatter 1064 nm light into the detector path, increasing noise. In high-power paths, scratches become damage initiation sites. | Reduced SNR in optical link. Risk of catastrophic mirror damage at >5W. |
| **Surface figure / wavefront error (WFE)** | Determines how well the wavefront is preserved through the optical train. A λ/10 mirror introduces 0.1 waves of aberration. Stack 10 such surfaces and you have 1 wave of total WFE — enough to degrade fiber coupling efficiency from 80% to under 30%. | Directly reduces coupled power into single-mode fiber. |
| **Coating reflectivity/transmission** | For HR (high-reflector) mirrors: 99.8% reflectivity means 0.2% loss per surface. With 15 mirrors in the path, that's 3% total loss. If actual reflectivity is 99.0%, loss jumps to 14%. | Wasted laser power. Thermal load on mounts. |
| **Clear aperture** | The usable optical area. A mirror with 90% clear aperture means the outer 5% annulus is unusable. If your beam footprint exceeds this, you clip the beam — creating diffraction. | Diffraction rings, reduced Strehl ratio, lower coupling. |
| **Centration (for lenses)** | A decentred lens introduces coma and astigmatism. For a beam expander, even 0.1mm decentration can misalign the output beam by several milliradians. | Misaligned downlink path. Lost pointing accuracy. |

### Inspection Checklist

| # | Check | Method | Acceptable Threshold | Notes |
|---|-------|--------|---------------------|-------|
| 1 | Visual surface inspection | Bright light against dark background | No visible scratches > 0.01mm width on clear aperture | Use MIL-PRF-13830B comparator if available |
| 2 | Scratch-dig verification | Darkfield illumination (40W incandescent or 15W fluorescent), compare to standard | 20-10 for precision optics, 40-20 for general use | Per MIL-PRF-13830B. Precision laser path: 20-10. Fold mirrors: 40-20. |
| 3 | Surface figure (WFE) test | Interferometer (Zygo or similar) | ≤ λ/10 at 632.8nm for precision optics, ≤ λ/4 for general use | Must be measured. Do not accept without a WFE test report from vendor. |
| 4 | Coating reflectivity (HR mirrors) | Spectrophotometer at 1064nm | ≥ 99.5% (preferred ≥ 99.8%) at design angle | Request coating run data from vendor. Spot-check with handheld power meter + reference mirror if available. |
| 5 | Coating transmission (AR optics) | Spectrophotometer at 1064nm | ≥ 99.0% (R < 1% per surface) | For anti-reflection coated windows and lenses |
| 6 | Clear aperture verification | Compare physical diameter to spec | ≥ 90% of physical diameter as specified | Measure physical diameter with calliper, verify clear aperture mark or assume central 90% |
| 7 | Centration (lenses) | Centration fixture or air gauge | ≤ 0.05mm (3 arcmin for most applications) | Critical for beam expander and collimator lenses |
| 8 | Coating adhesion (tape test) | Apply scotch tape, peel at 90° | No coating removal | Per MIL-C-48497. Sample test on first article only. |
| 9 | Marking/packaging | Visual | Each optic individually wrapped in lens tissue, in padded case. Part number and coating batch on label. | DO NOT touch optical surfaces with bare hands — inspect while wearing powder-free nitrile gloves |
| 10 | Certificate of compliance | Document check | C of C must state: part number, coating type, reflectivity/transmission measured value, date, inspector | Keep in PO record |

### Equipment Needed for Incoming Optical QC
| Tool | Cost Estimate | What It Measures | Minimum Requirement? |
|------|--------------|-----------------|---------------------|
| Scratch-dig paddle | $165 (Edmund Optics, stock #91-291) | Surface quality visual comparison to MIL-PRF-13830B | Yes for long-term QC |
| Handheld spectrophotometer (1064nm) | $2,000-5,000 | Coating reflectivity at specific wavelength | Desirable but not initial |
| Interferometer (Zygo) | $15,000-50,000 (used) | Wavefront error | Not needed — rely on vendor C of C for now |
| Calliper (digital, 0.01mm resolution) | $20-100 | Physical dimensions, clear aperture | Yes |
| Magnifying loupe (10×) | $15-30 | Scratch-detailed visual | Yes |

**Practical reality for a seed-stage startup:** QOSMIC will not own an interferometer or spectrophotometer at this stage. The inspection relies on:
- Vendor-supplied test reports (WFE, reflectivity) — require these as a contractual deliverable on every PO
- Visual inspection for scratch-dig ($165 scratch-dig paddle from Edmund Optics)
- Dimensional checks (calliper)
- Tape test for coating adhesion (zero cost)

If a precision optic is critical (eg. the primary mirror of the telescope), a one-time measurement at a local optics lab (IISc, ARCI Chennai) costs ₹5,000-15,000 per measurement and is worth it for the first article.

### Optical Inspection Reference Table

| Optical Component | Critical QC Parameters | Standard Spec |
|-------------------|----------------------|---------------|
| Flat mirrors (fold mirrors, dichroics) | Surface figure (λ/10 @ 633nm), Scratch-dig (20-10), Coating R > 99.5% @ 1064nm | λ/10, 20-10, R>99.5% |
| Curved mirrors (off-axis parabolas, spherical) | Surface figure (λ/8), Scratch-dig (20-10), Coating R > 98% | λ/8, 20-10, R>98% |
| Lenses (collimators, beam expanders) | WFE transmitted (λ/4), Centration (<3 arcmin), AR coating T > 99% @ 1064nm | λ/4, 3 arcmin, T>99% |
| Windows (vacuum, protective) | Surface figure (λ/4), Scratch-dig (40-20), AR coating R < 0.5% per surface | λ/4, 40-20, R<0.5% |
| Waveplates / polarisers | Retardance accuracy (λ/100), AR coating both sides | λ/100, R<0.5% |
| Optical fibers (patch cables, pigtails) | Connector polish (APC vs PC), insertion loss (<0.5dB), return loss (>50dB) | APC, <0.5dB, >50dB |

### First-Article Inspection for Custom Optics
For the first piece of any new custom optical component:
1. Request the vendor's full test data package (WFE interferogram, coating curve, surface quality report)
2. If budget allows: independent verification at a local optics lab
3. Retain the first-article test report in the PO record
4. Subsequent pieces from the same production run only need a certificate of compliance with lot-level test data
