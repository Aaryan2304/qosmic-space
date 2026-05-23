"""Parse Obsidian vault, chunk by H2 sections, embed, and store in ChromaDB."""

import re
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

from rag.config import (
    CHROMA_DIR,
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    COLLECTION_NAME,
    EMBED_MODEL,
    VAULT_DIR,
)


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter as a dict."""
    fm = {}
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return fm
    for line in match.group(1).splitlines():
        line = line.strip()
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip()
    return fm


def chunk_by_headings(content: str, source_file: str) -> list[dict]:
    """Split markdown content by H2 headings into chunks with metadata."""
    fm = parse_frontmatter(content)
    body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)

    chunks = []
    sections = re.split(r"^## ", body, flags=re.MULTILINE)

    for section in sections:
        section = section.strip()
        if not section:
            continue

        lines = section.split("\n", 1)
        heading = lines[0].strip()
        text = lines[1].strip() if len(lines) > 1 else ""

        if len(text) > CHUNK_SIZE + CHUNK_OVERLAP:
            for i in range(0, len(text), CHUNK_SIZE - CHUNK_OVERLAP):
                chunk_text = text[i : i + CHUNK_SIZE].strip()
                if chunk_text:
                    chunks.append(
                        {
                            "text": f"{heading}\n\n{chunk_text}",
                            "source": source_file,
                            "section": heading,
                            "type": fm.get("type", "unknown"),
                        }
                    )
        elif text:
            chunks.append(
                {
                    "text": f"{heading}\n\n{text}",
                    "source": source_file,
                    "section": heading,
                    "type": fm.get("type", "unknown"),
                }
            )

    return chunks


def index_vault() -> tuple[chromadb.Collection, SentenceTransformer]:
    """Parse all vault notes, chunk, embed, and store in ChromaDB."""
    model = SentenceTransformer(EMBED_MODEL)

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    collections = [c.name for c in client.list_collections()]
    if COLLECTION_NAME in collections:
        client.delete_collection(COLLECTION_NAME)
    collection = client.create_collection(COLLECTION_NAME)

    all_chunks: list[dict] = []
    for md_file in VAULT_DIR.rglob("*.md"):
        if md_file.name == "Dashboard.md":
            continue
        if md_file.parent.name == "templates":
            continue

        content = md_file.read_text(encoding="utf-8")
        source = md_file.stem
        chunks = chunk_by_headings(content, source)
        all_chunks.extend(chunks)

    if not all_chunks:
        print("No chunks found in vault")
        return collection, model

    texts = [c["text"] for c in all_chunks]
    embeddings = model.encode(texts, show_progress_bar=True).tolist()

    ids = [f"chunk_{i}" for i in range(len(all_chunks))]
    metadatas = [
        {"source": c["source"], "section": c["section"], "type": c["type"]}
        for c in all_chunks
    ]

    collection.add(ids=ids, embeddings=embeddings, documents=texts, metadatas=metadatas)
    print(f"Indexed {len(all_chunks)} chunks from vault")
    return collection, model


if __name__ == "__main__":
    collection, model = index_vault()
    print(f"Collection '{COLLECTION_NAME}' ready with {collection.count()} chunks")
