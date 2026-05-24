# Tool Stack Proposal

## Constraints (from the interview PDF)
- Usable by one non-developer
- Under $200/month
- Integrates with email and Slack

## Recommended Stack

| Tool | Plan | Monthly Cost | Role in System |
|------|------|-------------|----------------|
| **Airtable** | Free | $0 | Core database: purchase requests, vendor DB, PO tracking, inspection records, scorecard. Form views for request intake. Kanban view for PO status. |
| **Gmail / Google Workspace** | Free (personal) or Business Starter | $0-6 | Email for all vendor communication. Labels and filters for PO tracking. |
| **Slack** | Free | $0 | Alert channel (#procurement-alerts) for automated notifications. |
| Make.com | Free | $0 | Automation engine connecting Airtable → Slack alerts. 1,000 credits/month, 2 active scenarios, 15-min minimum interval. |
| **Google Drive** | Free (15GB) | $0 | Storage for drawings, quotes, inspection photos, C of C documents. |
| **PDF Reader / Editor** | Free (built-in) | $0 | Viewing vendor quotes and drawings. |

**Total monthly cost: $0-6** (depending on whether Google Workspace is already paid for)

### Why This Stack

**Airtable as the core:** It is the only tool that non-developers can actually build on. It replaces a custom database + a spreadsheet + a project tracker. The free plan supports 1,000 records per base — enough for a startup processing 15-25 POs/month. If the company scales past 1,000 records, the Team plan at $20/month unlocks 50,000 records.

**Make.com for automation:** It connects Airtable to Slack and Gmail without writing code. The visual builder is usable by a non-developer after a 30-minute tutorial. The free plan (1,000 credits/month) handles the alert triggers defined in PO-tracking-system.md — each alert is roughly 5-10 credits (read Airtable record + send Slack message + send email).

**No-code, not low-code:** The system must be maintainable by the procurement person without engineering support. Airtable + Make.com is the most mature no-code stack for this use case. Alternatives like Notion (weaker automations), Zapier (more expensive at scale), or custom code (requires a developer) all fail one of the constraints.

### What Each Tool Does in Practice

**Airtable Tables:**
1. **Purchase Requests** — form submissions, approval status, linked to POs
2. **Vendors** — vendor database with all schema fields from vendor-database-schema.md
3. **Purchase Orders** — one record per PO, linked to request and vendor, with status field driving the Kanban view
4. **Inspections** — one record per incoming inspection, linked to PO, with checklist results
5. **Scorecards** — quarterly vendor performance summary, auto-calculated from PO and inspection data

**Slack Channel (#procurement-alerts):**
- Automated messages from Make.com for: unacknowledged POs, overdue deliveries, budget threshold alerts, inspection reminders
- The procurement person monitors this channel daily

**Make.com Automations (2 core workflows, 1 planned):**
1. New purchase request submitted with cost > ₹50,000 → notify CEO on Slack
2. PO past promised delivery date, not yet delivered → alert procurement on Slack
3. *(Planned, requires Make Core)* PO status = Issued for 3+ days → alert procurement on Slack

### Scaling Path

| Stage | Monthly POs | Tool Upgrade | New Cost |
|-------|------------|--------------|----------|
| Now (seed) | 15-25 | Free plans suffice (2 automations on Make Free) | $0 |
| Growth (Series A) | 25-75 | Make Core ($12/mo) for 3rd automation + higher ops | $12 |
| Scale (production) | 75-200 | Airtable Team ($20/seat) + Make Core ($12) | $32 |
| Mature | 200+ | Airtable Business ($45/seat) + Make Pro ($21) | $66 |

Even at the mature stage, the total is well under $200/month. The $200 budget ceiling is not a constraint for this system at any realistic scale.

### What NOT to Use (and Why)

| Tool | Why Not |
|------|---------|
| SAP / Oracle / NetSuite | Overkill. Requires dedicated admin. $500+/month minimum. |
| Jira | Built for software development procurement, not hardware. Poor form handling. |
| Notion | Weaker automations than Airtable. No native form views. Automation requires external tools anyway. |
| Zapier | More expensive than Make.com at equivalent scale. Free tier is too limited (100 tasks/month). |
| Custom web app | Requires a developer. Violates the non-developer constraint. |
| Excel / Google Sheets alone | No native automation, no form views, no relational data. Becomes unmanageable past ~200 rows. |
