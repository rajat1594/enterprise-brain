"""
Generate local embeddings for all chunks using BAAI/bge-small-en-v1.5.

Reads:  knowledge/spark/chunks/chunks.jsonl
Writes: knowledge/spark/embeddings/embeddings.npy
        knowledge/spark/embeddings/metadata.json
        knowledge/spark/embeddings/model_info.json
"""

import json
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

CHUNKS_FILE = Path("knowledge/spark/chunks/chunks.jsonl")
OUTPUT_DIR = Path("knowledge/spark/embeddings")
MODEL_NAME = "BAAI/bge-small-en-v1.5"
BATCH_SIZE = 32


def load_chunks(path: Path):
    chunks = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            chunks.append(json.loads(line))
    return chunks


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Loading chunks from {CHUNKS_FILE}...")
    chunks = load_chunks(CHUNKS_FILE)
    print(f"Loaded {len(chunks)} chunks")

    print(f"Loading model {MODEL_NAME}...")
    model = SentenceTransformer(MODEL_NAME)
    vector_dim = model.get_sentence_embedding_dimension()

    texts = [c["text"] for c in chunks]

    print(f"Encoding {len(texts)} chunks (batch size {BATCH_SIZE})...")
    embeddings = model.encode(
        texts,
        batch_size=BATCH_SIZE,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,  # recommended for bge models; enables cosine sim via dot product
    ).astype(np.float32)

    # --- Success criteria checks ---
    assert embeddings.shape[0] == len(chunks), (
        f"Vector count ({embeddings.shape[0]}) does not match chunk count ({len(chunks)})"
    )
    assert embeddings.shape[1] == vector_dim, "Vector dimension mismatch"

    # Deterministic chunk_id <-> vector index mapping
    metadata = [
        {
            "index": i,
            "chunk_id": c["chunk_id"],
            "document_id": c["document_id"],
            "filename": c["filename"],
        }
        for i, c in enumerate(chunks)
    ]

    model_info = {
        "model_name": MODEL_NAME,
        "vector_dimension": int(vector_dim),
        "normalize_embeddings": True,
        "num_vectors": int(embeddings.shape[0]),
        "chunk_count": len(chunks),
        "batch_size": BATCH_SIZE,
    }

    np.save(OUTPUT_DIR / "embeddings.npy", embeddings)
    with open(OUTPUT_DIR / "metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    with open(OUTPUT_DIR / "model_info.json", "w", encoding="utf-8") as f:
        json.dump(model_info, f, indent=2)

    print(f"\nDone.")
    print(f"Embeddings shape: {embeddings.shape}")
    print(f"Saved to: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()