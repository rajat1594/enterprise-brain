import re
from pathlib import Path

RAW_DIR = Path("knowledge/spark/raw")
CLEAN_DIR = Path("knowledge/spark/cleaned")


def clean_markdown(text: str) -> str:
    """
    Cleans markdown while preserving meaning.
    """

    # Normalize Windows/Mac line endings
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Remove trailing spaces
    text = "\n".join(line.rstrip() for line in text.split("\n"))

    # Replace tabs with 4 spaces
    text = text.replace("\t", "    ")

    # Collapse 3+ blank lines into 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove spaces at beginning/end
    text = text.strip()

    # Ensure file ends with newline
    text += "\n"

    return text


def main():

    CLEAN_DIR.mkdir(parents=True, exist_ok=True)

    files = sorted(RAW_DIR.glob("*.md"))

    print(f"Found {len(files)} markdown files")

    cleaned_count = 0

    for file in files:

        content = file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        cleaned = clean_markdown(content)

        output_file = CLEAN_DIR / file.name

        output_file.write_text(
            cleaned,
            encoding="utf-8"
        )

        cleaned_count += 1

    print(f"\nSuccessfully cleaned {cleaned_count} files")
    print(f"Output folder: {CLEAN_DIR}")


if __name__ == "__main__":
    main()