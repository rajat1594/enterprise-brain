"""
Minimal retrieval test: embed a question, search the FAISS index,
and show which chunks come back.
"""

import json
from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

FAISS_INDEX_FILE = Path("knowledge/spark/faiss/faiss.index")
ID_MAPPING_FILE = Path("knowledge/spark/faiss/id_mapping.json")
CHUNKS_FILE = Path("knowledge/spark/chunks/chunks.jsonl")
MODEL_NAME = "BAAI/bge-small-en-v1.5"
TOP_K = 5

# bge models recommend this instruction prefix on the QUERY only (not on
# the documents we embedded earlier) -- it helps the model orient toward
# "find passages relevant to this" rather than treating it as a plain sentence.
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "


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


def search(question: str, model, index, id_mapping, chunk_lookup, top_k=TOP_K):
    query_vec = model.encode(
        [QUERY_PREFIX + question],
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype(np.float32)

    scores, indices = index.search(query_vec, top_k)

    print(f"\nQuestion: {question}")
    print("-" * 70)
    for rank, (score, idx) in enumerate(zip(scores[0], indices[0]), start=1):
        chunk_id = id_mapping[idx]["chunk_id"]
        chunk = chunk_lookup[chunk_id]
        print(f"{rank}. score={score:.4f}  chunk_id={chunk_id}")
        print(f"   heading: {chunk.get('heading')}")
        print(f"   filename: {chunk.get('filename')}")
        preview = chunk["text"][:150].replace("\n", " ")
        print(f"   preview: {preview}...")
        print()


def main():
    print("Loading model, index, and mappings...")
    model = SentenceTransformer(MODEL_NAME)
    index = faiss.read_index(str(FAISS_INDEX_FILE))
    id_mapping = json.load(open(ID_MAPPING_FILE))
    chunk_lookup = load_chunk_lookup(CHUNKS_FILE)

    questions = [
        "How does Spark decide when to use a broadcast hash join?",
        "How do I configure Spark executor memory?",
        "What is a DataFrame in PySpark?",
    ]

    for q in questions:
        search(q, model, index, id_mapping, chunk_lookup)


if __name__ == "__main__":
    main()