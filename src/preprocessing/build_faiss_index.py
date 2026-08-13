"""
Build a FAISS index from the saved chunk embeddings.

Reads:  knowledge/spark/embeddings/embeddings.npy
        knowledge/spark/embeddings/metadata.json
Writes: knowledge/spark/faiss/faiss.index
        knowledge/spark/faiss/id_mapping.json
"""

import json
from pathlib import Path

import faiss
import numpy as np

EMBEDDINGS_FILE = Path("knowledge/spark/embeddings/embeddings.npy")
METADATA_FILE = Path("knowledge/spark/embeddings/metadata.json")
OUTPUT_DIR = Path("knowledge/spark/faiss")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Loading embeddings from {EMBEDDINGS_FILE}...")
    embeddings = np.load(EMBEDDINGS_FILE)
    metadata = json.load(open(METADATA_FILE))

    assert embeddings.shape[0] == len(metadata), (
        f"Embeddings count ({embeddings.shape[0]}) does not match "
        f"metadata count ({len(metadata)})"
    )

    num_vectors, dim = embeddings.shape
    print(f"Vectors: {num_vectors}, dimension: {dim}")

    # Since embeddings are already normalized (unit length), inner product
    # search (IndexFlatIP) is mathematically equivalent to cosine similarity,
    # and is FAISS's fastest exact-search index type.
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    print(f"FAISS index built. Total vectors in index: {index.ntotal}")
    assert index.ntotal == num_vectors, "Index size does not match vector count"

    # id_mapping: FAISS internal index position -> chunk_id
    # (this lets us go from "result #7" back to an actual chunk)
    id_mapping = [
        {"faiss_index": i, "chunk_id": m["chunk_id"], "document_id": m["document_id"]}
        for i, m in enumerate(metadata)
    ]

    faiss.write_index(index, str(OUTPUT_DIR / "faiss.index"))
    with open(OUTPUT_DIR / "id_mapping.json", "w", encoding="utf-8") as f:
        json.dump(id_mapping, f, indent=2)

    print(f"Saved index and id_mapping to: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()