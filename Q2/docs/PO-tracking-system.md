# PO Tracking System

## 1. Status Flow

Each purchase order moves through the following states. Transitions are logged in Airtable with a timestamp and the person/system who made the change.

```
 Issued
   │
   ▼
 Acknowledged ───[3 day silent]──→ Alert: Vendor Not Acknowledged
   │
   ▼
 In Production
   │
   ▼
 Shipped
   │
   ▼
 In Transit ───[customs clearance]──→ Customs Hold
   │                                      │
   ▼                                      ▼
 Delivered                             Cleared (continues to Delivered)
   │
   ▼
 Inspected ───[reject]──→ Rejected
   │
   ▼
 Accepted
```

**Status Definitions:**

| Status | Meaning | Who Can Advance |
|--------|---------|-----------------|
| **Issued** | PO has been sent to vendor. No response yet. | System (on create) |
| **Acknowledged** | Vendor has confirmed receipt and committed to a delivery date. | Procurement (manual, on receipt of vendor acknowledgement) |
| **In Production** | Vendor has confirmed manufacturing has started. | Procurement (manual, on vendor communication) |
| **Shipped** | Vendor has dispatched. Tracking number recorded. | Procurement (manual, from shipping notification) |
| **In Transit** | Goods are en route. Tracking being monitored. | System (auto from tracking number activation) |
| **Customs Hold** | Shipment held at customs. Clearance documents pending. | Procurement (manual, from customs broker update) |
| **Delivered** | Package received at QOSMIC facility. | Receiving team (manual, upon physical receipt) |
| **Inspected** | Incoming inspection completed. Results recorded. | QA/inspector (manual, after checklist completed) |
| **Accepted** | Passed inspection. Matches PO spec. Stocked. | QA/inspector (manual) |
| **Rejected** | Failed inspection. Rejection workflow initiated. | QA/inspector (manual) |

---

## 2. Automated Alert Triggers

All alerts are configured in Airtable automations. Each sends a Slack message to the procurement channel and emails the person responsible.

| Trigger | Condition | Action | Recipient |
|---------|-----------|--------|-----------|
| PO not acknowledged | Status = Issued for > 3 business days | Slack alert + email | Procurement |
| Ship date approaching | Status = In Production, today > (promised ship date - 5 days) | Slack reminder | Procurement |
| Delivery overdue | Status ≠ Delivered, today > promised delivery date | Slack alert + email | Procurement + requester |
| No tracking update | Status = In Transit for > 7 days with no location update | Slack alert | Procurement |
| Customs hold > 3 days | Status = Customs Hold for > 3 business days | Slack alert + email | Procurement + CEO (if high-value) |
| Quarterly budget exceed | Sum of PO values for this vendor in current quarter > 120% of quarterly budget | Slack alert + email | Procurement + CEO |
| Inspection pending | Status = Delivered for > 2 business days, not yet inspected | Slack reminder | QA/inspector + procurement |

**Implementation:** Each alert is a single Airtable automation with a conditional trigger. No external tooling needed — 25,000 automation runs/month on the free Airtable plan covers this easily.

---

## 3. International Shipment Tracking

### Why Additional Tracking is Needed
International shipments into India require customs clearance, import duty payment, and transit insurance. A European optical component worth ₹1.2L ($1,244) can sit at Bengaluru customs for 3-10 days if documentation is wrong. This section tracks those extra steps.

### Fields Added to the PO Record for International Shipments

| Field | Example | Where It Comes From |
|-------|---------|---------------------|
| HS Code | 9013.80 (optical instruments) | Set at PO creation based on part type |
| CIF Value (USD) | $1,244 | PO total + estimated freight + insurance |
| BCD Rate | 7.5% | From HS code lookup table (verified at cybex.in) |
| IGST Rate | 18% | Standard for HS chapter 90 |
| Estimated Total Duty | $345 (CIF × effective rate ~27.7%) | Auto-calculated from rates |
| Clearing Agent | DHL Customs / FedEx Trade Networks | Selected at PO creation |
| Customs Broker Fee | ₹5,000 ($52) | Verified: ₹2,000-10,000 per shipment (azafra.mx) |
| Shipping Insurance | 1.5% of CIF ($18.66) | Auto-calculated if CIF > $500 |
| Bill of Entry Number | 2026-BLR-CUS-4412 | Entered on clearance |
| Duty Paid Date | 2026-05-15 | Entered on clearance |
| Actual Duty Paid | $340 | Entered after duty invoice received |

### Customs Clearance Checklist
- [ ] HS code verified against latest customs tariff (2026-27)
- [ ] Commercial invoice matches PO exactly (quantity, unit price, total, part number)
- [ ] Packing list attached (item count, weight, dimensions)
- [ ] Bill of lading / airway bill number recorded
- [ ] Certificate of origin (for EU vendors: benefits under India-EU FTA if applicable)
- [ ] For optics: no ITC restriction on import (Chapter 90 is generally free — verify for laser-related items)
- [ ] Duty amount pre-funded or line of credit active
- [ ] Customs broker appointed and briefed on shipment

### Shipping Insurance Policy
- All shipments with CIF value > ₹50,000 ($518) must have transit insurance.
- Insurance covers: loss, theft, physical damage in transit.
- Premium: typically 0.5-2% of declared value. Obtain quote from the freight forwarder.
- Insurance provider and policy number recorded in the PO record.
- For precision optics (wavefront error-critical components): add "rough handling damage" clause.

---

## 4. Vendor Follow-Up: 6-Week Critical-Path Component

This sequence applies when a component is on the critical path — a delay directly impacts a committed delivery date to a customer or a demo. It assumes a 6-week (42-day) lead time from PO issue.

| Week | Day | Tone | Action | Template Summary |
|------|-----|------|--------|------------------|
| Week 1 | Day 1 | Formal | Send PO. No follow-up needed yet. | — |
| Week 2 | Day 14 | Routine check-in | Brief email confirming all is on track, no pressure. | "Checking in — just confirming the timeline is still on track for [promised ship date]. No action needed if everything is on schedule." |
| Week 3 | Day 21 | Mild curiosity | Single question about progress. | "Quick check on the [part name] — any production updates you can share? No urgency, just planning our downstream schedule." |
| Week 4 | Day 28 | Expectation-setting | Reference the promised delivery date. Shift from "checking" to "planning around you." | "Based on our agreed timeline of [date], we're scheduling our assembly window around this delivery. Can you confirm the ship date is still firm?" |
| Week 5 | Day 35 | Firm | Explicit reference to the delivery commitment. Request a concrete update. | "We're inside the 1-week window before your promised ship date of [date]. Can you confirm: (1) has production completed? (2) when will it ship? (3) tracking number? If there's a schedule change, this is the moment to tell us." |
| Week 6+ | Day 42+ | Escalation | If delayed past the promised date, switch to damage control. CC the vendor's manager or escalate internally. | "The shipment has not arrived by the committed date of [date]. This is now delaying our customer delivery. Please provide: (1) revised ship date, (2) root cause of delay, (3) expedited shipping method (we will pay difference if needed). CC'ing [vendor manager] for visibility. If we do not have a concrete update within 48 hours, we will need to escalate to our CEO." |

### Tone Guide for the Sequence

| Phase | Emotional Content | Goal |
|-------|------------------|------|
| Week 2 | Neutral, friendly | Vendor knows they're being tracked but not pressured |
| Week 3 | Mild interest | Vendor knows someone is paying attention |
| Week 4 | Respectful expectation | Vendor realises this is a real deadline, not a placeholder |
| Week 5 | Businesslike firmness | No room for ambiguity — vendor must respond |
| Week 6 | Escalation | Vendor understands this is a relationship-level issue |

### Full Email Texts

**Week 2 Email (Day 14):**
Subject: Quick check — QOSMIC-PO-2026-0042

Hi [Contact Name],

Just checking in on PO 2026-0042 ([part name]). We're about two weeks in — wanted to confirm everything's tracking fine for the [date] ship date. No action needed if you're on schedule.

Thanks,

[Name]

**Week 4 Email (Day 28):**
Subject: Schedule confirmation — QOSMIC-PO-2026-0042

Hi [Contact Name],

Following up on PO 2026-0042 ([part name]) with the agreed ship date of [date]. We're planning our downstream assembly schedule around this delivery. Can you confirm the ship date is still firm?

If there's any shift, please let me know now so we can adjust — earlier notice helps us both.

Thanks,

[Name]

**Week 5 Email (Day 35):**
Subject: URGENT: Ship date confirmation needed — QOSMIC-PO-2026-0042

Hi [Contact Name],

We're one week out from the promised ship date of [date] for PO 2026-0042 ([part name]). Can you please confirm:

1. Has production been completed?
2. What is the confirmed ship date?
3. Do you have a tracking number?

If the schedule has changed, please tell us now so we can make contingency plans. No judgement on delays — but silence will leave us in a difficult position.

Regards,

[Name]

**Week 6+ Escalation Email (Day 42+):**
Subject: DELAY: QOSMIC-PO-2026-0042 — [part name] — action required

Hi [Contact Name],

The shipment for PO 2026-0042 ([part name]) was due on [date] and has not arrived. This part is on our critical path — this delay is now impacting our customer delivery.

I need the following within 48 hours:

1. Revised ship date
2. Root cause of the delay
3. Whether you can expedite shipping (we'll cover any incremental cost)

I'm CC'ing [sales manager / account manager] for visibility on this.

If we don't have a concrete update by [date + 2 days], I'll need to escalate this to our CEO and begin identifying an alternative supplier.

Regards,

[Name]
[Title], QOSMIC SPACE

Copy: [vendor manager email]
