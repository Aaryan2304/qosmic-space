# Internal Purchase Request Form

## Purpose
Standardised intake form that captures everything the procurement person needs to source a part. Every field exists to answer a specific downstream question — no fluff.

## Form Fields

### Requester Information
| Field | Required | Purpose |
|-------|----------|---------|
| Requester name | Yes | Who to contact for clarifications |
| Department/Team | Yes | Optics, Mechanical, Electronics, Systems |
| Date requested | Yes | Start of procurement clock |
| Required-by date | Yes | Drives vendor selection (fast vs. standard lead time) |
| Budget code | Yes | Cost allocation and spend tracking against quarterly budget |
| Cost centre manager | Yes | Approval routing |

### Part Information
| Field | Required | Purpose |
|-------|----------|---------|
| Part name | Yes | Human-readable identifier — e.g., "Mounting bracket, 90deg, SM1-threaded" |
| Part number | Conditional | For reorders: reference previous PO or vendor P/N. Required if "New/Reorder = Reorder" |
| New part or reorder | Yes | Reorders skip RFQ and spec review — go straight to PO |
| Quantity | Yes | Total units needed |
| Unit of measure | Yes | Pieces, sets, metres, grams |
| Estimated unit cost | Yes | Enables budget check before CTO/CEO review. If unknown, put a range |
| Total estimated cost | Yes | Quantity × estimated unit cost |

### Specifications
| Field | Required | Purpose |
|-------|----------|---------|
| Part type | Yes | Dropdown: Catalog, Custom-machined, Custom-fabricated, COTS assembly |
| If custom-machined: drawing link | Conditional | Link to technical drawing (DXF, STEP, or PDF). Required for machined parts |
| Drawing revision | Conditional | Revision letter/number from the drawing |
| Material specification | Conditional | Required for custom parts: alloy/grade, temper, surface treatment |
| Key dimensions/tolerances | Conditional | Critical dimensions the vendor must hold |
| Surface finish | Conditional | Ra value or equivalent. Required for custom-machined |
| Environmental requirements | No | Operating temperature range, humidity, vacuum compatibility — if applicable |
| Related design document link | No | Link to CAD assembly, optical layout, or system-level drawing showing where the part fits |

### Procurement Preferences
| Field | Required | Purpose |
|-------|----------|---------|
| Preferred vendor(s) | No | If requester has a known supplier. Overridden if RFQ process finds better |
| Vendor qualification level | No | Approved, Pre-qualified, New — speeds up vendor database entry |
| Any past quotes attached | No | Reduces RFQ cycle if vendor has already quoted this part |
| Shipping destination | Yes | Bengaluru lab, remote site, or other |
| Shipping speed | Yes | Standard, Expedited (paid by project budget), Critical (CEO visibility) |

### Attachments
- Technical drawing (PDF or DXF) — required for custom-machined
- Supplier quote (if reorder or preferred vendor) — PDF
- Reference photo or annotated screenshot — optional
- Material cert from previous batch (if reorder with same spec) — optional

## Form Usage Notes
- The form lives in Airtable as a Form view. Submissions create a new record in the Purchase Requests table.
- Required-by date triggers the first automated decision: if lead time for this part type exceeds remaining days, flag for expedited review.
- Estimated total cost determines approval routing (see approval-thresholds.md).
- Drawing link is validated at submission — missing drawing on a custom-machined request returns an error message before submission is accepted.

## Abridged Form (for quick reorders)
When "New/Reorder = Reorder" and the part has been procured within the last 6 months, only these fields are required:
- Requester, Department, Date, Quantity, Required-by date, Budget code
- Part number (auto-populates description, specs, previous vendor, previous unit cost)
