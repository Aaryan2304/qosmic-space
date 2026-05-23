"""Two-stage retrieval: bi-encoder candidate fetch, cross-encoder reranking."""

import chromadb
from sentence_transformers import CrossEncoder, SentenceTransformer

from rag.config import (
    CHROMA_DIR,
    COLLECTION_NAME,
    RERANK_CANDIDATES,
    RERANK_MODEL,
    TOP_K,
)


class Retriever:
    def __init__(self, model: SentenceTransformer):
        self.model = model
        self.client = chromadb.PersistentClient(path=str(CHROMA_DIR))
        self.collection = self.client.get_collection(COLLECTION_NAME)
        self.reranker = CrossEncoder(RERANK_MODEL)

    def retrieve(self, query: str) -> list[dict]:
        """Two-stage retrieval: fetch candidates with bi-encoder, rerank with cross-encoder."""
        # Stage 1: Fast bi-encoder retrieval
        query_emb = self.model.encode([query]).tolist()
        results = self.collection.query(
            query_embeddings=query_emb, n_results=RERANK_CANDIDATES
        )

        candidates = []
        for i, doc in enumerate(results["documents"][0]):
            meta = results["metadatas"][0][i]
            candidates.append(
                {
                    "text": doc,
                    "source": meta["source"],
                    "section": meta["section"],
                    "type": meta["type"],
                    "biencoder_score": results["distances"][0][i],
                }
            )

        # Stage 2: Cross-encoder reranking
        pairs = [(query, c["text"]) for c in candidates]
        scores = self.reranker.predict(pairs)

        for i, score in enumerate(scores):
            candidates[i]["rerank_score"] = float(score)

        candidates.sort(key=lambda c: c["rerank_score"], reverse=True)
        return candidates[:TOP_K]
