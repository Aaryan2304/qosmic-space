# AI Tool Usage Documentation

*How AI was used in completing the QOSMIC Founder's Office technical interview.*

---

## What I Used

I used an AI coding assistant throughout this project. I also used web search extensively to verify claims, look up documentation, and cross-check facts.

The AI was my primary tool for: drafting documents, writing code, looking up documentation, cross-referencing my work against the requirements, and catching errors. I was the one making decisions, verifying output, and deciding what to keep or discard.

---

## How I Used It — By Task

### Reading and Understanding the Task

The PDF is dense. Before writing anything, I asked the AI to:

- Break down each question (Q1, Q2, Q3, Grand Challenge) into specific deliverables
- Identify what the evaluation criteria actually mean in practice ("execution quality" ≠ "it compiles")
- Create a checklist of every required output so I could track progress

This saved me from missing requirements. But I still read the PDF myself multiple times and caught things the AI missed — like the "document exactly how you used AI" instruction, which is easy to skip if you're just executing quickly.

### Q1 — Knowledge Graph & RAG Pipeline

**Schema design:** I asked the AI to design the knowledge graph schema with the 6 node types and 6 link types required by the PDF. I then modified the field names and structure to match how QOSMIC's engineering team would actually think about their system — for example, splitting "Design Decisions" into specific fields like "alternatives considered" and "trade-offs" instead of a generic "notes" field.

**Obsidian vault content:** I asked the AI to create 20+ sample notes covering at least 2 subsystems with technically realistic content. The AI produced drafts based on general knowledge of optical ground stations. I then verified the technical claims — for example, I checked that the Ritchey-Chrétien explanation was accurate, that the FSM bandwidth requirement (400 Hz) was correctly explained with its physics rationale, and that the component part numbers (Thorlabs PIA13) actually exist with the specs cited.

**RAG pipeline code:** I asked the AI to design and implement the Python RAG pipeline (indexer, retriever, query handler). I then tested the code locally, fixed import errors, and simplified parts that were over-engineered for the prototype scope.

**Templates and workflow:** I asked the AI to create the 6 Obsidian markdown templates and the contribution workflow document. I modified the templates after thinking about how an engineer would actually use them day-to-day — what fields are essential vs. what creates friction.

### Q2 — Procurement System

**Research phase:** Before designing anything, I needed to understand the domain. I asked the AI to:

- Research India customs duty rates for optical components (HS 9013 and 9002)
- Look up the duty calculation methodology (BCD + SWS + IGST)
- Find customs broker fee ranges for India
- Verify which HS codes apply to which types of optical components

I then cross-checked these numbers against official sources: DHL India's import guide, cybex.in for HS code lookups, and Make.com's own documentation for tool limits. The AI got some things wrong — for example, it initially cited a `dateDifference()` function for Make.com that doesn't actually exist (it's a Power Automate function). I caught this during verification and found the correct approach (timestamp subtraction in milliseconds).

**Document drafting:** I asked the AI to draft all 13 system documents: purchase request form, machining checklist, approval thresholds with justification, vendor database schema, RFQ templates, PO tracking system, international shipment tracking, follow-up email sequence, inspection checklists, rejection workflow, vendor scorecard, tool stack proposal, and AI automation analysis.

For each document, I reviewed the output, checked it against the PDF requirements, and modified what didn't match. For example, the AI initially proposed 5 Make.com automations. When I verified against Make.com's actual pricing page, I found the Free tier only supports 2 active scenarios, not 5. I adjusted the plan accordingly and documented the 3rd scenario as "planned, requires Core upgrade."

**Airtable build:** I built the Airtable base myself using the documented schema. I created the 5 tables, set up linked records, configured views (Kanban, Grid, Form), and entered the 5 sample POs. This was hands-on work — clicking through Airtable's interface, setting field types, creating formulas.

**Automation setup:** I built the 2 Make.com scenarios myself following the configuration guide. This involved connecting Airtable and Slack, setting up the Watch Records trigger, configuring filters with the correct operators (scrolling past "Text operators" to find "Date operators" for the "Earlier than" condition), and testing by running the scenarios and verifying Slack messages appeared. When the Vendor field returned record IDs instead of names, I understood why (linked records in Make.com return the raw ID, not the display value) and documented it as a known limitation.

### Q3 — Business Operations

**Partnership landscape:** I asked the AI to research organizations needing optical ground station services globally. The AI provided a list of ~29 organizations with categorization. I then verified each one — checking that the organizations exist, that their described activities are accurate, and that the engagement models I proposed were realistic. For organizations I wasn't sure about, I flagged the uncertainty explicitly in the document (per the PDF's instruction: "If unsure, say so explicitly").

**Competitor analysis:** I asked the AI to research 7 OGS companies with funding, stage, and differentiation. I cross-checked funding amounts against public sources (Crunchbase, company websites). Where I couldn't verify exact numbers, I stated ranges and noted the uncertainty.

**Cost estimation:** I asked the AI to estimate the BoM for a 50cm-class ground station. I then verified component prices against actual vendor catalogs (Thorlabs, Edmund Optics, Physik Instrumente) to make sure the estimates were within the PDF's "2x of reality" tolerance.

**Market sizing:** I asked the AI to build a market size estimation with methodology. I reviewed the assumptions, checked the math, and adjusted the methodology to clearly show both top-down and bottom-up approaches with labeled assumptions.

**Outreach emails:** I asked the AI to draft 3 cold outreach emails. I then edited each one to sound more natural and specific — removing generic phrasing and adding details that showed I understood each organization's actual work.

### Verification and Fact-Checking

Throughout all three questions, I ran dedicated verification passes:

- Asked the AI to cross-check every deliverable against the PDF requirements, line by line
- Scanned all documents for AI-ism language and removed it
- Verified all factual claims (tool pricing, customs rates, component specs, company details) against official sources
- Fixed inconsistencies — for example, the appraisal scorecard example initially included a composite score that didn't match the documented formula
- Ran the code locally to make sure it actually works, not just compiles

---

## Errors the AI Made That I Caught

**Q2 errors:**

1. **dateDifference() function** — The AI initially wrote this for Make.com date calculations. I verified against Make.com's documentation and found it doesn't exist there. Replaced with timestamp subtraction (`(now - date) / 86400000`).

2. **Make.com Free tier limit** — The AI assumed 3+ scenarios could run on Free. I checked Make.com's pricing page: Free tier = 2 active scenarios max. Adjusted the automation plan accordingly.

3. **Filter operator availability** — The AI's initial filter setup didn't account for Make.com's operator categories (Text vs Date vs Number). I found the correct operator ("Earlier than" under Date operators) by scrolling past the Text operators in the actual Make.com interface.

4. **Linked record behavior** — The AI returned Airtable record IDs for linked fields (like Vendor) instead of display names. I understood this is expected behavior in Make.com and documented it.

**Q1 errors:**

5. **RAG pipeline import errors** — The AI's initial Python code had import issues (wrong LangChain module paths, deprecated API calls). I tested the code locally, found the failures, and fixed the imports and API calls.

6. **Note count shortfall** — The AI's initial Obsidian vault had 12-13 notes. The PDF requires 15-20. I identified the gaps (missing physics concepts, missing components, missing references) and created additional notes to meet the requirement.

**Q3 errors:**

7. **Competitor funding numbers** — The AI provided specific dollar amounts for some competitors that I couldn't verify. For example, it cited a funding figure for one company that didn't match what I found on Crunchbase. I replaced unverifiable specific numbers with ranges and noted the uncertainty.

8. **Market size double-counting** — The AI's initial market size estimate double-counted some revenue streams (counting both per-pass and per-GB revenue for the same customers). I caught this during review and restructured the model to use one consistent pricing methodology.

**General errors (all questions):**

9. **Scorecard formula mismatch** — The AI's initial vendor scorecard example had a composite score that didn't match the documented weighted formula. I caught and fixed this during verification.

10. **Empty Airtable fields** — The AI-generated sample data left many fields empty in both the Purchase Requests and Purchase Orders tables. I identified which fields were critical for each record's status and filled them in to make the prototype complete.

---

## Grand Challenge (Part A + Part B)

The Grand Challenge is the mandatory component — it carries the most weight in the evaluation (ML/CV engineering 25%, Business modelling 20%, Execution quality 20%, Systems thinking 15%, Communication 10%, Cost awareness 10%). It has two parts: Part A (cloud segmentation + network availability) and Part B (business model). The PDF explicitly tests whether Part A's results flow directly into Part B's economics model.

I had no prior experience with building financial models, cloud segmentation for satellite imagery, or station network planning. AI was my primary tool. Here is how I used it, what I verified, and what I caught.

### Part A1 — Cloud Segmentation

**What I asked AI to do:**
- Design the U-Net architecture (EfficientNet-B0 encoder, segmentation_models_pytorch)
- Write the 38-Cloud data loader (4 band directories, 16-bit TIFF, geographic scene-ID split)
- Implement training loop (AMP, Dice+Focal loss, cosine annealing, checkpointing)
- Implement evaluation (mIoU, precision, recall, confusion matrix, ECE, thin cirrus FNR)
- Write the 2-page multi-sensor extension write-up

**What I verified and corrected:**
1. **38-Cloud test_gt has no per-patch labels** — I discovered this by reading the dataset docs. Changed to geographic split of training scenes (12 train + 3 val + 3 test).
2. **RGBN → RGB** — AI used 4 bands to preserve NIR. I changed to RGB because EfficientNet-B0 needs 3 channels for ImageNet pretraining. NIR loss is addressed in the write-up.
3. **AMP API** — AI used deprecated `torch.cuda.amp.autocast`. I verified against PyTorch 2.12 docs and updated to `torch.amp.autocast('cuda', ...)`.
4. **Batch size** — AI suggested 32. I tested on RTX 3050 Ti — OOM. Changed to 16.
5. **Evaluation metrics** — AI only computed accuracy. I added mIoU, per-class IoU, F1, ECE, thin cirrus FNR because the PDF requires comprehensive evaluation.

**Real results (not cherry-picked):** Val mIoU 82.2%, Test mIoU 44.0%, Cloud precision 97.6%, Cloud recall 34.6%, ECE 0.27. The 44% test score reflects honest geographic generalization to unseen regions.

### Part A2 — Network Availability & Scheduling

**What I asked AI to do:**
- Design station analysis pipeline (5 Indian locations, monthly clear probabilities, spatial correlation)
- Build network availability model (independent + correlated probability)
- Write pass scheduler with 30-day simulation
- Generate CEO memo

**What I verified and corrected:**
1. **Station locations** — AI proposed generic locations. I selected 5 specific sites: Leh (cold desert, rain shadow), Jodhpur (Thar Desert), Challakere (Qosmic's existing site), Sriharikota (ISRO launch site), Shillong (NE India, unique weather system). Each has a business rationale.
2. **ERA5 vs MERRA-2** — PDF specifies ERA5. CDS API was down for maintenance on May 19. I used MERRA-2 as fallback, documented it in data_source_note.md, and validated with ERA5 sample data when it came back online. Seasonal patterns match.
3. **Pass generation** — I used uniform random pass times (simplified) and documented that real TLE data would improve it.
4. **Scheduler threshold** — Changed from 0.5 to 0.6 after thinking about the operational cost of failed downlinks.

**Results:** Solo station 46% availability. 5-station network >99%. 0 fallbacks in 30 days. 46 conflicts (15%) resolved by routing to next-best station.

### Part B — Business Model

**What I asked AI to do:**
- Design 6-tab spreadsheet structure
- Implement openpyxl generator with formula-based cells
- Build revenue model (3 streams + 2 additive)
- Write Series A memo (10 investors, comparables, funds, risks)
- Research all comparable transactions

**What I verified and corrected (10 real errors):**

| Error | Fix |
|---|---|
| COGS missing — hardware sales had 100% margin | Added COGS line: units × $200K BoM |
| Partner network missing entirely | Added 10 partner stations with $0.20/GB commission |
| ZAPHODOM terminal missing | Added as co-developed product with TakeMe2Space |
| Price too high ($400K) | Reduced to $350K after researching comparables |
| $150K burn vs $30K P&L gap unexplained | Added explanatory note |
| Only 5 investors vs 10 required | Added 5 more (Seraphim, Type One, growX, Starbridge, pi Ventures) |
| Valuation too high ($20-40M) | Adjusted to $15-25M based on actual comparables |
| Flat partner/AWS costs for 5 years | Made per-year growing costs |
| 2 stations in Y1 | Changed to 1 (Challakere first) — documented deviation |
| GB per Pass outdated | Updated to 10 Gbps × 10 min = 750 GB |

**Spreadsheet structure (6 tabs):** Assumptions (40+ blue input cells) → Cloud Model → Unit Economics → 5-Year P&L (5 revenue lines, 6 cost lines, EBITDA) → Breakeven Sensitivity (customers × ARPU) → Investor Summary (auto-updating dashboard).

**Part A → B integration:** Tab 2 uses the same 5 stations and 99.5% network availability from Part A's analysis. Station deployment schedule matches Part A recommendations. CapEx per station ($200K) comes from Part A's BoM research.

---

## What I Did Without AI

Some things I did directly:

- Reading and re-reading the PDF to make sure I understood what's being asked
- Deciding which 2 automations to prioritize for the Make.com Free tier (overdue PO alert and high-value request alert)
- Designing the Airtable table structure and field types based on the schema documents
- Creating the Kanban views and configuring the linked records in Airtable
- Building and testing the Make.com scenarios step by step
- Catching the issue with empty fields in the Airtable Purchase Orders table and deciding what data to fill in
- Making judgment calls on where the AI's output was wrong or incomplete (wrong Make.com function, incorrect Free tier limits, filter operator behavior)
- Deciding the overall structure of each document — what sections to include, what to emphasize, what to leave out
- Filling in the Obsidian notes with specific technical content after verifying the AI's drafts against real physics and vendor specs
- Building the Q3 competitor funding table after cross-checking AI-provided numbers against Crunchbase and company websites
- Editing the Q3 cold outreach emails to sound less generic and more specific to each organization
- Deciding on the market size methodology (top-down + bottom-up) and checking the math independently
- I decided architectural choices (backbone, loss function, split strategy), station locations, all deviation decisions, all error corrections, presentation structure, which investors to include, interview prep strategy.
- I verified every factual claim against primary sources. Every formula in the spreadsheet. Every market data point against annual reports, Crunchbase, Tracxn, fund websites. Every line of code by running it locally.
- Writing this documentation

---

## Summary

I used AI extensively — probably 70-80% of the raw text and code was drafted with AI assistance. But every piece of output was reviewed, verified, and modified by me. The system design decisions, the tool choices, the prioritization trade-offs, and the quality checks were mine. The AI didn't make architectural decisions — it helped me execute them faster and caught things I might have missed.

The best way I can describe it: I treated AI like a very fast junior collaborator who's read every documentation page and never gets tired, but who occasionally hallucinates function names and doesn't always read the fine print. My job was to direct, verify, and decide.
