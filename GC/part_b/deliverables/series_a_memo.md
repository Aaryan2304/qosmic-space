# Series A Readiness Memo: QOSMIC SPACE

**Date:** May 2026 | **Stage:** Seed → Series A

---

## 1. Where We Are

QOSMIC SPACE is building the optical ground segment for the satellite industry. Our thesis: satellites are collecting far more data than RF can move. Over 100,000 satellites are expected to launch this decade, generating petabytes daily, but Ka-band RF downlinks still max out at 1–2 Gbps — a standard that hasn't meaningfully changed in 30 years. Over half that data never reaches Earth. We solve this with laser-based optical ground stations that deliver 10–100 Gbps per pass at $1/GB.

We have two products. **ARGUS** is our optical ground station — a 0.5m–1.0m aperture system at 1550nm C-band with sub-arcsecond tracking, deployable in under 6 months. **ZAPHOD** is our satellite optical terminal — a CubeSat–SmallSat compatible laser communications payload under 3 kg, co-developed with TakeMe2Space. Together they form what Accel Atoms describes as "India's only full-stack optical comms platform."

We operate an optical ground station network marketplace at stations.qosmic.space — a real-time booking platform that connects satellite operators to available optical ground station capacity globally. The network currently has 11 stations online across North America, Europe, Asia, Oceania, and Africa. One station (OGS011) is our own ARGUS unit; the other 10 are partner stations operated by NASA JPL (Table Mountain Facility, California), the European Space Agency, German Aerospace Center (DLR), Australian space tracking facilities, Japanese and UAE quantum communications facilities, Norwegian Arctic facilities, and others. Pricing is transparent: $1/GB at ~2.5 Gbps per station, with availability visible and bookable in real time. The platform is built on AWS with support for 1550nm, 810nm, and 1064nm wavelengths.

Our hardware is validated at TRL 6 with a 5+ km optical link in the field. The team published a peer-reviewed link budget model (arXiv:2507.20908, July 2025) providing a probabilistic framework for atmospheric effects on LEO optical links. We are backed by ARTPARK, Accel (through Accel Atoms), Prosus, and South Park Commons.

**Team:**
- **Shreyaans Jain** — Founder & CEO
- **Dr. Rohit Ramakrishnan** — Co-Founder & CTO (C V Raman Post-Doctoral Fellow)
- **Prof. Aloke Kumar** — Co-founder / Faculty Advisor

### Market Context

The global satellite ground station market was valued at USD 40.99 billion in 2025 and is projected to reach USD 82.72 billion by 2030 (MarketsandMarkets, 2025). Within this, optical (laser) satellite communication — our specific technology layer — was valued at USD 0.62 billion in 2025 and is forecast to reach USD 1.56 billion by 2030 at 20.4% CAGR (MarketsandMarkets, 2025). The LEO satellite communication market that feeds both is valued at USD 9.4 billion in 2025 with a 17.1% CAGR through 2034 (Dataintelo, 2025).

India's space sector has undergone structural reform. 100% FDI is now permitted in satellite manufacturing, ground stations, and data products (India Briefing, 2025). IN-SPACe has issued ground station establishment authorisations. The government's space budget tripled over the past decade from ₹5,615 crore in 2013-14 to ₹13,416 crore in 2025-26.

### Competitive Landscape

**KSAT** (Kongsberg Satellite Services) is the world's largest polar-orbit ground station operator — NOK 2,236 million (~USD 210 million) revenue in 2024 from 28 stations and 522 employees, with 77% of revenue from international customers (Space Norway Annual Report 2024). They operate a similar booking model but for RF ground stations. They are 60 years old and state-owned.

**Mynaric**, the German optical terminal manufacturer, was acquired by Rocket Lab for USD 155 million in April 2026 after entering restructuring. The acquisition is a clear exit signal for the optical comms space: incumbents see optical as strategically critical, but manufacturing at scale is difficult.

**Skyloom** raised USD 52.9M and delivered 90 terminals for U.S. Space Development Agency missions before being acquired by IonQ in 2026. They were terminal-focused, not network/platform-focused.

QOSMIC is differentiated by its full-stack approach (terminals + ground stations + booking platform) and its India cost base, which allows pricing at $1/GB versus $3–17/GB for RF alternatives.

---

## 2. Milestones: What the Seed Got Us

| Milestone | Status | Evidence |
|---|---|---|
| ARGUS ground station at TRL 6 | Complete | 5+ km optical link validated in field |
| ZAPHOD satellite terminal co-developed | Complete | Sub-3kg CubeSat–SmallSat terminal with TakeMe2Space |
| Network marketplace live (11 stations) | Complete | stations.qosmic.space: real-time booking, pass prediction, 3D globe |
| 10 partner station agreements signed | Complete | NASA JPL, ESA, DLR, Australian, Japanese, UAE, Norwegian Arctic partners |
| Core engineering team of 8 hired | Complete | Blended avg USD 30K/yr |
| arXiv publication on link budget | Published | arXiv:2507.20908 (July 2025); probabilistic atmospheric model |
| Featured at Quantum India Summit | Complete | Deccan Herald coverage (Bengaluru, 2025) |
| Backed by Accel, Prosus, South Park Commons | Complete | Accel Atoms portfolio listing confirms |
| NQM Phase 1 PoC contract secured | Active | USD 200K Year 1; milestone payments scaling to USD 600K Year 3 |
| First commercial OGS customer (owned stations) | Year 2 target | 1 pilot customer at USD 150K ARPU |
| 5 owned ARGUS stations deployed across India | Years 2–5 | Challakere (operational) → Leh → Jodhpur → Sriharikota → Shillong |

## 3. Milestones the Series A Will Unlock

| Milestone | Timeline | Cost |
|---|---|---|
| Deploy owned stations 2–4 (Leh, Jodhpur, Sriharikota) | Months 1–12 | USD 1.5M (CapEx) |
| Scale to 3 owned-station OGS customers at USD 150K ARPU | Year 2–3 | USD 450K ARR |
| Grow partner network from 10 to 20+ stations | Year 2–3 | USD 200K (BD + integration) |
| Deliver first turnkey ARGUS hardware sale | Year 4 | USD 350K per unit |
| Expand to 15-person team | Year 5 | USD 450K/yr payroll |
| Achieve network-level >99.5% uptime across owned + partner sites | Year 3 onward | USD 250K/yr OpEx |

Our financial model includes all revenue streams: owned-station OGS, partner network commissions, ARGUS hardware sales (with COGS deducted), NQM contracts, and ZAPHOD terminal sales. Costs cover station buildout, operations, team, overhead, hardware cost of goods sold, and platform hosting. EBITDA turns positive in Year 3 at approximately USD 453K, reaching USD 1.2M by Year 4 and USD 1.99M by Year 5. The two-year build is CapEx-heavy: USD 221K negative in Year 1, USD 82K negative in Year 2, then strongly profitable from Year 3 onward. Hardware sales carry a 43% gross margin ($350K revenue − $200K COGS per ARGUS unit). The partner network grows from USD 137K in Year 1 to USD 821K by Year 5 as utilisation and partner count scale.

---

## 4. Raise Amount & Valuation

**Target: USD 4–6 million at USD 15–25 million pre-money valuation**

USD 19–31 million post-money, implying 15–19% dilution at the midpoint — consistent with Carta Q1 2025 median of 17.9% at Series A.

### Justification by Comparables

**KSAT** is the closest market comparable. At NOK 2,236 million (~USD 210M) revenue with 28 stations, 28% EBITDA margin, and a booking/platform model similar to ours, a conservative 3x revenue multiple implies ~USD 630M enterprise value. Our Year 5 projected revenue of USD 2.05M is 1% of KSAT's — small but in a growing segment (optical) where KSAT has minimal presence.

**Pixxel** raised USD 5M seed → USD 25M Series A → USD 95M total across 11 rounds (Tracxn, 2026). Employs 177 people, reported USD 4.65M revenue in FY2025, and is valued at ~USD 1.1B at its most recent round. The 200x+ price-to-sales multiple at peak valuation is not directly comparable to a seed-stage company, but it demonstrates that Indian space tech can command substantial premiums once revenue is established.

**Dhruva Space** raised ~USD 15M Series A (Via Satellite, April 2024), then a pre-Series B of USD 6M (₹51.76 Cr) at a USD 215M valuation (Entrackr). Total funding stands at USD 21.4M across 11 rounds (Tracxn).

**GalaxEye** raised USD 10M Series A (MountTech Growth Fund, November 2024) for its Drishti satellite — India's largest privately built satellite, the world's first OptoSAR payload. An additional USD 3M was raised in pre-seed.

| Company | Stage Sequence | Raise Amounts | Late-Stage Valuation |
|---|---|---|---|
| Pixxel | Seed → Series A → Series B ($60M) | $5M → $25M → $60M | ~$1.1B |
| Dhruva Space | Series A → Pre-Series B | $15M → $6M | $215M (pre-Series B) |
| GalaxEye | Pre-seed → Series A | $3M → $10M | Not disclosed |
| Mynaric | Acquired by Rocket Lab | ~$200M+ total | $155M acquisition |
| **QOSMIC (proposed)** | **Seed → Series A** | **$1M → $4–6M** | **$15–25M pre-money** |

The 15–25x step-up from our USD 1M seed is within range for deep-tech hardware. The seed was intentionally sized for one-station proof-of-concept and platform development. Series A covers full network deployment of owned stations and commercial scale-up.

---

## 5. Existing Backers & Target Investors

**Current investors:** ARTPARK, Accel (Accel Atoms), Prosus, South Park Commons. Accel and Prosus at the table validate institutional confidence in both the team and the thesis. South Park Commons (founded by former Facebook executive Ruchi Sanghvi) is raising a USD 40M India-specific fund (TechCrunch, January 2025) — a potential follow-on source.

### Lead Candidates for Series A

**Speciale Invest** — Indian deep-tech VC, USD 68M current fund, Growth Fund II targeting ₹1,400 Cr (~USD 168M). Sweet spot ~USD 1M initial checks with follow-on reserves. Portfolio: Agnikul Cosmos, GalaxEye Space, QNu Labs (quantum encryption — complementary for quantum-safe optical comms). They understand the IN-SPACe pathway, Indian deep-tech hardware go-to-market, and government procurement cycles. Our exact investor profile.

**BEENEXT** — India-Japan focused VC, closed USD 160M across two funds in 2025. Average check ~USD 11.4M. Existing Pixxel and Dhruva Space exposure means zero learning curve on Indian space tech risk. Their Japan network could unlock Japanese satellite operator partnerships (JSAT, etc.) for our booking platform — a natural expansion route.

**Space Capital** — Dedicated space VC, seed-stage specialist. Checks USD 750K–2M. Portfolio: Planet, Spire, Capella Space. Thesis on applications-layer space infrastructure — exactly how we position our booking platform. Tracked USD 14.4B invested across 216 space companies in the trailing 12 months (Space IQ, Q3 2025).

### Co-investor Candidates

**DCVC** — Deep-tech VC, Palo Alto. USD 2B+ AUM. Check sizes USD 5–25M at Series A. Portfolio includes Planet and Rocket Lab. Their 2025 Deep Tech Opportunities Report covers industrial renaissance themes that space infrastructure feeds into. They lead rounds, which makes them suitable as a lead at the upper end of our round (USD 6M).

**Lux Capital** — Frontier science VC, closed Fund IX at USD 1.5B (January 2026). Portfolio includes Relativity Space and Planet. Check range USD 100K–100M. Dedicated defence/aerospace/space practice; USD 21.4B in defence tech VC investment tracked in 2025 across 306 deals — relevant for our NQM pathway.

**Seraphim Space** — World's first publicly listed space-tech VC, London-based. Trust raised £137M, targeting £350M for next fund. Check sizes USD 250K–25M across seed to Series B. Portfolio includes Pixxel, GalaxEye, ICEYE, D-Orbit, Hawkeye 360, LeoLabs, AST SpaceMobile. Their portfolio spans the entire space stack — satellite operators, ground segment, launch, and orbital services. They understand optical ground infrastructure as a category. They are already invested in Pixxel and GalaxEye (both Indian), which signals India conviction.

**Type One Ventures** — Space and deep tech specialist, San Francisco. Raised USD 34M for Fund II (SpaceNews, 2025). Check sizes USD 500K–20M. Portfolio includes Axiom Space (USD 350M raised), Lunar Outpost, and other space infrastructure companies. Thesis: "startups building the technologies, infrastructure, and services that will be integral as we progress towards a Type I Civilization." Qosmic's optical ground infrastructure fits this thesis directly.

### India-Specific Co-investors

**growX Ventures** — Indian deep-tech VC, Gurugram. Fund II targeting ₹400 Cr (~USD 48M) for early-stage and early-growth investments. Portfolio includes Pixxel (hyperspectral satellites), Armory (defence tech), and Bellatrix (in-space propulsion). They have demonstrated capital deployment in both Indian space tech and defence tech — our two primary revenue pathways. Their investment in Pixxel gives them direct familiarity with the optical ground station use case.

**Starbridge Venture Capital** — Washington D.C.-based, space-focused early-stage VC. Check sizes USD 500K–3M. Portfolio: SpaceX, Axiom Space, Lynk Global (satellite-to-phone), Orbital Sidekick (hyperspectral), Umbra (SAR). Thesis: "space related technologies with large terrestrial market potential." Qosmic's core optical communication technology has both space-to-ground and terrestrial (FSO backhaul for telecom) applications.

**pi Ventures** — Indian deep-tech VC, Bangalore. USD 85M current fund. Check sizes USD 250K–3M. Portfolio includes Agnikul Cosmos (3D-printed rockets, US-based, India-founded) and Quanfluence (photonic quantum computing). They invest at Seed and Series A. Their Agnikul investment shows comfort with Indian space hardware. Their Quanfluence investment shows interest in photonics — directly adjacent to our 1550nm optical ground station technology.

---

## 6. Use of Funds (USD 5M midpoint case)

| Category | Amount | Detail |
|---|---|---|
| Station CapEx (owned stations 2–5) | USD 1.8M | 4 stations × ~USD 200K CapEx + contingency |
| Team expansion (8 → 15) | USD 1.2M | Incremental payroll over 18 months at USD 30K blended avg; engineering, ops, platform development, sales |
| Partner network expansion | USD 0.4M | BD team to grow from 10 to 20+ partner stations; integration engineering for new sites; platform feature development |
| Operating expenses (owned stations) | USD 0.4M | Power, BSNL fiber backhaul, maintenance, site leases, monitoring personnel |
| Office + overhead | USD 0.4M | Bangalore office scaling 8 to 15 seats; legal, IN-SPACe compliance, IP protection, insurance |
| Sales & business development | USD 0.3M | Customer acquisition for satellite operators; conference attendance (SmallSat, SpaceCom, IAC) |
| Working capital buffer | USD 0.5M | 6-month runway buffer for NQM payment delays (standard government cycle) |
| **Total** | **USD 5.0M** | |

---

## 7. Top 3 Risks & Mitigations

**1. Customer concentration in early years.** Year 1 revenue is entirely NQM contracts (USD 200K). Year 2 is 73% NQM, 27% OGS. Non-renewal of NQM Phase 2 leaves OGS revenue insufficient until Year 4.

*Mitigation:* NQM is structured as phased deliverables with government commitment letters. We maintain a 6-month working capital buffer. A second government customer (ISpA/ISRO) is in parallel discussion. The partner network (10 stations) gives us an immediate bookable product — satellite operators can access global capacity today, not just our owned stations. ZAPHOD terminal sales provide an additional non-government revenue channel.

**2. Station deployment delays at remote sites.** Leh (3,500m, −30°C winter) and Shillong (2,000mm annual monsoon) pose construction challenges that could slip deployment by 3–6 months.

*Mitigation:* Challakere deployment served as the engineering prototype — build procedure, supply chain, and integration timeline are documented. Leh is scheduled for the October–April dry window. Shillong is the last station (Year 3) with the longest preparation time. In the interim, the partner network provides continuous global coverage — we are never without bookable capacity. Backup sites at Nagpur and Hyderabad have been identified.

**3. Optical link reliability at scale.** Our 99.5% network availability assumes geographic diversity across 5 owned stations. Solo-station clear-sky probabilities range from 46% (Challakere) to 78% (Jodhpur). If any station underperforms the ERA5 model, the diversity calculation shifts.

*Mitigation:* The cloud model is built from 10-year ERA5 reanalysis data per station (Part A). Dropping one station gives 4-station availability above 97%, with a ~2.5% revenue impact. Our published probabilistic link budget model (arXiv:2507.20908) provides the framework for dynamic pass scheduling. Additionally, partner stations in different climate zones (arid, coastal, Arctic, desert) provide automated failover — the platform already handles cross-station routing.

---

*Sources: qosmic.space, stations.qosmic.space (network dashboard, accessed May 2026), Accel Atoms portfolio, MarketsandMarkets (2025), Dataintelo (2025), Space Norway Annual Report 2024, Tracxn (2026), PitchBook (2026), Entrackr (2025), Carta Q1 2025, arXiv:2507.20908. Financial projections for owned-station economics only — reference the live Excel model at `deliverables/business_model.xlsx`.*
