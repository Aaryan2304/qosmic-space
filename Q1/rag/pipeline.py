"""Full RAG pipeline: index, retrieve, generate with citations."""

import os

from openai import OpenAI

from rag.config import OPENROUTER_BASE_URL, OPENROUTER_MODEL
from rag.indexer import index_vault
from rag.retriever import Retriever


SYSTEM_PROMPT = """You are a knowledge assistant for QOSMIC, a company building optical ground stations for laser satellite communications.

Answer questions using ONLY the provided context chunks. Rules:
1. Be concise and technically precise.
2. At the end of your answer, list citations using EXACT note titles from the context, formatted as: [[Note Title]]
3. Use ONLY note titles that appear in the [Source: ...] lines of the context chunks.
4. If the context does not contain enough information, say so explicitly.
5. Do not fabricate any technical details, numbers, or specifications.
6. Do NOT use section headers (like "Trade-offs" or "Dependencies") as citations.
7. Use Indian numbering (lakhs, crores) when discussing costs.

Example of correct citation format:
[[FSM 400 Hz Bandwidth Requirement]]
[[REQ-002: Pointing Accuracy < 10 urad]]
[[Piezoelectric vs Voice-Coil FSM Actuator]]"""


def build_prompt(query: str, chunks: list[dict]) -> str:
    """Build the user prompt with retrieved context."""
    context = "\n\n---\n\n".join(
        f"[Source: {c['source']}]\n{c['text']}"
        for c in chunks
    )
    return f"""Context from the knowledge base:

{context}

---

Question: {query}

Answer the question using only the above context. End your response with citations using the exact source names shown in [Source: ...] lines, formatted as [[Source Name]]."""


def generate_answer(client: OpenAI, prompt: str, max_retries: int = 2) -> str:
    """Call OpenRouter LLM to generate an answer with retry."""
    for attempt in range(max_retries):
        response = client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            max_tokens=500,
            temperature=0.3,
        )
        content = response.choices[0].message.content
        if content is not None:
            return content.strip()
    return "Error: LLM returned empty response after retries. Try rephrasing the question."


class RAGPipeline:
    def __init__(self):
        self.collection, self.model = index_vault()
        self.retriever = Retriever(self.model)
        self.client = OpenAI(
            base_url=OPENROUTER_BASE_URL,
            api_key=os.environ.get("OPENROUTER_API_KEY", ""),
        )

    def query(self, question: str) -> str:
        """Full RAG query: retrieve context, generate cited answer."""
        chunks = self.retriever.retrieve(question)
        prompt = build_prompt(question, chunks)
        answer = generate_answer(self.client, prompt)
        return answer
