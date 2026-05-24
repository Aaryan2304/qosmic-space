# Approval Thresholds: Justification

## Context
QOSMIC is a seed-stage startup at approximately ₹18L/month burn (~$18,650/month at ₹96.5/USD). At this burn rate, cash is the constraint. Every purchase decision must balance speed (don't slow down engineering) against oversight (don't waste money). The thresholds below are designed so that oversight scales with financial impact.

## Threshold Table

| Purchase Total | Approval Required | Rationale |
|---------------|-------------------|-----------|
| < ₹5,000 (< ~$52) | Self-approved (requester only) | Small tools, fasteners, cables, common consumables. ₹5K is 0.28% of monthly burn. A wrong decision at this level costs less than the overhead of CTO reviewing it. |
| ₹5,000 – ₹50,000 ($52 – $518) | CTO approval | Covers most custom-machined parts, standard optical components, and small assemblies. ₹50K is 2.8% of monthly burn. The CTO can assess whether the spec is correct and the price is reasonable. |
| > ₹50,000 (> ~$518) | CEO approval | Major optical assemblies, custom optics, long-lead items, multi-unit batches. Requires CEO visibility because these orders commit significant cash and often have 4-12 week lead times — a cancellation or delay has strategic impact. |

## Why These Numbers Specifically

**₹5,000 floor:** At a seed-stage hardware startup, the engineer's time is more expensive than the parts under this threshold. If a ₹1,500 pack of M6 bolts needs CTO sign-off, the engineer stops working to write a justification and the CTO stops working to approve it — that's 2×30 minutes of engineering time, conservatively ₹2,000 in salary cost, for a ₹1,500 purchase. Self-approval below ₹5K is cheaper.

**₹50,000 ceiling on CTO authority:** At ₹18L/month burn, a ₹50K purchase is small enough that one bad one doesn't materially affect runway. But three ₹50K bad purchases in a month (₹1.5L) is 8.3% of monthly burn and starts to hurt. The CEO seeing every purchase above ₹50K prevents a pile-up of mid-sized commitments without visibility.

**No CEO approval on < ₹50K emergency purchases:** An exception exists for critical-path items where delay costs more than the part. If a ₹12K component is holding up a customer demo, the CTO can approve it immediately without CEO bypass — but must tag the record as "expedited" with the reason documented.

## Engineering Materials Specifically

Optical components (lenses, mirrors, waveplates) are case-by-case because a single lens can cost ₹200 or ₹2,00,000. For these:

- **Standard catalog optics** (Thorlabs, Edmund Optics, Newport): follow the same threshold table. The vendor list has negotiated pricing, so the procurement person can verify price against previous PO.
- **Custom optical components** (coated mirrors, precision lenses): always require CEO approval regardless of value. These have 6-12 week lead times and cannot be returned if wrong.

## How This Plays Out in Practice

| Part | Est. Cost | Approval Path | Time to Approve |
|------|-----------|--------------|-----------------|
| 50× M6×12mm socket head cap screws | ₹1,200 | Self-approve | 0 minutes |
| 10× SM1-threaded post holders | ₹15,000 | Engineer submits, CTO reviews by EOD | < 4 hours |
| Custom aluminium bracket (prototype run of 5) | ₹35,000 | CTO review (checked spec + drawing) | < 1 day |
| Precision mirror mount (stainless, spring-loaded) | ₹42,000 | CTO review | < 1 day |
| Custom off-axis parabolic mirror (2" dia, protected silver) | ₹1,20,000 | CEO review with CTO recommendation | < 2 days |
| Full assembly: 8-element beam expander | ₹3,50,000 | CEO review with written cost-benefit memo | < 3 days |

## Edge Cases

**Batched purchases:** Multiple line items on one PO use **total PO value** to determine approval level. Splitting a ₹60K order into two ₹30K POs to bypass CEO approval is a policy violation.

**Recurring orders:** Reorders of previously approved parts within the same quarter skip the approval gate entirely — go straight to PO. Reorders in a new fiscal quarter follow the threshold table again.

**Quarterly budget alerts:** If a department's cumulative procurement spend exceeds 80% of its quarterly budget, subsequent requests from that department are auto-flagged for CFO review regardless of individual value.

## Integration with Airtable

The Airtable template has an automation:
1. On form submission, read Estimated Total Cost
2. If < ₹5,000: set Status = "Approved (Self)", notify requester and procurement
3. If ₹5,000 - ₹50,000: set Status = "Pending CTO Approval", notify CTO via Slack
4. If > ₹50,000: set Status = "Pending CEO Approval", notify CEO via Slack with link to record
5. On approval action (button click in Airtable): Status → "Approved", timestamped, logged
