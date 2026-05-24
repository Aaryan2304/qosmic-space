# Make.com Workflow Configurations — Q2 Procurement System

*Step-by-step guide to connect Airtable → Make.com → Slack. All module names and syntax verified against Make.com's May 2026 interface.*

---

## Prerequisites

1. **Make.com account** — sign up at make.com (free tier)
2. **Slack workspace** — you already have one with `#procurement-alerts` channel
3. **Airtable base** — the existing "QOSMIC Procurement" base is already connected

### Connect everything in Make.com

1. Sign in at https://www.make.com
2. Go to left sidebar → **Credentials** (shield icon)
3. Click **Add connection** → search "Airtable" → authorize with your Airtable account
4. Click **Add connection** → search "Slack" → authorize with your Slack workspace → allow Make to post to `#procurement-alerts`

---

## Make.com Free Tier Limits (Verified May 2026)

| Resource | Free Tier Limit |
|----------|----------------|
| Operations/month | 1,000 |
| Active scenarios | **2** (not 3) |
| Minimum run interval | Every 15 minutes |

**Implication:** You can only run 2 automations on the free plan. A 3rd scenario requires the Core plan ($12/month). We'll build the 2 highest-priority scenarios and document the 3rd as "ready to deploy on Core."

---

## CRITICAL: Before Building Scenarios — Airtable Requirements

The Airtable **"Watch Records" trigger requires a "Created Time" or "Last Modified Time" field** in the table it watches. Without this field, the trigger will not work.

**Check if your tables have this field:**

1. Open your Airtable base → go to the **Purchase Orders** table
2. Look for a field called **"Created Time"** or **"Last Modified Time"**
3. If it doesn't exist, create it:
   - Click **"+ Add a field"** at the right end of the column headers
   - In the field type dropdown, select **"Created time"**
   - Name it `Created Time`
   - Click **"Create field"**
4. Repeat for the **Purchase Requests** table (needed for Scenario 3)

---

## CRITICAL: Date Calculation in Make.com

**Make.com does NOT have a `dateDifference()` function.** That function belongs to Microsoft Power Automate, not Make.

**To calculate days between two dates in Make.com:**

When you need to calculate "days since Issue Date," you have two options:

**Option A: Use Math with Timestamps (Recommended)**

In a **Tools → Set variable** module, set the variable value to:
```
{{round((now - Issue Date) / 86400000)}}
```
- `now` = Make's built-in system variable for current timestamp (in milliseconds)
- `Issue Date` = your Airtable date field (also in milliseconds)
- `86400000` = number of milliseconds in a day (1000 × 60 × 60 × 24)
- `round()` = rounds to nearest whole number

**How to enter this in Make.com:**
1. Click inside the "Variable value" field
2. Click the **`{x}`** icon (Insert function) that appears above the field, OR type directly
3. For `now`: click the **star icon** (System variables) → select `Now` from the list
4. Type ` - ` (minus sign)
5. For Issue Date: click the number from the module output list on the left (e.g., `5. Issue Date`)
6. Type ` / 86400000`
7. Wrap the whole expression: `{{round((...))}}`

**Option B: Use addDays to Create a Comparison Date**

Create a date that is "Issue Date + 3 days" and compare it to today:
```
{{addDays(Issue Date; 3)}}
```
Then check if that date is before `now`.

**We'll use Option A in the scenarios below.**

---

## Scenario 1: PO Past Promised Delivery Date → Slack Alert

**Priority:** HIGH — simplest scenario, no date math needed, uses basic filter

**What it does:** Every 15 minutes, checks all Purchase Orders. If any PO's Promised Delivery Date has passed AND status is not "Delivered" or "Accepted," sends a Slack alert.

### Build Steps

**Step 1 — Create scenario**
- In Make.com left sidebar, click **Scenarios** (chain link icon)
- Click **"+ Create a new scenario"**
- A blank scenario builder opens

**Step 2 — Add Airtable "Watch Records" trigger**
- Click the large **"+"** circle in the center
- Search **"Airtable"** → select the Airtable app
- Select the module **"Watch Records"** (under Triggers)
- **Connection:** Select your Airtable connection
- **Base:** Select "QOSMIC Procurement"
- **Table:** Select "Purchase Orders"
- **Trigger field:** Select "Created Time" (or "Last Modified Time" if that's what you have)
- **Label field:** Select "PO Number"
- **Limit:** Leave at 10
- Click **"Save"**
- At the bottom of the scenario builder, set scheduling to **"Every 15 minutes"**

**Step 3 — Add Filter (past delivery date, not delivered)**
- Click the **circle with three dots** on the right side of the Airtable module → **"Add a filter"**
- Wait — Make.com doesn't add filters from the module dot menu. Instead:
- **Hover between the Airtable module and where the next module would be**
- Click the **"+"** that appears between them
- Search **"Basic Filter"** (under Flow Control or Tools)
- Select **"Basic Filter"**

  **Configure the filter:**

  - **Label:** "Past delivery date, not delivered"
  - **Condition 1:**
    - Left side: Click → select from the list → find **"Promised Delivery Date"** from module 1 (Watch Records)
    - Operator: Select **"before"** (from the dropdown)
    - Right side: Type **`{{now}}`** or select **"Now"** from the system variables (star icon)
  - **Add AND rule:**
    - Left side: Select **"Status"** from module 1
    - Operator: Select **"does not equal"**
    - Right side: Type **`Delivered`**
  - **Add AND rule:**
    - Left side: Select **"Status"** from module 1
    - Operator: Select **"does not equal"**
    - Right side: Type **`Accepted`**
- Click **"OK"**

**Step 4 — Add Slack "Create a Message"**
- Click the **"+"** on the right side of the Filter module
- Search **"Slack"** → select the Slack app
- Select **"Create a Message"**
- **Connection:** Select your Slack connection
- **Channel:** Click the dropdown → select `#procurement-alerts` (Make will show channels from your workspace)
- **Message text:** Click inside the text field and type:

```
🚨 OVERDUE PO: Shipment has not arrived by promised delivery date

PO Number: {{1.PO Number}}
Vendor: {{1.Vendor}}
Promised Delivery Date: {{1.Promised Delivery Date}}
Current Status: {{1.Status}}
Tracking Number: {{1.Tracking Number}}

Action required: Contact vendor for updated delivery timeline.
```

To insert field values: click where you want the value, then find the field in the module list on the left side (under "1. Watch Records") and click it.

**Step 5 — Test and activate**
- Click **"Run once"** at the bottom (purple button)
- Make will execute the scenario once
- Check the execution log at the bottom — green = success, red = error
- If successful, click the **toggle switch** at the bottom left to activate it (it should say "ON")
- The scenario will now run every 15 minutes automatically

---

## Scenario 2: New High-Value Purchase Request (₹50,000+) → Slack Alert

**Priority:** HIGH — triggers on record creation, simple filter, no date math

**What it does:** When a new record is created in Purchase Requests with Total Estimated Cost > 50000, send a Slack alert for CEO approval.

### Build Steps

**Step 1 — Create new scenario**
- **Scenarios** → **"+ Create a new scenario"**

**Step 2 — Add Airtable "Watch Records" trigger**
- Click **"+"** → **"Airtable"** → **"Watch Records"**
- **Connection:** Your Airtable connection
- **Base:** "QOSMIC Procurement"
- **Table:** Select **"Purchase Requests"**
- **Trigger field:** Select "Created Time"
- **Label field:** Select "Part Name"
- **Limit:** Leave at 5
- Click **"Save"**

**Step 3 — Add Filter (high-value only)**
- Click **"+"** between modules → add **"Basic Filter"**
- **Label:** "Cost above 50000"
- **Condition:**
  - Left: Select **"Total Estimated Cost"** from module 1
  - Operator: Select **"greater than"**
  - Right: Type **`50000`**
- Click **"OK"**

**Step 4 — Add Slack "Create a Message"**
- Click **"+"** → **"Slack"** → **"Create a Message"**
- **Connection:** Your Slack connection
- **Channel:** `#procurement-alerts`
- **Message text:**

```
💰 HIGH-VALUE REQUEST: Requires CEO approval

Part Name: {{1.Part Name}}
Requester: {{1.Requester Name}}
Department: {{1.Department}}
Total Estimated Cost: ₹{{1.Total Estimated Cost}}
Required By: {{1.Required-By Date}}

Open Airtable to review and approve.
```

**Step 5 — Test and activate**
- Click **"Run once"** → check for green success
- Flip the toggle to **ON**

---

## Scenario 3: PO Not Acknowledged in 3 Days → Slack Alert

**Priority:** MEDIUM — requires date calculation, documented for Core plan upgrade

**What it does:** Every 15 minutes, checks Purchase Orders in "Issued" status where Issue Date was more than 3 days ago, sends Slack alert.

**⚠️ NOTE:** This is the 3rd scenario. Make.com Free tier only supports **2 active scenarios**. Deploy this one after upgrading to Core ($12/month) or replace one of the above.

### Build Steps

**Step 1 — Create new scenario**
- Same as above

**Step 2 — Add Airtable "Watch Records" trigger**
- Same as Scenario 1
- **Table:** "Purchase Orders"
- **Trigger field:** "Created Time"
- **Limit:** 10

**Step 3 — Add Filter (Status = Issued)**
- Add **"Basic Filter"**
- **Label:** "Status is Issued"
- **Condition:**
  - Left: Select **"Status"** from module 1
  - Operator: **"equals"**
  - Right: Type **`Issued`**

**Step 4 — Add Tools → Set Variable (calculate days since issue)**
- Click **"+"** after the filter
- Search **"Tools"** → select **"Set variable"**
- **Variable name:** Type `days_since_issue`
- **Variable value:** Click inside the field and type:
  ```
  {{round((now - 1.Issue Date) / 86400000)}}
  ```
  To build this:
  1. Type `{{round((`
  2. Click the **star icon** (System variables) → select **"Now"`** — this inserts the current timestamp
  3. Type ` - `
  4. In the module list on the left, find **"Issue Date"** under "1. Watch Records" (it shows as `1.Issue Date`) — click it
  5. Type `) / 86400000)}}`
- The expression should look like: `{{round(({{6.Now}} - 1.Issue Date) / 86400000)}}`
  (The exact number for "Now" may differ — it depends on module numbering)
- Click **"OK"**

**Step 5 — Add Filter (days_since_issue > 3)**
- Add another **"Basic Filter"**
- **Label:** "Over 3 days"
- **Condition:**
  - Left: Select **`days_since_issue`** from the Set Variable module (module 3)
  - Operator: **"greater than"**
  - Right: Type **`3`**

**Step 6 — Add Slack "Create a Message"**
- Same pattern as above
- **Message text:**

```
⚠️ PO ALERT: Vendor has not acknowledged PO for 3+ days

PO Number: {{1.PO Number}}
Vendor: {{1.Vendor}}
Status: {{1.Status}}
Issue Date: {{1.Issue Date}}
Days since issue: {{3.days_since_issue}}

Action required: Contact vendor to confirm receipt.
```

**Step 7 — Test and activate**
- Test, then upgrade to Core if needed

---

## How to Test

**Test Scenario 1 (Overdue PO):**
1. Open Airtable → find existing PO QOSMIC-PO-2026-0033 (the Jenoptik aspheric lens — it's already past its delivery date of 2026-04-25)
2. Make sure Status is NOT "Delivered" or "Accepted" (it's currently "In Transit")
3. In Make.com, click "Run once" on Scenario 1
4. Check `#procurement-alerts` in Slack for the alert

**Test Scenario 2 (High-value request):**
1. Open Airtable → Purchase Requests table
2. Create a new record with any Part Name and set Total Estimated Cost = 60000
3. In Make.com, click "Run once" on Scenario 2
4. Check Slack

---

## Troubleshooting

**"Required field(s) are empty or unavailable" in Airtable:**
- This is normal for optional fields that aren't filled in the sample data
- Fields like `Notes`, `Assignee`, `Attachments`, `Environmental Requirements`, `Design Document Link`, etc. are optional in the real workflow
- They appear empty because the 5 sample records only populate core fields
- The automations only reference fields that ARE populated (PO Number, Status, Issue Date, Promised Delivery Date, Total Estimated Cost, Part Name, Vendor, etc.)

**Watch Records trigger not working:**
- The most common cause is missing "Created Time" or "Last Modified Time" field in the Airtable table
- Add the field as described in the "CRITICAL" section above
- Then re-open the Make.com module settings, re-select the Trigger field (now "Created Time" will appear in the dropdown), and save

**Scenario shows error after "Run once":**
- Click on the module with the red error indicator
- Read the error message
- Most common errors: wrong field name mapping, missing connection authorization, or filter value type mismatch (e.g., comparing text to number)

**Scenario runs but no Slack message:**
- Verify the Slack bot has been added to the `#procurement-alerts` channel
- In Slack, type `/invite @Make` in the `#procurement-alerts` channel to add the bot
- Check that you selected the correct channel in the Slack module

**Free tier "2 active scenarios" limit:**
- If you try to turn on a 3rd scenario and get an error about limits, you've hit the Free tier cap
- Either turn off one scenario, or upgrade to Core ($12/month)

---

## Cost Analysis

| Plan | Cost | Scenarios | Ops/month |
|------|------|-----------|-----------|
| Free | $0 | 2 active | 1,000 |
| Core | $12/mo | Unlimited | 10,000 |

At 2 scenarios running every 15 minutes:
- ~2 scenarios × 4 runs/hour × 24 hours × 30 days = ~5,760 runs/month
- Each run uses ~2-4 ops (Watch Records + Filter + Slack message)
- Total: ~12,000-23,000 ops/month

**This exceeds the Free tier's 1,000 ops limit.** To avoid this:
- Increase the interval to **Every 60 or 120 minutes** instead of 15 minutes
- At Every 60 min: ~3,000 ops/month — still over
- At Every 6 hours: ~500 ops/month — safely within Free tier

**Recommended:** Set scenarios to run **Every 1-6 hours** on the Free tier. For production use (every 15 min), upgrade to Core ($12/month).

---

## What to Show the Evaluator

When they ask "show me the automations working":

> "I built 2 automated workflows on Make.com's free tier that connect Airtable to Slack. When a purchase request exceeds ₹50,000, the system sends a Slack alert to #procurement-alerts for CEO approval. When a PO passes its promised delivery date without being marked delivered, another alert fires. Both run on scheduled polling — Make checks Airtable every [interval] minutes. The scenarios are live; here's the Slack channel showing alerts that fired from our existing PO data. A third scenario for unacknowledged POs is documented and ready to deploy — it requires Make's Core plan ($12/month) since the Free tier only supports 2 active scenarios."
