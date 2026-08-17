"""
Full local RAG loop: retrieve relevant chunks with FAISS, then ask a local
LLM (via Ollama) to answer the question grounded in those chunks.

This is the first piece where the local model actually generates an answer.
Only reads existing artifacts -- does not touch the crawler, cleaner,
filter, chunker, embeddings, or FAISS index.
"""

import json
from pathlib import Path

import faiss
import numpy as np
import requests
from sentence_transformers import SentenceTransformer

FAISS_INDEX_FILE = Path("knowledge/spark/faiss/faiss.index")
ID_MAPPING_FILE = Path("knowledge/spark/faiss/id_mapping.json")
CHUNKS_FILE = Path("knowledge/spark/chunks/chunks.jsonl")
EMBED_MODEL_NAME = "BAAI/bge-small-en-v1.5"
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2:3b"

TOP_K = 5


def load_chunk_lookup(path: Path):
    lookup = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            c = json.loads(line)
            lookup[c["chunk_id"]] = c
    return lookup


def retrieve(question: str, embed_model, index, id_mapping, chunk_lookup, top_k=TOP_K):
    query_vec = embed_model.encode(
        [QUERY_PREFIX + question],
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype(np.float32)

    scores, indices = index.search(query_vec, top_k)

    results = []
    for score, idx in zip(scores[0], indices[0]):
        chunk_id = id_mapping[idx]["chunk_id"]
        chunk = chunk_lookup[chunk_id]
        results.append({"score": float(score), "chunk": chunk})
    return results


def build_prompt(question: str, retrieved_chunks: list) -> str:
    context_blocks = []
    for i, r in enumerate(retrieved_chunks, start=1):
        c = r["chunk"]
        context_blocks.append(f"[Source {i}: {c.get('heading', 'untitled')}]\n{c['text']}")
    context = "\n\n---\n\n".join(context_blocks)

    prompt = f"""You are a helpful assistant answering questions about Apache Spark using ONLY the documentation excerpts provided below.

Rules:
- Answer using only the information in the sources below.
- If the sources do not contain enough information to answer, say so clearly instead of guessing.
- Cite which source number(s) you used, e.g. (Source 1).
- Be concise and technically precise.

Sources:
{context}

Question: {question}

Answer:"""
    return prompt


def ask_ollama(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False},
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["response"]


def main():
    print("Loading embedding model, FAISS index, and chunk lookup...")
    embed_model = SentenceTransformer(EMBED_MODEL_NAME)
    index = faiss.read_index(str(FAISS_INDEX_FILE))
    id_mapping = json.load(open(ID_MAPPING_FILE))
    chunk_lookup = load_chunk_lookup(CHUNKS_FILE)
    print("Ready.\n")

    while True:
        question = input("Ask a Spark question ('quit' to exit): ").strip()
        if question.lower() in ("quit", "exit", ""):
            break

        retrieved = retrieve(question, embed_model, index, id_mapping, chunk_lookup)

        print("\nTop retrieved sources:")
        for i, r in enumerate(retrieved, start=1):
            c = r["chunk"]
            print(f"  {i}. score={r['score']:.4f}  {c.get('heading')}  ({c['filename']})")

        prompt = build_prompt(question, retrieved)

        print("\nGenerating answer with llama3.2:3b...")
        answer = ask_ollama(prompt)

        print("\n" + "=" * 70)
        print("ANSWER:")
        print(answer)
        print("=" * 70 + "\n")


if __name__ == "__main__":
    main()