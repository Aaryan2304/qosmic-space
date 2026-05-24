# RFQ Process, Templates, and Fast-Track Path

## 1. RFQ Process: Vendor Solicitation Guidelines

### How many vendors to solicit

| Part Type | Min Vendors | Max Vendors | Rationale |
|-----------|-------------|-------------|-----------|
| Catalog component (Thorlabs, Edmund, Newport) | 1 | 2 | Pricing is published. One PO confirms stock and delivery. Second vendor only if lead time concerns. |
| Custom-machined part (bracket, mount, housing) | 3 | 5 | Machining is competitive. 3 quotes gives you a price floor and a ceiling. More than 5 wastes time — diminishing returns on price variation past 5. |
| Precision custom optics (lens, mirror, window) | 2 | 3 | Fewer qualified vendors exist. Solicit 2-3 specialists and compare capability statements alongside pricing. |
| Electronics / PCBA | 2 | 3 | Prototype runs: JLCPCB + one local assembler. Production: get a third quote. |
| Assembly (full system integration) | 1 | 2 | Normally single-sourced to the design vendor. A second quote only if the first is uncompetitive. |

### RFQ Process Flow
1. Requester confirms drawing(s) and spec sheet are final (see machining-checklist.md).
2. Procurement identifies candidate vendors from the vendor database, filtering by capability and country.
3. For new vendors: run initial qualification check — request a sample part or reference list before sending the full RFQ.
4. Send RFQ email (Template A) to all candidates on the same day.
5. Set response deadline: **7 business days** for custom parts, **3 business days** for catalog.
6. If no response in 5 business days, send follow-up (Template B).
7. On receipt of all quotes: compile into comparison matrix (Airtable table with columns: vendor, unit price, lead time, shipping cost, payment terms, exclusions).
8. If lowest quote is >30% above budget: enter negotiation (Template C).
9. Award to lowest compliant bidder. "Compliant" means meets all spec requirements — not just lowest price.
10. Update vendor database with interaction and quote data.

---

## 2. Fast-Track Path for Catalog Components

### When to Use
Catalog components are off-the-shelf items with published part numbers, specs, and prices. Most QOSMIC catalog buys are from **Thorlabs, Edmund Optics, Newport, McMaster-Carr**, and **Mouser/Digikey**.

Fast-track applies when:
- The part has a published part number (e.g., Thorlabs SM1CP2 — SM1 end cap)
- The requesting engineer specifies the exact part number
- The unit price is within 20% of the last PO for the same part (if a reorder)
- The lead time is standard (does not require expedited handling)

### Fast-Track Procedure
1. Engineer submits request form with "Catalog" as part type and the vendor part number.
2. No RFQ needed — procurement goes directly to PO creation.
3. Procurement verifies pricing against vendor website (updated if >90 days since last buy).
4. PO issued within 1 business day of request approval.
5. Tracking auto-populated from the single-source Airtable view.

### When Not to Use
- If the part requires any customization or modification — falls back to full RFQ.
- If the order value exceeds ₹50,000 — CEO still needs to approve even if it's catalog.
- If this is the first buy from a new catalog vendor — a test PO of <₹5,000 is fine, but larger values should go through a brief capability check.

### Preset Vendor List (Airtable)
The catalog vendor list in Airtable stores:
- Vendor name and customer account number
- Preferred shipping method (UPS for Thorlabs, FedEx for Edmund, DHL for Mouser)
- Customer-specific discount (Thorlabs educational discount if applicable)
- Payment method on file
- Shipping address template

---

## 3. Vendor Communication Templates

### Template A: Initial RFQ — Custom-Machined Aluminum Optical Mount

**Subject:** RFQ: Custom Aluminum Optical Mount — QOSMIC-OPT-2026-0012

Dear [Contact Name],

QOSMIC SPACE is sourcing a custom aluminum optical mount for our optical ground station prototype. We are requesting a quotation for the following:

**Part Description:**
Custom kinematic optical mount, 1-inch (25.4mm) optic capacity, intended for 90-degree beam folding in a 1064nm free-space optical path.

**Material:** 6061-T6 aluminum, clear anodised per MIL-A-8625 Type II, Class 2.

**Quantity:** 5 pieces initially, with potential for 25-50 pieces in production Q1 2026.

**Key Tolerances:**
- Mounting surface flatness: ≤ 0.05 mm over 50 mm
- Threaded hole positions: ±0.1 mm from drawing datum
- Optic-axis alignment features: ±0.05 mm
- Surface finish on optical mounting face: Ra ≤ 0.8 µm
- Non-functional surfaces: Ra ≤ 3.2 µm

**Drawing Reference:** QOSMIC-OPT-BRACKET-2026-RevA.pdf (attached)
**3D Model:** QOSMIC-OPT-BRACKET-2026-RevA.step (available on request)

**Delivery Requirement:** First article within 4 weeks of PO, balance within 6 weeks.

**Shipping Terms:** FCA your facility (we arrange and pay freight from your door to Bengaluru, India).

**Payment Terms:** Please propose — we typically accept net 30 for first orders.

**Please include in your quote:**
- Unit price for quantities 5, 25, and 50
- Tooling / setup costs (one-time), if any
- Estimated lead time for first article and for full production quantity
- Shipping cost to Bengaluru, India (CIF Bangalore preferred for comparison)
- Validity period of the quote
- Any exclusions or assumptions that could affect pricing

We expect responses by [date — 7 business days from send date]. If you anticipate timing challenges, please let us know early so we can adjust our evaluation schedule.

Please send the quote in PDF format to [procurement email] with the subject line "Quote — QOSMIC-OPT-2026-0012 — [Your Company Name]".

Thank you,

[Name]
QOSMIC SPACE

**Attachments:**
- QOSMIC-OPT-BRACKET-2026-RevA.pdf
- QOSMIC General Terms for Prototype Procurement (optional, for new vendors)

---

### Template B: Follow-Up — After 5 Business Days of Silence

**Subject:** Follow-Up: RFQ QOSMIC-OPT-2026-0012 — Custom Aluminum Optical Mount

Dear [Contact Name],

I sent a request for quotation (below) on [original date] for a custom aluminum optical mount (5 units initial, 25-50 units potential production). I haven't heard back yet.

If you're working on the quote and need more time, a quick note on expected delivery date would help. If you're unable to quote this work, a brief reply is fine — I'll arrange my vendor list accordingly.

If the email or attachments didn't come through, let me know and I'll resend.

Thanks,

[Name]
QOSMIC SPACE

---

### Template C: Negotiation — Quote 30%+ Above Budget

**Subject:** RE: Quote — QOSMIC-OPT-2026-0012 — [Vendor Name]

Dear [Contact Name],

Thanks for the detailed quote. We appreciate the thoroughness.

At [quoted total], this comes in about [X]% above our budget range for this part. We'd like to proceed with you if we can get closer to our target.

Could you share a cost breakdown — material, machining time, finishing, and tooling separately — so we can understand the main cost drivers? We're open to adjusting specifications if there are particular features driving cost.

Specifically, we could consider:
- Switching the surface finish from clear anodise to as-machined on non-functional surfaces
- Relaxing the Ra 0.8 on non-critical faces to Ra 3.2
- Accepting a longer lead time
- Adjusting payment terms (we can do net 15 or advance payment if that helps cash flow)

Alternatively, if there's a standard product you offer that meets 80% of the spec at a lower price point, we'd be interested.

We'd like to close this within [X] days. If [X]% off the quoted price is achievable, we can issue the PO today.

Best,

[Name]
QOSMIC SPACE

---

## 4. Email Tone Guide

| Template | Tone | Goal |
|----------|------|------|
| RFQ (A) | Professional, technically detailed | Communicate competence and seriousness. A well-written RFQ gets a better response rate. |
| Follow-up (B) | Polite, recognises competing priorities | Gentle nudge. Do not imply the vendor is disorganised. |
| Negotiation (C) | Firm but constructive | Signal budget constraint without threatening. Open the door for a competitive counter. |

**General principles:**
- Always include a part number or reference in the subject line — vendors track by their own systems.
- Attach the drawing as PDF, not STEP/DXF — the vendor will request the native file if they need it.
- State a response deadline in the first email, not hidden in the last paragraph.
- If a vendor consistently ignores follow-ups for two consecutive RFQs, move them to conditional status in the vendor database and reduce their solicitation frequency.
