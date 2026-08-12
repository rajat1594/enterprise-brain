from sentence_transformers import SentenceTransformer
import numpy as np

print("Loading BAAI/bge-small-en-v1.5...")
model = SentenceTransformer("BAAI/bge-small-en-v1.5")

test_sentences = [
    "How does Spark decide when to use a broadcast hash join?",
    "PySpark DataFrame API reference",
]

embeddings = model.encode(test_sentences)

print(f"Model loaded OK")
print(f"Embedding shape: {embeddings.shape}")
print(f"Embedding dtype: {embeddings.dtype}")
print(f"Vector dimension: {embeddings.shape[1]}")
print(f"Sample values (first 5 dims of first vector): {embeddings[0][:5]}")