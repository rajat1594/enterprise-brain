import json
import shutil
from collections import Counter
from pathlib import Path

RAW_DIR = Path("knowledge/spark/raw")
FILTERED_DIR = Path("knowledge/spark/filtered")
REPORT_FILE = Path("knowledge/spark/filter_report.json")

MIN_WORDS = 20

FILENAME_RULES = {
    "sha512": "Checksum file",
    ".asc": "Signature file",
    ".tgz": "Archive",
    ".gz": "Archive",
    ".zip": "Archive",
    "index-all": "Huge API index",
    "directory": "Directory listing"
}


def word_count(text):
    return len(text.split())


def rejection_reason(file_name, words):
    if words < MIN_WORDS:
        return "tiny"

    lower = file_name.lower()

    for pattern, reason in FILENAME_RULES.items():
        if pattern in lower:
            return reason

    return None


def main():

    FILTERED_DIR.mkdir(parents=True, exist_ok=True)

    accepted = 0
    rejected = 0

    reasons = Counter()

    for file in sorted(RAW_DIR.glob("*.md")):

        text = file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        reason = rejection_reason(
            file.name,
            word_count(text)
        )

        if reason:

            rejected += 1
            reasons[reason] += 1
            continue

        shutil.copy2(
            file,
            FILTERED_DIR / file.name
        )

        accepted += 1

    report = {
        "accepted": accepted,
        "rejected": rejected,
        "reasons": dict(reasons)
    }

    REPORT_FILE.write_text(
        json.dumps(report, indent=4),
        encoding="utf-8"
    )

    print("=" * 50)
    print(f"Accepted : {accepted}")
    print(f"Rejected : {rejected}")
    print("=" * 50)

    for k, v in reasons.items():
        print(f"{k:<20} {v}")

    print("\nReport saved to:")
    print(REPORT_FILE)


if __name__ == "__main__":
    main()