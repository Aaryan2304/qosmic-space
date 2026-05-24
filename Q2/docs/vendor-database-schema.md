# Vendor Database Schema — Q2 Deliverable

## Purpose

This document defines the schema for QOSMIC's vendor database, used to track, evaluate, and manage all suppliers across our optical ground station supply chain. The database covers prototyping shops, precision optics manufacturers, local fabricators, and specialty photonics vendors.

---

## Schema Definition

| Field | Type | Example | Purpose |
|---|---|---|---|
| `vendor_id` | UUID / auto-increment | `V-2026-0042` | Unique internal identifier for the vendor record |
| `company_name` | String (required) | `JLCPCB Co., Ltd.` | Legal or commonly used company name |
| `primary_contact` | String | `Wei Zhang` | Name of the main point of contact |
| `contact_phone` | String (E.164) | `+86-755-2394-1122` | Direct phone number for the primary contact |
| `contact_email` | String (email) | `wei.zhang@jlcpcb.com` | Direct email for the primary contact |
| `vendor_type` | Enum | `prototyping` | Category: `prototyping`, `production`, `local_fabrication`, `specialty` |
| `country` | String (ISO 3166-1) | `CN` | Country where the vendor is headquartered or primarily operates |
| `capabilities` | Array[String] | `["CNC", "electronics", "assembly"]` | List of manufacturing/service capabilities. Valid values: `CNC`, `precision_optics`, `electronics`, `coatings`, `assembly` |
| `on_time_delivery_rate` | Float (0–100) | `94.5` | Percentage of orders delivered on or over the last 12 months |
| `quality_rejection_rate` | Float (0–100) | `2.1` | Percentage of received lots rejected during incoming QC over the last 12 months |
| `avg_lead_time_days` | Integer | `18` | Average calendar days from PO issuance to delivery, rolling 12-month window |
| `payment_terms` | Enum | `net_30` | Accepted payment terms: `net_30`, `net_45`, `LC` (Letter of Credit), `T/T` (Telegraphic Transfer) |
| `moq_standard_parts` | Integer | `50` | Minimum order quantity for standard/catalog parts (units) |
| `moq_custom_parts` | Integer | `5` | Minimum order quantity for custom-fabricated parts (units) |
| `qualification_status` | Enum | `approved` | Current qualification state: `approved`, `conditional` (probation), `new` (pending evaluation), `inactive` |
| `notes` | Text (free-form) | `Responds well to RFQs under $5k. Escalate to sales mgr for >$20k.` | Free-text notes on relationship, escalation paths, known issues |
| `last_interaction_date` | Date (ISO 8601) | `2026-04-12` | Date of last meaningful contact (PO, email, call, audit) |
| `total_spend_to_date` | Decimal (USD) | `48750.00` | Cumulative spend with this vendor in USD since first engagement |

---

## Capability Tags — Definitions

| Capability | Description |
|---|---|
| `CNC` | CNC milling, turning, and multi-axis machining of metals and polymers |
| `precision_optics` | Fabrication and testing of lenses, mirrors, prisms, and optical assemblies to tight tolerances |
| `electronics` | PCB fabrication, SMT assembly, and electronic component sourcing |
| `coatings` | Thin-film deposition (AR, HR, dielectric, metallic coatings) on optical and mechanical substrates |
| `assembly` | Mechanical and opto-mechanical assembly, integration, and alignment |

---

## Qualification Status — Definitions

| Status | Meaning |
|---|---|
| `approved` | Fully qualified. Can receive POs without additional review. |
| `conditional` | On probation. Limited PO value or requires QA sign-off per order. |
| `new` | Pending evaluation. No POs issued yet; undergoing capability review and sample qualification. |
| `inactive` | No longer used. Historical data retained but no new POs to be issued. |

---

## Sample Vendor Entries

### Vendor 1 — JLCPCB Co., Ltd.

| Field | Value |
|---|---|
| `vendor_id` | `V-2026-0001` |
| `company_name` | JLCPCB Co., Ltd. |
| `primary_contact` | Wei Zhang |
| `contact_phone` | `+86-755-2394-1122` |
| `contact_email` | `wei.zhang@jlcpcb.com` |
| `vendor_type` | `prototyping` |
| `country` | `CN` |
| `capabilities` | `["electronics", "assembly"]` |
| `on_time_delivery_rate` | `96.2` |
| `quality_rejection_rate` | `1.4` |
| `avg_lead_time_days` | `12` |
| `payment_terms` | `T/T` |
| `moq_standard_parts` | `5` |
| `moq_custom_parts` | `5` |
| `qualification_status` | `approved` |
| `notes` | `Primary PCB supplier for all prototyping runs. Turnkey SMT assembly consistently reliable. Use for boards up to 4-layer, 0.4mm pitch. For HDI or RF substrates, route through Vendor 2 instead.` |
| `last_interaction_date` | `2026-05-02` |
| `total_spend_to_date` | `31200.00` |

---

### Vendor 2 — Jenoptik AG (Optical Systems Division)

| Field | Value |
|---|---|
| `vendor_id` | `V-2026-0014` |
| `company_name` | Jenoptik AG |
| `primary_contact` | Dr. Markus Reinhardt |
| `contact_phone` | `+49-3641-65-2201` |
| `contact_email` | `markus.reinhardt@jenoptik.com` |
| `vendor_type` | `production` |
| `country` | `DE` |
| `capabilities` | `["precision_optics", "coatings", "assembly"]` |
| `on_time_delivery_rate` | `88.7` |
| `quality_rejection_rate` | `0.8` |
| `avg_lead_time_days` | `45` |
| `payment_terms` | `net_45` |
| `moq_standard_parts` | `10` |
| `moq_custom_parts` | `1` |
| `qualification_status` | `approved` |
| `notes` | `Supplies custom aspheric lenses and beam-expander assemblies for the OGS-1 telescope train. Lead times spike in Q3 (German factory shutdown). Place orders by June 1 for Q3 delivery. Quality is excellent — wavefront error consistently within spec.` |
| `last_interaction_date` | `2026-04-28` |
| `total_spend_to_date` | `127500.00` |

---

### Vendor 3 — Precision Bengaluru Works Pvt. Ltd.

| Field | Value |
|---|---|
| `vendor_id` | `V-2026-0027` |
| `company_name` | Precision Bengaluru Works Pvt. Ltd. |
| `primary_contact` | Arvind Krishnamurthy |
| `contact_phone` | `+91-80-4123-8800` |
| `contact_email` | `arvind@pbw-machine.com` |
| `vendor_type` | `local_fabrication` |
| `country` | `IN` |
| `capabilities` | `["CNC", "assembly"]` |
| `on_time_delivery_rate` | `82.3` |
| `quality_rejection_rate` | `4.6` |
| `avg_lead_time_days` | `21` |
| `payment_terms` | `net_30` |
| `moq_standard_parts` | `25` |
| `moq_custom_parts` | `3` |
| `qualification_status` | `conditional` |
| `notes` | `Bengaluru-based machine shop handling custom mounting brackets and adapter plates. On-time delivery has been inconsistent — currently on a 90-day improvement plan. QA rejection rate above threshold; working with their team on GD&T training. Good pricing and responsive to design feedback.` |
| `last_interaction_date` | `2026-05-10` |
| `total_spend_to_date` | `14800.00` |

---

### Vendor 4 — Thorlabs Inc.

| Field | Value |
|---|---|
| `vendor_id` | `V-2026-0008` |
| `company_name` | Thorlabs Inc. |
| `primary_contact` | Sarah Mitchell |
| `contact_phone` | `+1-973-579-7227` |
| `contact_email` | `s.mitchell@thorlabs.com` |
| `vendor_type` | `specialty` |
| `country` | `US` |
| `capabilities` | `["precision_optics", "electronics", "coatings", "assembly"]` |
| `on_time_delivery_rate` | `97.1` |
| `quality_rejection_rate` | `0.3` |
| `avg_lead_time_days` | `7` |
| `payment_terms` | `net_30` |
| `moq_standard_parts` | `1` |
| `moq_custom_parts` | `1` |
| `qualification_status` | `approved` |
| `notes` | `Go-to catalog vendor for off-the-shelf optics, optomechanical components, photodetectors, and fiber assemblies. Same-week shipping on most stock items. Custom waveplates and specialty fibers available with 3–4 week lead time. No MOQ on any line item — ideal for lab and prototype builds.` |
| `last_interaction_date` | `2026-05-14` |
| `total_spend_to_date` | `62300.00` |

---

## Notes on Implementation

- All monetary values are stored in USD. For vendors invoicing in other currencies (EUR, CNY, INR), the `total_spend_to_date` should be converted at the prevailing rate on the date of each transaction and summed.
- The `on_time_delivery_rate` and `quality_rejection_rate` should be recalculated monthly from the PO and receiving logs.
- Vendors with `qualification_status` of `conditional` should be reviewed quarterly. If metrics do not improve within two review cycles, status should be changed to `inactive`.
- The `last_interaction_date` field is critical for relationship management — any vendor with no interaction in 180+ days should be flagged for re-engagement or archival.
