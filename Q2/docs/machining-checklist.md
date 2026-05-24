# Custom-Machined Parts: Pre-Submission Checklist

## Why This Exists
When an engineer submits a request for a custom-machined part, common specification errors waste weeks: missing tolerances, incompatible materials, undefined surface finishes. This checklist catches those errors before the request reaches a vendor. The person filling the request must check every item before submission.

## Checklist

### Drawing Requirements
| # | Check | Pass/Fail | Notes |
|---|-------|-----------|-------|
| 1 | Drawing file is attached AND viewable (PDF or DXF/STEP) | | No photo of a hand-drawn sketch — must be a dimensioned CAD drawing |
| 2 | Drawing is fully dimensioned (length, width, height, hole diameters, thread specs) | | Check every feature has at least one dimension callout |
| 3 | All critical dimensions have tolerance callouts | | Bilateral (±0.1mm), unilateral (+0.05/-0), or Geometric Dimensioning & Tolerancing (GD&T) |
| 4 | Thread callouts are complete (size × pitch × depth) | | E.g., M6×1.0 - 6H, 12mm depth. Incomplete thread specs are the #1 rework cause |
| 5 | Drawing has a revision letter/number and a title block | | Rev A, Rev B, etc. Title block must list: part name, material, scale, units, drawn by, date |
| 6 | Units are explicitly stated (mm or inches) | | A missing unit spec at 18L/month burn is a ₹5K-50K mistake |

### Material Requirements
| # | Check | Pass/Fail | Notes |
|---|-------|-----------|-------|
| 7 | Material spec includes alloy/grade | | Not "aluminium" — must be 6061-T6, 7075-T6, 6082, stainless 304/316, etc. |
| 8 | Material temper/heat treatment is specified (if applicable) | | E.g., T6 temper for 6061, solution-treated and aged. If not needed, state "No HT required" |
| 9 | Surface treatment specified (if applicable) | | Clear anodise (MIL-A-8625 Type II), hard anodise, black oxide, nickel plate, none |
| 10 | Material spec is consistent between drawing title block and request form | | Mismatched specs between form and drawing cause vendor confusion |

### Tolerance & Fit Requirements
| # | Check | Pass/Fail | Notes |
|---|-------|-----------|-------|
| 11 | Mating features (holes, shafts, locating pins) have explicit tolerance classes | | If this part bolts to something else, the fit (clearance, transition, interference) must be stated |
| 12 | Surface finish (Ra or equivalent) specified on functional surfaces | | Optical mounting surfaces typically require Ra ≤ 0.8 µm. Non-functional surfaces can be Ra 3.2 µm |
| 13 | Edge break / chamfer specified | | "Break sharp edges 0.2mm max" is standard. If a specific chamfer is needed, dimension it |
| 14 | Flatness / parallelism specified if the part mounts to an optical breadboard or other part | | A bracket that isn't flat will misalign an optical path — this is a common failure |

### Practical Checks
| # | Check | Pass/Fail | Notes |
|---|-------|-----------|-------|
| 15 | Is the part manufacturable? Check: internal corners have relief radii matching available tool sizes | | A square internal corner cannot be machined with a round endmill. Standard corner radii: 1mm, 2mm, 3mm minimum |
| 16 | Wall thickness is at least 1mm (aluminium) or 0.5mm (steel) for standard machining | | Thinner walls risk chatter during machining and breakage during handling |
| 17 | Hole depths do not exceed 4× diameter for standard drills | | Deep holes need specialised tooling. If deeper, flag as "deep hole drilling required" |
| 18 | Thread depth does not exceed 2.5× thread diameter for tapped holes in aluminium | | Taps break in deep blind holes. Consider thread inserts (Helicoil) for critical threads in aluminium |
| 19 | Has this part been prototyped? If yes, have any issues been noted from the prototype run? | | Capture lessons from prototype before ordering production batch |

### Vendor-Specific Flags
| # | Check | Pass/Fail | Notes |
|---|-------|-----------|-------|
| 20 | If the part has tight tolerances (±0.02mm or tighter), verify the vendor has CNC capabilities rated for this | | Not all Chinese prototyping shops hold ±0.02mm. For precision, specify a European vendor |
| 21 | If the part will be used in a vacuum environment (optical path), note any outgassing concerns with material/surface treatment | | Standard anodising is fine. No cadmium plating, no zinc plating in vacuum |

## Submission Gate
The checklist is embedded in the Airtable request form. If any item in sections "Drawing Requirements" or "Material Requirements" is unchecked or marked Fail, the form rejects submission with a message:
> "Cannot submit: drawing or material specification is incomplete. Review items [X, Y, Z] before resubmitting."

Items in "Practical Checks" and "Vendor-Specific Flags" produce warnings but do not block submission — they flag the issue for the CTO during approval review.
