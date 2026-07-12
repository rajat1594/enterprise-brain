from pathlib import Path
from collections import Counter
import hashlib

RAW_DIR = Path("knowledge/spark/filtered")


def sha256(text):
    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


def main():

    files = sorted(RAW_DIR.glob("*.md"))

    total_words = 0
    total_chars = 0
    total_lines = 0

    hashes = []

    largest = ("", 0)
    smallest = ("", float("inf"))

    empty = 0

    headings = 0
    code_blocks = 0
    tables = 0

    print(f"Analyzing {len(files)} files...\n")

    for file in files:

        text = file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        words = len(text.split())
        chars = len(text)
        lines = len(text.splitlines())

        total_words += words
        total_chars += chars
        total_lines += lines

        hashes.append(sha256(text))

        if words == 0:
            empty += 1

        if words > largest[1]:
            largest = (file.name, words)

        if words < smallest[1]:
            smallest = (file.name, words)

        headings += text.count("\n#")
        code_blocks += text.count("```")
        tables += text.count("|")

    duplicates = sum(
        count - 1
        for count in Counter(hashes).values()
        if count > 1
    )

    print("=" * 50)

    print(f"Documents              : {len(files)}")
    print(f"Words                  : {total_words:,}")
    print(f"Characters             : {total_chars:,}")
    print(f"Average Words          : {total_words / len(files):.1f}")
    print(f"Average Lines          : {total_lines / len(files):.1f}")

    print()

    print(f"Largest Document       : {largest[0]} ({largest[1]:,} words)")
    print(f"Smallest Document      : {smallest[0]} ({smallest[1]:,} words)")

    print()

    print(f"Empty Documents        : {empty}")
    print(f"Duplicate Documents    : {duplicates}")

    print()

    print(f"Markdown Headings      : {headings:,}")
    print(f"Markdown Tables        : {tables:,}")
    print(f"Code Blocks            : {code_blocks // 2:,}")

    print("=" * 50)


if __name__ == "__main__":
    main()