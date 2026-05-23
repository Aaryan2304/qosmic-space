from pathlib import Path

# ─── Paths ───────────────────────────────────────────────────
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
CHECKPOINT_DIR = OUTPUT_DIR / "checkpoints"
LOG_DIR = OUTPUT_DIR / "logs"
FIGURE_DIR = OUTPUT_DIR / "figures"

# ─── Model ───────────────────────────────────────────────────
BACKBONE = "efficientnet-b0"
IN_CHANNELS = 3          # RGB only (bands 2,3,4); NIR excluded for ImageNet weights
NUM_CLASSES = 2          # 0=clear, 1=cloud
ENCODER_WEIGHTS = "imagenet"
INPUT_SIZE = 384         # 384x384 patches from 38-Cloud

# ─── Training ────────────────────────────────────────────────
BATCH_SIZE = 16          
EPOCHS = 50
LEARNING_RATE = 1e-3
WEIGHT_DECAY = 1e-4
OPTIMIZER = "adamw"
SCHEDULER = "cosine"     
MIN_LR = 1e-6
SEED = 42
NUM_WORKERS = 4
PIN_MEMORY = True

# ─── Loss ────────────────────────────────────────────────────
DICE_WEIGHT = 0.5
FOCAL_WEIGHT = 0.5
FOCAL_GAMMA = 2.0
FOCAL_ALPHA = 0.75       # Upweight cloud class (minority in many patches)

# ─── Augmentation ────────────────────────────────────────────
RANDOM_CROP_SIZE = 256   # Crop 384→256 for training (regularization)
HORIZONTAL_FLIP_PROB = 0.5
VERTICAL_FLIP_PROB = 0.5
ROTATION_DEGREES = 10

# ─── Validation / Test ───────────────────────────────────────
VAL_SCENE_IDS = [
    "LC08_L1TP_002053_20160520_20170324_01_T1",
    "LC08_L1TP_029040_20160720_20170222_01_T1",
    "LC08_L1TP_045026_20160720_20170221_01_T1",
]  # 3 scenes held out for validation (~420-462 patches each)

TEST_SCENE_IDS = [
    "LC08_L1TP_034034_20160520_20170223_01_T1",
    "LC08_L1TP_044010_20160220_20170224_01_T1",
    "LC08_L1TP_059014_20160620_20170221_01_T1",
]  # 3 scenes held out for testing (~440-550 patches each)

# ─── Logging ─────────────────────────────────────────────────
SAVE_BEST_ONLY = True
METRIC_FOR_BEST = "val_miou"
