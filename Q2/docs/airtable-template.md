# Airtable Template Design with 5 Sample POs

## Purpose
This document describes the Airtable base structure and populates it with 5 sample POs in various stages to demonstrate the system. The actual Airtable base can be built from this specification.

## Base Structure

### Table 1: Purchase Requests
**Fields:** All fields from purchase-request-form.md
**Views:**
- Form view (for request intake)
- Grid view, filtered by status
- Kanban view grouped by approval status

### Table 2: Vendors
**Fields:** All fields from vendor-database-schema.md
**Views:**
- Grid view (all vendors)
- Kanban view grouped by qualification status
- Gallery view (vendor cards with key metrics)

### Table 3: Purchase Orders
**Fields:**
- PO Number (auto-generated: QOSMIC-PO-YYYY-XXXX)
- Linked to: Purchase Request (one request → one PO)
- Linked to: Vendor
- Status (dropdown: Issued, Acknowledged, In Production, Shipped, In Transit, Customs Hold, Delivered, Inspected, Accepted, Rejected)
- Issue Date
- Promised Ship Date
- Promised Delivery Date
- Actual Ship Date
- Actual Delivery Date
- Total Value (INR)
- Total Value (USD)
- Shipping Terms (FOB, FCA, CIF, EXW)
- Payment Terms
- Tracking Number
- HS Code (for international)
- Estimated Duty (INR)
- Notes
**Views:**
- Kanban view grouped by Status (main working view)
- Calendar view grouped by Promised Delivery Date
- Grid view filtered to "Overdue" (where today > Promised Delivery Date and Status ≠ Delivered)

### Table 4: Inspections
**Fields:**
- Linked to: PO
- Inspection Date
- Inspector Name
- Result (Pass / Fail / Conditional)
- Checklist items (as individual checkbox or rating fields)
- Photos (attachment field)
- Notes
**Views:**
- Grid view, filtered by result

### Table 5: Scorecards
**Fields:**
- Linked to: Vendor
- Quarter (e.g., Q1-2026)
- All 7 metrics (numeric fields)
- Composite Score (formula field)
- Status (formula: Preferred / Approved / Conditional / Probation)
- Notes
**Views:**
- Grid view, sorted by composite score

---

## 5 Sample POs

### PO-1: QOSMIC-PO-2026-0031 — Custom Aluminum Optical Mounts
| Field | Value |
|-------|-------|
| Vendor | Precision Bengaluru Works Pvt. Ltd. (V-2026-0027) |
| Status | **In Transit** |
| Issue Date | 2026-04-01 |
| Promised Ship Date | 2026-04-22 |
| Actual Ship Date | 2026-04-24 (2 days late) |
| Promised Delivery Date | 2026-04-29 |
| Total Value | ₹35,000 ($363) |
| Shipping Terms | FCA Bengaluru |
| Payment Terms | Net 30 |
| Tracking Number | PBW-2026-0441 (local courier) |
| Notes | Prototype run of 5 units. Drawing Rev A. Vendor was 2 days late shipping — within tolerance but noted in scorecard. |

### PO-2: QOSMIC-PO-2026-0032 — SM1 Threaded Lens Tubes (Catalog)
| Field | Value |
|-------|-------|
| Vendor | Thorlabs Inc. (V-2026-0008) |
| Status | **Accepted** |
| Issue Date | 2026-03-15 |
| Promised Ship Date | 2026-03-18 |
| Actual Ship Date | 2026-03-17 (1 day early) |
| Actual Delivery Date | 2026-03-22 |
| Total Value | ₹18,500 ($192) |
| Shipping Terms | DDP Bengaluru (Thorlabs arranged) |
| Payment Terms | Net 30 |
| Tracking Number | UPS-1Z-8842-91 |
| Notes | 20× SM1L10 — 1" lens tubes. Fast-track catalog order. No RFQ. Inspection passed. All 20 units within spec. |

### PO-3: QOSMIC-PO-2026-0033 — Custom Aspheric Lens (Precision Optics)
| Field | Value |
|-------|-------|
| Vendor | Jenoptik AG (V-2026-0014) |
| Status | **Customs Hold** |
| Issue Date | 2026-03-01 |
| Promised Ship Date | 2026-04-15 |
| Actual Ship Date | 2026-04-14 |
| Promised Delivery Date | 2026-04-25 |
| Total Value | ₹1,20,000 ($1,244) |
| HS Code | 9002.11 |
| Estimated Duty | ₹37,200 ($385) |
| Shipping Terms | CIF Bengaluru |
| Payment Terms | Net 45 |
| Tracking Number | DHL-EXP-882011 |
| Notes | Custom aspheric lens, 25.4mm dia, f=75mm, AR coated @ 1064nm. First article. Shipment held at Bengaluru customs since 2026-04-26 — broker requested additional documentation (end-user certificate). Expected clearance: 2026-05-03. CEO notified. |

### PO-4: QOSMIC-PO-2026-0034 — PCB Assembly (Electronics)
| Field | Value |
|-------|-------|
| Vendor | JLCPCB Co., Ltd. (V-2026-0001) |
| Status | **Inspected** |
| Issue Date | 2026-04-10 |
| Promised Ship Date | 2026-04-18 |
| Actual Ship Date | 2026-04-18 |
| Actual Delivery Date | 2026-04-25 |
| Total Value | ₹8,200 ($85) |
| Shipping Terms | DDP Bengaluru |
| Payment Terms | T/T (prepaid) |
| Tracking Number | 4PX-2026-CN-9912 |
| Notes | 10× photodetector interface boards, 4-layer FR4, SMT assembled. Inspection completed 2026-04-26. 9 boards passed. 1 board failed — solder bridge on U3. Rejection notice sent to JLCPCB. Replacement board to be shipped separately. |

### PO-5: QOSMIC-PO-2026-0035 — Stainless Steel Fasteners (M6 Kit)
| Field | Value |
|-------|-------|
| Vendor | Precision Bengaluru Works Pvt. Ltd. (V-2026-0027) |
| Status | **Issued** |
| Issue Date | 2026-05-14 |
| Promised Ship Date | 2026-05-21 |
| Total Value | ₹2,800 ($29) |
| Shipping Terms | EXW Bengaluru |
| Payment Terms | Net 30 |
| Notes | Self-approved (under ₹5,000). M6×12mm socket head cap screws, stainless steel A2-70, 50 pcs. Reorder from previous PO. No RFQ. Awaiting vendor acknowledgement. |

---

## Kanban Board View (as of 2026-05-20)

| Issued | Acknowledged | In Production | Shipped | In Transit | Delivered | Inspected | Accepted | Rejected |
|--------|-------------|---------------|---------|------------|-----------|-----------|----------|----------|
| PO-0035 | | | | PO-0031 | | PO-0034 | PO-0032 | |
| | | | | | PO-0033 (Customs) | | | |

## Dashboard Metrics (as of 2026-05-20)

| Metric | Value |
|--------|-------|
| Active POs | 5 |
| Overdue POs | 1 (PO-0033, customs hold) |
| Total value of active POs | ₹1,84,500 (~$1,912) |
| Vendors engaged | 3 |
| Inspections pending | 1 (PO-0033, awaiting customs clearance) |
| Rejections this month | 1 (PO-0034, 1 of 10 boards) |

## How to Build This in Airtable

1. Create a new Airtable base called "QOSMIC Procurement"
2. Create the 5 tables listed above with the specified fields
3. Link the tables: Purchase Requests → Purchase Orders → Vendors, Inspections → Purchase Orders, Scorecards → Vendors
4. Create the views listed for each table
5. Import the 5 sample POs above
6. Set up the 2 Make.com Automations from tool-stack.md (2 live on Free tier, 1 planned for Core upgrade)
7. Share the base with the procurement person (edit access) and the CTO/CEO (comment access for approvals)

**Time to build: 2-3 hours** for someone familiar with Airtable. The free plan is sufficient.
