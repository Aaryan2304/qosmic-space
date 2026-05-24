# Implementation Cost Estimate

## One-Time Setup Costs

| Item | Cost | Notes |
|------|------|-------|
| Airtable base setup (5 tables, views, links) | 0 (self-built, ~3 hours) | Free plan |
| Make.com automation setup (5 workflows) | 0 (self-built, ~2 hours) | Free plan |
| Google Drive folder structure | 0 | Free |
| Slack channel (#procurement-alerts) | 0 | Free |
| Template documents (RFQ, rejection, inspection) | 0 | Written in this repo |
| Scratch-dig paddle (Edmund Optics, stock #91-291) | $165 | One-time. Only needed if doing in-house optical QC to MIL-PRF-13830B standard. |
| Digital calliper (0.01mm resolution) | $20-50 | One-time. Amazon India. |

**Total one-time cost: $0-215** (depending on whether optical QC equipment is purchased)

## Recurring Monthly Costs

| Item | Cost | Notes |
|------|------|-------|
| Airtable Free | $0 | Sufficient for 15-25 POs/month |
| Make.com Free | $0 | 1,000 credits/month |
| Slack Free | $0 | |
| Gmail / Google Workspace | $0-6 | Free personal Gmail or $6 for Workspace |
| Claude API (for AI automations) | ~$0.50 | ~50 automation calls/month at $0.01/call |
| Shipping insurance (per shipment) | Varies | 0.5-2% of CIF value, only on international shipments >$518 |
| Customs broker fee (per shipment) | $31-83 | Per international shipment into India (verified: azafra.mx reports ₹2,000-10,000 typical) |

**Total recurring cost (excluding shipping/insurance/brokerage): $0-6.50/month**

The shipping insurance and customs broker fees are operational costs of importing goods, not system costs. They scale with procurement volume.

## Cost vs. the $200/month Budget

The system as designed costs **$0-6.50/month** in tooling. The remaining budget headroom ($193.50+) is available for:
- Upgrading to Airtable Team ($20/month) when record count exceeds 1,000
- Upgrading Make.com to Core ($12/month) when automation volume exceeds 1,000 credits/month
- Adding a dedicated procurement tool (e.g., Procru, Precoro) if the company scales past 100 POs/month

At no point does this system approach the $200/month ceiling. The constraint is not binding.
