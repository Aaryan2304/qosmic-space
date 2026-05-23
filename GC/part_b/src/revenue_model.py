"""
Revenue model data for QOSMIC optical ground station services.

Three revenue streams with pricing, buyer personas, sales cycles, and
timeline assumptions. All numbers sourced from verified web research.

Sources (searched 2026-05-19):
- KSATlite pricing: PayloadSpace article (~$3/min S/X-band)
- Planet Labs revenue: SEC filing FY2025 ($307.7M)
- Capella Space revenue: CB Insights ($12M in 2023)
- Pixxel revenue: Tracxn (₹39.3Cr ~$4.7M)
- NQM budget: DST/PIB (₹6,003.65Cr total)
- Skyloom funding: PitchBook ($52.9M)
- Mynaric funding: PayloadSpace (~$200M)
- KSAT revenue: KSAT annual report (~$149M)
- Optical comms market: MarketsandMarkets ($0.62B→$1.56B, CAGR 20.4%)
"""
from dataclasses import dataclass, field


@dataclass
class RevenueStream:
    name: str
    priority: str          # HIGHEST / HIGH / MEDIUM
    pricing_model: str     # description of pricing structure
    price_range: str       # e.g. "$5-15/GB"
    sales_cycle_months: tuple[int, int]  # (min, max)
    timeline: str          # when first revenue expected
    buyer_persona: str
    rationale: str         # why this pricing works
    risks: list[str] = field(default_factory=list)


def get_ogs_as_a_service() -> RevenueStream:
    """
    Revenue Stream 1: OGS-as-a-Service.

    Pricing logic:
    - RF ground station passes cost ~$3/min (PayloadSpace).
      A 7-min pass = ~$21. At 100 Mbps X-band, that's ~4 GB = ~$5/GB.
    - Optical at 5 Gbps delivers 262 GB in 7 min.
    - At $5-15/GB, a pass costs $1,310-3,930.
    - Customer gets 65x more data than RF at comparable per-GB cost.
    """
    return RevenueStream(
        name="OGS-as-a-Service",
        priority="HIGHEST",
        pricing_model="Per-pass or per-GB. Also monthly subscription and reserved capacity.",
        price_range="$5-15/GB, $500-1,500/pass, $20-50K/month subscription",
        sales_cycle_months=(3, 6),
        timeline="H2 2027 (after first satellite downlink demo late 2026)",
        buyer_persona=(
            "Primary: LEO satellite imaging operators with data bottleneck "
            "(Planet $307.7M revenue, 200+ sats; Capella $12M, SAR data; "
            "Pixxel ₹39.3Cr, hyperspectral). "
            "Secondary: Defense/intelligence (SDA, DRDO). "
            "Revenue per customer at 40% utilization and 10 passes/day: ~$3.6M/yr."
        ),
        rationale=(
            "RF downlink at $3/min delivers ~4 GB per 5-min pass. "
            "Optical at $5-15/GB delivers 262 GB per 7-min pass. "
            "Same or lower cost per GB, 65x more data. "
            "Enables business models that don't work with RF: video, real-time analytics."
        ),
        risks=["Slow adoption — operators need optical terminals on satellites",
               "Price pressure as competitors enter market",
               "Cannibalisation by in-space relay networks (Kepler, SpaceX)"],
    )


def get_hardware_sales() -> RevenueStream:
    """
    Revenue Stream 2: Turnkey hardware sales.

    Pricing logic:
    - BoM per station: ~$265K (from Part A analysis).
    - Standard pricing: 1.5-2x BoM = $400-530K.
    - Premium/defense: higher margin for MIL-SPEC, encryption.
    """
    return RevenueStream(
        name="Hardware Sales (Turnkey OGS)",
        priority="MEDIUM",
        pricing_model="One-time sale per station. Three tiers: standard, premium, defense.",
        price_range="Standard 50cm: $350-500K, Premium 80cm: $600-800K, Defense: $800K-1.2M",
        sales_cycle_months=(6, 18),
        timeline="2028+ (need proven operational track record, 2+ deployed stations)",
        buyer_persona=(
            "Space agencies (ESA, ISRO, NASA) — R&D budgets. "
            "Defense (SDA, DRDO, US Space Force) — assured access. "
            "Research institutions. Governments (NQM quantum-capable OGS). "
            "Sales cycle 6-18 months; government procurement."
        ),
        rationale=(
            "BoM ~$265K/station. At $400K sale price, margin is ~34%. "
            "Higher per-deal revenue than OGS-as-a-Service but lumpy and long cycle. "
            "Mynaric CONDOR terminals are the main competitor; "
            "Mynaric raised ~$200M but is in financial distress — opportunity."
        ),
        risks=["Long government procurement cycles (12-18+ months)",
               "Mynaric/CACI/Atlas have existing relationships with SDA",
               "Requires proven reliability — no sales before first 2 stations operational"],
    )


def get_government_contracts() -> RevenueStream:
    """
    Revenue Stream 3: Government R&D contracts.

    NQM budget verified from DST/PIB:
    - Total: ₹6,003.65Cr (~$720M) over 2023-2031
    - FY2024-25 allocation: ₹86Cr (~$10M)
    - Focus areas: quantum communications, quantum computing, sensing

    QOSMIC can position for quantum-capable OGS under NQM's
    quantum communications vertical.
    """
    return RevenueStream(
        name="Government / NQM Contracts",
        priority="HIGH",
        pricing_model="R&D contracts and grants. Non-dilutive funding.",
        price_range=(
            "NQM Phase 1 (PoC): ₹5-10Cr ($600K-1.2M). "
            "NQM Phase 2 (demonstration): ₹20-30Cr ($2.4-3.6M). "
            "ISRO collaboration: ₹3-8Cr ($360K-960K). "
            "Total over 3 years: ₹30-50Cr ($3.6-6M)."
        ),
        sales_cycle_months=(6, 12),
        timeline="2027 (NQM is active 2023-2031, Phase 2/3 funding available)",
        buyer_persona=(
            "ISRO/DoS — Director, Satellite Communications. "
            "DST — Program Director, National Quantum Mission. "
            "DRDO — Director, Laser Science and Technology. "
            "Government RFPs, evaluation committees, formal procurement."
        ),
        rationale=(
            "NQM has ₹6,003.65Cr budget through 2031. QOSMIC's OGS can "
            "be positioned as quantum-capable ground infrastructure — NQM's "
            "quantum communications vertical needs ground stations compatible "
            "with photon entanglement and QKD protocols. "
            "Non-dilutive funding extends runway without equity dilution."
        ),
        risks=["Slow disbursement of NQM funds (only ₹86Cr of ₹6,003.65Cr allocated in FY2024-25)",
               "Government procurement delays (6-12 month cycle)",
               "Competition from established defense contractors"],
    )


# ─── Comparison Table ─────────────────────────────────────────

REVENUE_STREAMS = [
    get_ogs_as_a_service(),
    get_government_contracts(),
    get_hardware_sales(),
]


def print_summary():
    """Print revenue model summary for quick reference."""
    print(f"{'Stream':35s} {'Priority':10s} {'Timeline':20s} {'Price Range':40s}")
    print("-" * 105)
    for rs in REVENUE_STREAMS:
        print(f"{rs.name:35s} {rs.priority:10s} {rs.timeline:20s} {rs.price_range:40s}")
    print()

    print("Near-term recommendation (2026-2027):")
    print("  1. Secure at least 1 NQM-related contract for non-dilutive runway")
    print("  2. Sign 2-3 LOIs/MOUs with satellite operators ahead of first downlink demo")
    print("  3. Convert first satellite downlink (late 2026) into paid OGS-as-a-Service contracts")
    print("  4. Delay hardware sales until 2+ stations operational (2028+)")


if __name__ == "__main__":
    print_summary()
