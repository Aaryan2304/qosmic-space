# Vendor Quality Scorecard

## Purpose
After a vendor has completed 10+ orders, the scorecard provides an objective basis for the keep/replace decision. It is reviewed quarterly and triggers action when a vendor's performance degrades.

## Metrics (7 total)

| # | Metric | What It Measures | Target | Weight |
|---|--------|-----------------|--------|--------|
| 1 | On-time delivery rate | % of orders delivered on or before the promised date | ≥ 90% | 25% |
| 2 | Quality rejection rate | % of received lots rejected at incoming inspection | ≤ 3% | 25% |
| 3 | Quote accuracy | Average deviation of quoted price from final invoice (excluding scope changes) | ≤ 5% | 10% |
| 4 | Lead time consistency | Standard deviation of actual lead time vs. quoted lead time (in days) | ≤ 7 days | 10% |
| 5 | Responsiveness | Average time to acknowledge PO and respond to RFQs (in business days) | ≤ 2 days | 10% |
| 6 | Documentation quality | % of shipments with complete documentation (C of C, packing list, invoice, test reports) | 100% | 10% |
| 7 | Issue resolution speed | Average time to resolve a rejection or complaint (in business days) | ≤ 5 days | 10% |

## Scoring Methodology

Each metric is scored 0-100:

| Score | Meaning |
|-------|---------|
| 90-100 | Exceeds target — best in class |
| 70-89 | Meets target — acceptable |
| 50-69 | Below target — needs improvement |
| 0-49 | Unacceptable — immediate action required |

**Composite Score** = Σ (metric score × weight)

| Composite Score | Vendor Status | Action |
|-----------------|---------------|--------|
| ≥ 85 | **Preferred** | Increase share of business. Negotiate better terms. |
| 70-84 | **Approved** | Continue as-is. Monitor quarterly. |
| 55-69 | **Conditional** | Issue improvement plan. 90-day review. Reduce new POs. |
| < 55 | **Probation / Replace** | Actively source alternative. No new POs until improvement. |

## Review Trigger Thresholds

A vendor review is triggered immediately (not waiting for quarterly) when:
- Quality rejection rate exceeds 5% in any single month
- On-time delivery rate drops below 80% in any single quarter
- Two or more rejections in a rolling 6-month window
- Vendor fails to respond to a rejection notice within 5 business days

## Scorecard Example

| Metric | Vendor A (Jenoptik) | Vendor B (Precision Bengaluru) | Vendor C (JLCPCB) |
|--------|---------------------|-------------------------------|---------------------|
| On-time delivery | 88.7% → 85 | 82.3% → 70 | 96.2% → 95 |
| Quality rejection | 0.8% → 95 | 4.6% → 55 | 1.4% → 90 |
| Quote accuracy | 3% → 90 | 8% → 65 | 1% → 95 |
| Lead time consistency | ±12 days → 70 | ±8 days → 75 | ±3 days → 95 |
| Responsiveness | 1.5 days → 90 | 3 days → 70 | 1 day → 95 |
| Documentation | 100% → 100 | 85% → 75 | 100% → 100 |
| Issue resolution | 4 days → 85 | 8 days → 60 | 2 days → 95 |
| **Composite** | **88.0 — Preferred** | **67.5 — Conditional** | **94.4 — Preferred** |

## Data Source
All metrics are calculated from Airtable records:
- On-time delivery: PO promised date vs. actual delivery date
- Quality rejection: Inspection records linked to each PO
- Quote accuracy: RFQ table vs. final PO value
- Lead time consistency: Quoted lead time vs. actual (delivery date - PO date)
- Responsiveness: Timestamp of first vendor reply after PO/RFQ send
- Documentation: Checklist completed flag on receiving record
- Issue resolution: Rejection date to resolution date

## Quarterly Review Process
1. Procurement runs the scorecard report (Airtable view filtered by vendor, grouped by quarter).
2. Vendors scoring below 70 are flagged for a review meeting.
3. The review meeting covers: root cause of underperformance, improvement plan with specific targets and dates, and a decision on whether to continue or begin sourcing alternatives.
4. The outcome is recorded in the vendor database notes field.
5. If a vendor on conditional status does not improve within two review cycles (6 months), status is changed to inactive.
