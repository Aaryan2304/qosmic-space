"""
Pass-by-pass scheduling simulation over 30 days.

Simulates LEO satellite passes over 5 Indian ground stations and assigns each pass to the station with the highest clear-sky probability.

Key orbital parameters:
  Altitude: 500 km (typical LEO)
  Period: ~94 minutes
  Pass duration: ~7 minutes
  Passes per day per station: 8-12

For each pass, the scheduler picks the best available station.
Fallback: if no station is confidently clear, picks the best available and logs a warning.
"""
import json
import random
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import Rectangle

STATIONS = {
    "Leh":        {"monthly_clear": [0.72, 0.39, 0.55, 0.68, 0.78, 0.80, 0.82, 0.85, 0.88, 0.85, 0.80, 0.75]},
    "Jodhpur":    {"monthly_clear": [0.85, 0.84, 0.78, 0.79, 0.88, 0.78, 0.49, 0.50, 0.79, 0.93, 0.89, 0.83]},
    "Challakere": {"monthly_clear": [0.70, 0.66, 0.65, 0.55, 0.45, 0.30, 0.08, 0.12, 0.25, 0.50, 0.60, 0.65]},
    "Sriharikota":{"monthly_clear": [0.75, 0.78, 0.72, 0.65, 0.55, 0.40, 0.30, 0.32, 0.45, 0.55, 0.65, 0.72]},
    "Shillong":   {"monthly_clear": [0.80, 0.87, 0.75, 0.55, 0.35, 0.18, 0.12, 0.15, 0.25, 0.55, 0.75, 0.80]},
}

STATION_NAMES = list(STATIONS.keys())
NUM_STATIONS = len(STATION_NAMES)
DAYS = 30
PASSES_PER_DAY = 10  # average
ORBITAL_PERIOD_MIN = 94
PASS_DURATION_MIN = 7
SEED = 42
THRESHOLD = 0.6  # minimum clear probability to consider a station


def generate_passes(days: int, passes_per_day: int) -> list[dict]:
    """
    Generate synthetic LEO satellite passes over 30 days.

    Each pass: {day, start_min, end_min, duration_min}
    Day is 1-indexed. Times are minutes since midnight (0-1440).
    """
    random.seed(SEED)
    passes = []
    for day in range(1, days + 1):
        # Generate pass start times scattered through the day
        # LEO at 500km: ~10 passes/day spread across the orbital period
        start_times = sorted(random.sample(range(0, 1440 - PASS_DURATION_MIN), passes_per_day))

        for start in start_times:
            passes.append({
                "day": day,
                "start_min": start,
                "end_min": start + PASS_DURATION_MIN,
                "duration_min": PASS_DURATION_MIN,
            })
    return passes


def get_daily_cloud_state(station: dict, day: int, days_in_month: int = 30) -> float:
    """
    Get clear-sky probability for a station on a given day.

    Uses monthly clear probability. In a real system, this would come from the cloud segmentation model or ERA5/INSAT-3D data.
    """
    month = (day - 1) % 12
    p_clear = station["monthly_clear"][month]
    # Simulate actual clear/cloudy outcome with persistence
    return p_clear


def schedule(passes: list[dict]) -> dict:
    """
    Assign each pass to the best available station.

    Returns assignments dict with per-station stats and conflict log.
    """
    assignments = []        # list of {pass_id, station, day, start, end, fallback}
    station_counts = {s: 0 for s in STATION_NAMES}
    fallbacks = 0
    conflicts = 0
    # Track busy intervals per station: {station: [(start, end)]}
    busy = {s: [] for s in STATION_NAMES}

    for pass_event in passes:
        day = pass_event["day"]
        start = pass_event["start_min"]
        end = pass_event["end_min"]

        # Get clear probabilities for all stations on this day
        candidates = []
        for name in STATION_NAMES:
            p = get_daily_cloud_state(STATIONS[name], day)
            if p >= THRESHOLD:
                candidates.append((name, p))
            elif not candidates:
                candidates.append((name, p))

        # Sort by clear probability descending
        candidates.sort(key=lambda x: x[1], reverse=True)

        # Find first non-busy station
        chosen = None
        for name, _ in candidates:
            if not any(s <= start < e or s < end <= e for s, e in busy[name]):
                chosen = name
                break

        if chosen is None:
            chosen = candidates[0][0]
            conflicts += 1

        is_fallback = candidates[0][1] < THRESHOLD
        if is_fallback:
            fallbacks += 1

        busy[chosen].append((start, end))
        station_counts[chosen] += 1

        assignments.append({
            "pass_id": len(assignments),
            "station": chosen,
            "day": day,
            "start_min": start,
            "end_min": end,
            "fallback": is_fallback,
        })

    return {
        "assignments": assignments,
        "station_counts": station_counts,
        "total_passes": len(assignments),
        "fallbacks": fallbacks,
        "conflicts": conflicts,
    }


def plot_gantt(assignments: list[dict], save_path: Path):
    """Plot a Gantt chart of station assignments over 30 days."""
    colors = plt.cm.Set2(np.linspace(0, 1, NUM_STATIONS))
    station_colors = {s: colors[i] for i, s in enumerate(STATION_NAMES)}

    fig, ax = plt.subplots(figsize=(14, 6))

    filtered = [a for a in assignments if a["day"] <= 5]

    for i, a in enumerate(filtered):
        y = STATION_NAMES.index(a["station"])
        color = station_colors[a["station"]]
        alpha = 0.5 if a["fallback"] else 0.9
        ax.barh(y, PASS_DURATION_MIN, left=a["start_min"], height=0.6,
                color=color, alpha=alpha, edgecolor="black", linewidth=0.5)

    ax.set_yticks(range(NUM_STATIONS))
    ax.set_yticklabels(STATION_NAMES)
    ax.set_xlabel("Minutes since midnight")
    ax.set_title("Station Assignments — Days 1-5 (sample)")
    ax.set_xlim(0, 1440)

    # Add hourly gridlines
    for h in range(0, 24):
        ax.axvline(h * 60, color="gray", alpha=0.2, linewidth=0.5)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  Saved Gantt chart: {save_path}")


def plot_station_share(assignments: list[dict], save_path: Path):
    """Pie chart of pass assignments per station."""
    counts = {}
    for a in assignments:
        counts[a["station"]] = counts.get(a["station"], 0) + 1

    fig, ax = plt.subplots(figsize=(7, 5))
    colors = plt.cm.Set2(np.linspace(0, 1, len(counts)))
    wedges, texts, autotexts = ax.pie(
        counts.values(), labels=counts.keys(), autopct="%1.0f%%",
        colors=colors, startangle=90
    )
    ax.set_title(f"Pass Distribution Across Stations ({len(assignments)} total passes)")

    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  Saved station share: {save_path}")


def main():
    fig_dir = Path("outputs/figures")
    fig_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Scheduling Simulation — 30 Days, 5 Stations")
    print("=" * 60)
    print()

    # Generate passes
    passes = generate_passes(DAYS, PASSES_PER_DAY)
    print(f"Generated {len(passes)} satellite passes over {DAYS} days")
    print(f"  Orbital period: {ORBITAL_PERIOD_MIN} min")
    print(f"  Pass duration: {PASS_DURATION_MIN} min")
    print(f"  Passes per day per station: {PASSES_PER_DAY}")
    print(f"  Clear threshold: {THRESHOLD}")
    print()

    # Schedule
    result = schedule(passes)
    assignments = result["assignments"]
    print(f"Scheduled {result['total_passes']} passes")
    print(f"  Conflicts resolved: {result['conflicts']}")
    print(f"  Fallbacks (below threshold): {result['fallbacks']}")
    print()
    print("Assignments per station:")
    for name in STATION_NAMES:
        pct = result["station_counts"][name] / result["total_passes"] * 100
        print(f"  {name:15s}: {result['station_counts'][name]:>4d} passes ({pct:5.1f}%)")
    print()

    # Summary statistics
    fallback_pct = result["fallbacks"] / result["total_passes"] * 100
    print(f"Fallback rate: {result['fallbacks']}/{result['total_passes']} ({fallback_pct:.1f}%)")
    print(f"Conflict rate: {result['conflicts']}/{result['total_passes']} ({result['conflicts']/result['total_passes']*100:.1f}%)")
    print()

    # Figures
    print("Generating figures...")
    plot_gantt(assignments, fig_dir / "schedule_gantt.png")
    plot_station_share(assignments, fig_dir / "station_share.png")

    # Save report
    report = {
        "total_passes": result["total_passes"],
        "simulation_days": DAYS,
        "passes_per_day": PASSES_PER_DAY,
        "clear_threshold": THRESHOLD,
        "fallbacks": result["fallbacks"],
        "fallback_pct": round(fallback_pct, 1),
        "conflicts": result["conflicts"],
        "per_station": result["station_counts"],
    }
    with open("outputs/scheduler_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print(f"  Saved: outputs/scheduler_report.json")

    print()
    print("Done.")


if __name__ == "__main__":
    main()
