"""RAG pipeline configuration."""

import os
from pathlib import Path

# Load .env file if it exists
_env_file = Path(__file__).parent / ".env"
if _env_file.exists():
    for line in _env_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, val = line.split("=", 1)
            os.environ.setdefault(key.strip(), val.strip())

VAULT_DIR = Path(__file__).parent.parent / "obsidian-vault"
CHROMA_DIR = Path(__file__).parent / ".chroma_db"
COLLECTION_NAME = "qosmic_knowledge"

EMBED_MODEL = "all-mpnet-base-v2"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100
TOP_K = 3
RERANK_MODEL = "cross-encoder/ms-marco-MiniLM-L6-v2"
RERANK_CANDIDATES = 10

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODEL = "openai/gpt-oss-120b:free"
