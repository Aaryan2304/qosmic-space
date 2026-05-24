# Rejection Workflow

## 1. When a Part is Rejected

This workflow activates when any Critical check in the incoming inspection checklist fails.

### Workflow Steps

```
Inspection finds defect
        │
        ▼
Document the rejection in Airtable (Status → "Rejected")
        │
        ├──→ Minor defect (single dimension out, functional but not to spec)
        │       │
        │       ▼
        │   Document deviation → Conditional Accept (with CTO approval) → Update scorecard
        │
        └──→ Major defect (crack, wrong material, multiple dimensions out, optical damage)
                │
                ▼
            Photograph defect (minimum 3 angles, include reference scale)
                │
                ▼
            Move part to Quarantine area (physically labelled, segregated)
                │
                ▼
            Send rejection notification to vendor (Template D below)
                │
                ▼
            Wait for vendor response (target: 3 business days)
                │
                ├──→ Vendor agrees → Rework / Replacement / Refund (negotiated)
                │
                └──→ Vendor disputes → Escalate to CEO. Third-party inspection if needed.
```

### Documentation Required for Every Rejection
1. Photographs of the defect (3+ angles, scale reference)
2. Measured vs. specified values (dimensions, surface finish, or optical test results)
3. Inspection checklist with failing items clearly marked
4. The rejection email sent to vendor
5. Vendor's response (or note if no response in 5 business days)
6. Resolution: rework, replacement, refund, or partial accept

---

## 2. Rejection Email Template

### Template D: Rejection Notification

**Subject:** REJECTION NOTICE: QOSMIC-PO-2026-00XX — [Part Name]

Dear [Contact Name],

The shipment received under PO QOSMIC-PO-2026-00XX ([part name], quantity [X]) has been inspected and found non-conforming to the agreed specifications. We are formally rejecting the shipment.

**Rejection Details:**

| Parameter | Specified | Measured | Tolerance | Status |
|-----------|-----------|----------|-----------|--------|
| [Dimension A] | 50.00 mm | 50.47 mm | ±0.05 mm | FAIL |
| [Dimension B] | 25.4 mm | 25.38 mm | ±0.05 mm | FAIL |
| [Surface finish] | Ra 0.8 µm | Ra 2.1 µm | — | FAIL |

**Defect Description:**
[Bracket mounting boss is 0.47mm oversize, causing a 0.9mm interference fit with the mating SM1-threaded tube. Additionally, the optical mounting face has a measured roughness of Ra 2.1 µm against the specified Ra 0.8 µm.]

**Documentation Attached:**
- Photographs showing the defects (3 views, with scale reference)
- Inspection report with measured values
- Comparison to the approved drawing (QOSMIC-OPT-BRACKET-2026-RevA.pdf)

**Requested Resolution:**
We will accept either of the following within [X] business days:

1. **Rework** — the vendor corrects the non-conforming dimensions at their facility and ships back within [timeframe].
2. **Replacement** — a new batch manufactured to the correct spec, shipped at the vendor's cost, with expedited delivery.
3. **Full refund** — including all shipping and customs costs incurred.

Please confirm your preferred resolution by [date — 3 business days from date of email]. If we do not receive a response by then, we will initiate a refund claim and pursue an alternative vendor for the balance of our requirement.

Regards,

[Name]
QOSMIC SPACE

**Attachments:**
- Photographs (3)
- Inspection report PDF
- Annotated drawing with measured vs. specified callouts

---

## 3. Resolution Options

| Resolution | When to Accept | When to Reject |
|------------|---------------|----------------|
| **Rework** | Defect is dimensional-only and reworkable (e.g., drill a hole to correct size, re-surface a mounting face). Only accept if: (a) the rework leaves no residual stress or distortion, (b) the vendor certifies the reworked part meets all original specs, (c) timeline is acceptable. | Do not accept rework on: coated optical surfaces (recoating is a full remake), heat-treated parts (rework can alter temper), or any part where material removal changes the geometry beyond the original tolerances. |
| **Replacement** | Generally preferred. Vendor manufactures new parts to spec. Request expedited shipping at vendor's cost. | Accept unless the vendor has shown a pattern of repeated failures (2+ rejections on similar parts). At that point, consider moving to a new vendor. |
| **Refund** | Accept when: the part is not reworkable, the vendor cannot meet the timeline, or this is the vendor's third rejection in 12 months. Partial refund may be acceptable for partial usable shipments. | Do not accept refund-only if you need the parts urgently — you're now back at square one with no parts and lost time. |

### Financial Impact of Rejection
- **Cost of rejection:** the value of the part + any customs duty paid + shipping both ways for the replacement
- **Cost of delay:** the value of the downstream work that cannot proceed without this part
- **Decision rule:** If the cost of delay > the cost of the replacement, accept a faster resolution (e.g., air freight a replacement) even if it costs more than the part itself.

---

## 4. Partial Shipment Policy

### When Partial Shipments Occur
- Vendor ships what's ready and backorders the rest
- One line item of a multi-line PO is delayed
- Part of a batch fails inspection, the rest passes

### Policy
1. **Partial shipments are allowed** for POs with multiple line items or quantities > 10.
2. Each partial shipment gets its own receiving record and inspection.
3. The PO remains open until all line items are inspected and accepted.
4. Backordered items are tracked as a line-level promise date in the PO record.

### Partial Acceptance
If only some units in a batch fail inspection:
- Accepted units: process normally (move to stock)
- Rejected units: follow the rejection workflow above
- The vendor must resolve the rejected units. The accepted units are paid for per the PO terms.

### Partial Rejection (Partial Acceptance of a Mixed Lot)
If a shipment has a mix of conforming and non-conforming parts:
- Accept the conforming parts. Issue a receiving report showing accepted quantity.
- Reject the non-conforming parts. Initiate rejection workflow for those units only.
- The PO balance adjusts: vendor is paid for accepted quantity, and must replace or refund the rejected quantity.

### Example
PO for 10 custom brackets. 8 pass inspection, 2 fail on thread tolerance.
- 8 brackets are accepted and moved to stock.
- Vendor is notified of rejection on 2 units with measurements and photos.
- Vendor ships 2 replacement brackets. Those are inspected on arrival against the same checklist.
- If the 2 replacements pass, the PO is closed. If they fail, initiate full PO review.

### Accounting Note
Partial acceptances should be recorded in the vendor scorecard at the acceptance rate level (not by dollar value) — an 80% unit acceptance rate is a clearer signal than an 80% dollar acceptance rate, since expensive single parts can mask systemic quality issues.
