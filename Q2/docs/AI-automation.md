# AI/LLM Automation Opportunities

## Framework: Automatable vs. Human-Judgment

The question is not "can AI do this?" but "can AI do this *reliably enough* that a human doesn't need to check every output?" For each task below, I classify it as:

- **Fully automatable:** AI produces output that can be used as-is or with a quick human glance.
- **Partially automatable:** AI produces a draft that a human must review and edit before use.
- **Human-judgment:** AI can assist with research or data gathering, but the decision requires human expertise.

---

## Phase 1: Request & Vendor Selection

| Task | Automation Level | How | Tool | Caveat |
|------|-----------------|-----|------|--------|
| Drafting RFQ emails from request form data | **Partially automatable** | Claude/GPT takes the part spec, quantity, and drawing reference from the Airtable record and drafts the RFQ email. Human reviews for technical accuracy before sending. | Claude via Make.com or manual prompt | The AI doesn't know your vendor's capabilities or your internal spec conventions. First-time use requires heavy editing. After 5+ RFQs, the template is stable and AI just fills in the blanks. |
| Checking request form completeness | **Fully automatable** | Airtable form validation (built-in, no AI needed) + a Make.com automation that flags missing fields or inconsistent data. | Airtable + Make.com | This is rule-based, not AI. It's the right tool for the job. |
| Vendor shortlisting | **Partially automatable** | AI queries the vendor database and recommends vendors based on capability match, past performance, and lead time. Human makes the final call. | Claude + Airtable API | The AI can miss context — e.g., a vendor is "approved" but currently overloaded. Human must verify. |
| Approval routing | **Fully automatable** | Rule-based: if total < ₹5K → self-approved; ₹5K-50K → CTO; > ₹50K → CEO. No AI needed. | Airtable automation | Pure if/then logic. AI adds no value here. |

## Phase 2: Order Tracking & Follow-Up

| Task | Automation Level | How | Tool | Caveat |
|------|-----------------|-----|------|--------|
| PO status tracking | **Fully automatable** | Airtable Kanban view + Make.com automations for alerts. No AI needed. | Airtable + Make.com | Rule-based. |
| Vendor follow-up email drafting | **Partially automatable** | AI drafts the follow-up email based on the PO record (days since last contact, promised date, tone appropriate to the week). Human reviews and sends. | Claude via Make.com | Tone calibration is important. An AI-generated email that sounds like an AI-generated email defeats the purpose. Needs a human pass. |
| Parsing vendor quote PDFs into comparison matrix | **Fully automatable** | AI extracts line items, prices, lead times, and terms from vendor quote PDFs and populates an Airtable comparison table. | Claude / GPT-4V with PDF input, or a tool like Docparser | This is the highest-value automation in the system. Vendor quotes come in different formats — AI normalises them into a single comparison table. Saves 30-60 minutes per RFQ cycle. |
| Customs documentation pre-fill | **Partially automatable** | AI takes the PO data (part description, value, HS code) and pre-fills the Bill of Entry and commercial invoice templates. Human verifies before submission. | Claude + Google Docs template | HS code classification can be wrong. A human who understands the product must verify. Getting the HS code wrong costs days at customs. |

## Phase 3: Quality Tracking

| Task | Automation Level | How | Tool | Caveat |
|------|-----------------|-----|------|--------|
| Vendor scorecard calculation | **Fully automatable** | Airtable formulas compute the metrics from PO and inspection data. No AI needed. | Airtable formula fields | Pure arithmetic. |
| Scorecard narrative summary | **Partially automatable** | AI reads the scorecard data and generates a one-paragraph summary for the quarterly review meeting. Human edits for accuracy. | Claude | Useful for preparing review meeting packs. The AI might misinterpret a metric — e.g., a high rejection rate on a single difficult part vs. a pattern. |
| Rejection email drafting | **Partially automatable** | AI takes the inspection data (measured vs. specified values, photos) and drafts the rejection email with the defect table. Human verifies measurements and photos before sending. | Claude + Airtable | The measurements must be exact. AI can format them, but the human must have verified the calliper readings first. |

---

## Summary: What to Automate First

| Priority | Automation | Time Saved per Month | Effort to Set Up |
|----------|-----------|---------------------|-----------------|
| 1 | Quote PDF parsing → comparison matrix | 3-5 hours | Medium (one-time Make.com + Claude setup) |
| 2 | RFQ email drafting from form data | 1-2 hours | Low (template + Make.com) |
| 3 | Follow-up email drafting | 1-2 hours | Low (template + Make.com) |
| 4 | Rejection email drafting | 30 min | Low (template + Make.com) |
| 5 | Scorecard narrative summary | 30 min | Low (one-time prompt) |

**Total time saved: 6-9 hours/month** for a procurement person handling 15-25 POs. That's meaningful.

## What Should NOT Be Automated

| Task | Why Not |
|------|---------|
| Vendor selection decision | Requires understanding of strategic relationships, current vendor workload, and technical fit. AI can shortlist, not decide. |
| Approval decisions | The CTO/CEO need to see the spec and the cost. Automating the routing is fine; automating the decision is not. |
| Incoming inspection | Physical measurement and visual inspection cannot be automated without a machine vision system (not justified at this scale). |
| Negotiation | The back-and-forth of negotiation requires reading the vendor's situation, understanding market dynamics, and making judgment calls. AI can draft the email, not negotiate. |

## Implementation Note

All AI automations described above use Claude (or any LLM with a good API) triggered by Make.com. The cost is:
- Make.com Free: 1,000 credits/month (sufficient for ~2 active scenarios at hourly intervals)
- Claude API: ~$0.01-0.03 per automation call (Haiku) → ~$0.20-0.90/month for the volume described

**Total AI automation cost: under $1/month** on top of the base tool stack.

**Currently deployed automations (2 on Make.com Free):**
1. PO overdue → Slack alert
2. High-value request (₹50,000+) → Slack alert for CEO approval
3. *(Planned)* PO not acknowledged in 3 days → Slack alert (requires Make Core upgrade for 3rd scenario)
