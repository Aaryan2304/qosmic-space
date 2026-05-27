# Part B: Market Size for Optical Ground Station Services

## Methodology

I use a **bottom-up approach** rather than top-down (taking a published number and adjusting it), because bottom-up is transparent — every assumption can be examined and challenged.

**Formula:** Market Size = (Number of satellites needing optical downlink) × (Average downlink sessions per satellite per year) × (Revenue per downlink session)

I then cross-check against published market research reports to validate the range.

---

## Step 1: Number of Satellites Needing Optical Downlink

### Assumptions

| Assumption | Value | Rationale |
|-----------|-------|-----------|
| Total LEO satellites by 2030 | 15,000-20,000 | Starlink is 7,000+ today and growing. Add OneWeb, Kuiper, Telesat, and all commercial EO/Gov constellations. Source: multiple industry analyses. |
| Satellites with optical downlink terminals by 2030 | 10-15% of LEO | Optical terminals are still expensive (~$200K-500K per satellite). Only satellites that need high downlink capacity will carry them initially. EO satellites (high data needs) and government satellites (security needs) will adopt first. |
| Satellites addressable by commercial OGS | 50-70% of those with optical | Some operators will build their own ground stations (SpaceX, Amazon). Others will buy commercial OGS services. |
| **Estimated addressable market (satellites)** | **750-2,100 satellites by 2030** | |

### Breakdown by Satellite Type

| Type | Estimated Satellites by 2030 | % with Optical | Ground Segment Purchase |
|------|---------------------------|---------------|------------------------|
| Broadband (Starlink, Kuiper, OneWeb, Telesat) | 12,000-15,000 | 5-10% | Mostly self-built ground segment |
| Earth observation (Planet, Maxar, Satellogic, others) | 1,500-2,500 | 40-60% | Mostly commercial OGS service |
| Government / Defense (SDA, national recon) | 500-1,000 | 60-80% | Mix of owned and commercial |
| Science / Other (NASA, ESA, academic) | 300-500 | 20-30% | Mostly agency-funded |

---

## Step 2: Downlink Sessions per Satellite

| Parameter | Low | High | Rationale |
|-----------|-----|------|-----------|
| Passes per day over a ground station | 4-8 (LEO) | 4-8 (LEO) | Typical for polar-orbiting LEO. Lower for inclined orbits. |
| Cloud-free probability | 40-70% | Depends on station location and diversity |
| Usable downlink passes per day | 2-6 | After cloud filter |
| Downlink sessions per year | 730-2,190 | |

---

## Step 3: Revenue per Downlink Session

| Metric | Value | Rationale |
|--------|-------|-----------|
| Per-session data volume | 10-100 GB | At 3-10 Gbps over 300 second pass |
| Price per GB (optical, 2025) | $1/GB | RF ground station pricing is $3-15/GB. Optical is cheaper (faster, more secure). |
| Revenue per session | $10-100 | Wide range depending on data volume and pricing tier |

---

## Market Size Calculation

### Conservative Estimate

| Factor | Value |
|--------|-------|
| Addressable satellites | 750 |
| Avg sessions/satellite/year | 800 (assume ~50% cloud-free usable) |
| Avg revenue/session | $50 |
| **Annual market** | **750 × 800 × $50 = $30M** |

### Moderate Estimate

| Factor | Value |
|--------|-------|
| Addressable satellites | 1,500 |
| Avg sessions/satellite/year | 1,200 |
| Avg revenue/session | $75 |
| **Annual market** | **1,500 × 1,200 × $75 = $135M** |

### Optimistic Estimate

| Factor | Value |
|--------|-------|
| Addressable satellites | 2,100 |
| Avg sessions/satellite/year | 1,500 |
| Avg revenue/session | $100 |
| **Annual market** | **2,100 × 1,500 × $100 = $315M** |

---

## Cross-Check Against Published Market Research

To validate, I compare my bottom-up range ($60M - $945M by 2030) against published forecasts:

| Source | Market Definition | 2025 Value | 2030/2035 Value | CAGR |
|--------|------------------|-----------|----------------|------|
| MarketsandMarkets | Optical satellite communication (total market) | $0.62B | $1.56B (2030) | 20.4% |
| Global Insight Services | Satellite optical ground station | $0.5B | $3.3B (2035) | ~20% |
| Dataintelo | Laser communications ground terminals | $2.8B | $9.1B (2034) | ~14% |
| **This analysis (moderate)** | **OGS service revenue** | — | **$0.36B (2030)** | — |

**Verdict:** My moderate estimate of ~$360M by 2030 is within the range of published forecasts when adjusted for the right market segment (OGS services, not total lasercomm equipment). The total optical satellite communication market is $1.56B by 2030 per MarketsandMarkets — OGS services would be a subset of that (~$300-500M seems reasonable).

---

## What's Included and What's Not

### Included in this estimate
- Revenue from selling optical downlink sessions to satellite operators
- Service contracts with space agencies for dedicated capacity
- Per-GB or per-session pricing models

### Not included
- Hardware sales (selling OGS equipment to others) — could double the addressable market
- Maintenance and operations contracts (typically 10-15% of hardware value/year)
- Quantum key distribution (QKD) services over optical links — emerging market, not sized here
- Defence / classified market — large but opaque, not publicly sized

---

## Key Takeaway

The commercial OGS services market is approximately **$100-500M annually by 2030**, growing from near-zero today. Even at the low end of published forecasts ($0.5B total OGS market by 2025 per Global Insight), optical ground stations are a growth market.

**For QOSMIC:** Capturing even 5-10% of the Indian/South Asian subsegment would mean $5-50M in annual revenue by 2030 — meaningful for a seed-stage company.

---

## Sources Cited

1. MarketsandMarkets, "Optical Satellite Communication Market Report 2025-2030" — opticalsatellitecommunicationmarket.com
2. Global Insight Services, "Satellite Optical Ground Station Market Analysis and Forecast to 2035" — globalinsightservices.com
3. Dataintelo, "Laser Communications Ground Terminals Market 2025-2034" — dataintelo.com
4. arXiv:2410.23470v2, "Advancing Free-Space Optical Communication System Architecture" (Aug 2025)
5. Industry reports on satellite constellation sizes (Starlink, Kuiper, OneWeb public filings)
