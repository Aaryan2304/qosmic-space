# Grand Challenge Submission — QOSMIC SPACE

**Candidate:** Aaryan Kurade | MIT-WPU Pune, ECE (AI/ML), 2025
**Date:** May 2026

---

## Structure

```
GC/
├── part_a/
│   ├── cloud_segmentation/          # Challenge A1: Cloud Segmentation Model
│   │   ├── src/                     # Python source code
│   │   │   ├── config.py           # All hyperparameters (single source of truth)
│   │   │   ├── data_utils.py       # 38-Cloud dataset loader + transforms
│   │   │   ├── model.py            # U-Net with EfficientNet-B0 encoder
│   │   │   ├── loss.py             # Dice + Focal loss combination
│   │   │   ├── train.py            # Training loop (50 epochs, AMP, checkpointing)
│   │   │   └── evaluate.py         # Test evaluation (mIoU, precision, recall, ECE)
│   │   ├── notebooks/
│   │   │   ├── dataset_exploration.ipynb   # Data exploration notebook
│   │   │   └── generate_notebook.py        # Notebook generator script
│   │   ├── deliverables/
│   │   │   └── multi_sensor_writeup.md     # 2-page multi-sensor extension paper
│   │   └── outputs/
│   │       ├── figures/             # Architecture diagram, confusion matrix, metrics, predictions
│   │       └── logs/metrics.json    # Test set metrics
│   │
│   └── network_availability/        # Challenge A2: Station Network & Scheduling
│       ├── src/
│       │   ├── station_analysis.py  # Per-station availability, spatial correlation, network model
│       │   └── scheduler.py         # 30-day pass scheduling simulation
│       ├── deliverables/
│       │   ├── ceo_memo.md          # One-page CEO memo with recommendations
│       │   └── data_source_note.md  # ERA5/MERRA-2 data source documentation
│       └── outputs/
│           ├── figures/             # Station map, availability curves, Gantt chart
│           ├── station_analysis.json
│           └── scheduler_report.json
│
└── part_b/                          # Challenge B: Business Model
    ├── src/
    │   ├── spreadsheet.py          # openpyxl generator — creates the 6-tab .xlsx
    │   └── revenue_model.py        # 3 revenue streams with pricing, personas, cycles
    └── deliverables/
        ├── business_model.xlsx     # Living spreadsheet (6 linked tabs)
        └── series_a_memo.md        # Series A readiness memo (10 investors)
```

## How to Run

### Part A1 — Cloud Segmentation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Download the 38-Cloud dataset:
```bash
# Option 1: Kaggle API
kaggle datasets download sorour/38cloud-cloud-segmentation-in-satellite-images
unzip 38cloud-cloud-segmentation-in-satellite-images.zip -d part_a/cloud_segmentation/data/38-cloud/

# Option 2: Google Drive
# https://goo.gl/683SHf
```

3. Train the model:
```bash
cd part_a/cloud_segmentation
python src/train.py
```

4. Evaluate:
```bash
python src/evaluate.py
```

### Part A2 — Network Availability

```bash
cd part_a/network_availability
python src/station_analysis.py
python src/scheduler.py
```

### Part B — Spreadsheet

```bash
cd part_b
python src/spreadsheet.py
# Output: deliverables/business_model.xlsx
```

## Key Results Summary

| Metric | Value |
|---|---|
| Cloud segmentation val mIoU (geographic split) | 82.2% |
| Cloud segmentation test mIoU (geographic split) | 44.0% |
| Solo station availability (Challakere) | 46% |
| 5-station network availability | >99% |
| Scheduler fallbacks in 30 days | 0 |
| Cost per GB at maturity | $0.146 |
| OGS-as-a-Service pricing | $1/GB |
| Breakeven | Year 3 |
| Year 5 EBITDA | $1.99M (61% margin) |
| Series A target | $4-6M at $15-25M pre-money |

## Data Sources

| Dataset | Used For | Source |
|---|---|---|
| 38-Cloud (Landsat 8) | Cloud segmentation training | Kaggle (Apache 2.0) |
| MERRA-2 Reanalysis | Station clear-sky probabilities | NASA/WeatherSpark |
| ERA5 Reanalysis | Validation (CDS API back online May 2026) | ECMWF/Copernicus |
| qosmic.space | Company product info, pricing, team | QOSMIC website |
| stations.qosmic.space | Partner network dashboard | QOSMIC network platform |
| Space Norway AR 2024 | KSAT revenue/comparables | Space Norway |
| MarketsandMarkets 2025 | GSaaS market size | MarketsandMarkets |
| Tracxn/PitchBook 2026 | Comparable company funding | Tracxn, PitchBook |
