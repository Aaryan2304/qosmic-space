#!/usr/bin/env python3
"""CLI interface for querying the QOSMIC knowledge graph."""

import sys

from rag.pipeline import RAGPipeline


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m rag.query 'Your question here'")
        print("Example: python -m rag.query 'Why does our FSM need 400 Hz bandwidth?'")
        sys.exit(1)

    question = " ".join(sys.argv[1:])
    print(f"Indexing vault and loading model (first run may take a minute)...\n")

    pipeline = RAGPipeline()
    answer = pipeline.query(question)

    print(f"Q: {question}\n")
    print(f"A: {answer}\n")


if __name__ == "__main__":
    main()
