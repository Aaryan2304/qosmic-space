# Q2: End-to-End Vendor Procurement System

A complete procurement system for QOSMIC SPACE, covering the full lifecycle from internal request to vendor quality tracking.

## Contents

| Directory | Description |
|-----------|-------------|
| `docs/` | All 13 system documentation files (markdown) |
| `screenshots/` | Screenshots of the working Airtable prototype |
| `deliverables/` | Compiled deliverable document (HTML + PDF) |
| `Q2_Deliverable.pdf` | **Main submission document** — single PDF with all sections and screenshots |

## Deliverables Phase Coverage

**Phase 1 — Internal Request, Specification & Vendor Selection**
- Purchase request form with 20+ fields
- Custom-machined parts pre-submission checklist (21 items)
- Approval thresholds with justification at 18L/month burn
- Vendor database schema with 4 sample entries
- RFQ process + 3 email templates

**Phase 2 — Order Tracking, Follow-Up & Incoming Inspection**
- PO tracking system with 10-status flow + 7 automated alerts
- International customs tracking with verified duty rates
- 6-week critical-path vendor follow-up email sequence
- Incoming inspection checklists (machined parts + precision optics)
- Rejection workflow with email template + partial shipment policy

**Phase 3 — Quality Tracking & System Architecture**
- Vendor quality scorecard with 7 weighted metrics
- Tool stack at $0/month (Airtable Free + Make.com Free + Slack)
- AI/LLM automation analysis (10 tasks ranked)
- Airtable prototype with 5 sample POs in varying stages
- Implementation cost breakdown

## Live Prototype

The Airtable base is live at:
[QOSMIC Procurement Base](https://airtable.com/appjG6EmwqTczL6Sk/shrkQDqxASSepMnQL)

## Tools Used

All built on free tiers:
- **Airtable Free** — Database, Kanban, Forms, linked records
- **Make.com Free** — 2 automations live (overdue PO alert, high-value request alert)
- **Slack Free** — #procurement-alerts channel receiving automated notifications

Total tooling cost: $0/month.

**Connected automations (live):**
1. PO overdue → Slack alert via Make.com
2. Purchase request > ₹50,000 → Slack alert for CEO approval
3. *(Planned)* PO not acknowledged in 3 days → requires Make Core ($12/mo) for 3rd scenario slot

## How to Read This

Open `Q2_Deliverable.pdf` first — it's the full system documentation with embedded screenshots.
Individual markdown files in `docs/` contain the detailed version of each section.
