import json
import hashlib
from pathlib import Path

SOURCE_NAME = "spark"

RAW_DIR = Path("knowledge/spark/raw")
OUTPUT_FILE = Path("knowledge/spark/metadata.json")


def sha256(text: str):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def get_word_count(text: str):
    return len(text.split())


def build_metadata():

    metadata = []

    files = sorted(RAW_DIR.glob("*.md"))

    print(f"Found {len(files)} markdown files")

    for index, file in enumerate(files, start=1):

        content = file.read_text(encoding="utf-8")

        metadata.append({

            "id": f"{SOURCE_NAME}_{index:06d}",

            "filename": file.name,

            "source": SOURCE_NAME,

            "title": "",

            "url": "",

            "crawl_timestamp": "",

            "word_count": get_word_count(content),

            "char_count": len(content),

            "content_hash": sha256(content),

            "status": "success"

        })

    OUTPUT_FILE.write_text(
        json.dumps(metadata, indent=4),
        encoding="utf-8"
    )

    print(f"Metadata written to {OUTPUT_FILE}")
    print(f"Documents processed: {len(metadata)}")


if __name__ == "__main__":
    build_metadata()