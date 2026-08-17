"""
Recursive Text Splitter

Splits large markdown sections into retrieval-friendly chunks while
preserving as much semantic structure as possible.
"""

import re

from .config import ChunkConfig


class RecursiveSplitter:

    def __init__(self, config: ChunkConfig):
        self.config = config

    @staticmethod
    def word_count(text: str) -> int:
        return len(text.split())

    def split(self, text: str):
        """
        Entry point.
        """

        if self.word_count(text) <= self.config.max_words:
            return [text]

        return self._split_paragraphs(text)

    # ---------------------------------------------------------
    # Paragraph Split
    # ---------------------------------------------------------

    def _split_paragraphs(self, text):

        paragraphs = [
            p.strip()
            for p in re.split(r"\n\s*\n", text)
            if p.strip()
        ]

        chunks = []
        current = ""

        for paragraph in paragraphs:

            candidate = (
                current + "\n\n" + paragraph
                if current
                else paragraph
            )

            if self.word_count(candidate) <= self.config.max_words:
                current = candidate
                continue

            if current:
                chunks.append(current)

            current = ""

            if self.word_count(paragraph) <= self.config.max_words:
                current = paragraph
                continue

            chunks.extend(
                self._split_sentences(paragraph)
            )

        if current:
            chunks.append(current)

        return self._merge_small_chunks(chunks)

    # ---------------------------------------------------------
    # Sentence Split
    # ---------------------------------------------------------

    def _split_sentences(self, paragraph):
        
        if "<property>" in paragraph:
            return self._split_xml_properties(paragraph)

        if self.config.preserve_tables and self._is_markdown_table(paragraph):
            return self._split_markdown_table(paragraph)

        sentences = re.split(
            r'(?<=[.!?])\s+',
            paragraph
        )

        chunks = []

        current = ""

        for sentence in sentences:

            candidate = (
                current + " " + sentence
                if current
                else sentence
            )

            if self.word_count(candidate) <= self.config.max_words:
                current = candidate
                continue

            if current:
                chunks.append(current)

            current = ""

            if self.word_count(sentence) <= self.config.max_words:
                current = sentence
                continue

            chunks.extend(
                self._split_words(sentence)
            )

        if current:
            chunks.append(current)

        return chunks

    # ---------------------------------------------------------
    # Word Split
    # ---------------------------------------------------------

    def _split_words(self, text):

        words = text.split()

        chunks = []

        step = (
            self.config.max_words
            - self.config.overlap_words
        )

        if step <= 0:
            step = self.config.max_words

        for i in range(
            0,
            len(words),
            step
        ):

            chunk = words[
                i:i + self.config.max_words
            ]

            chunks.append(
                " ".join(chunk)
            )

        return chunks

    # ---------------------------------------------------------
    # Merge Tiny Chunks
    # ---------------------------------------------------------

    def _merge_small_chunks(self, chunks):

        if not chunks:
            return []

        result = []

        i = 0

        while i < len(chunks):

            current = chunks[i]

            if self.word_count(current) >= self.config.min_words:

                result.append(current)

                i += 1
                continue

            # Tiny chunk

            if result:

                if (
                    self.word_count(result[-1])
                    + self.word_count(current)
                    <= self.config.max_words
                ):

                    result[-1] += "\n\n" + current

                    i += 1
                    continue

            if i + 1 < len(chunks):

                chunks[i + 1] = current + "\n\n" + chunks[i + 1]

            else:

                result.append(current)

            i += 1

        return result


    # ---------------------------------------------------------
    # Markdown Table Split
    # ---------------------------------------------------------
    #
    # Large markdown tables (e.g. Spark's configuration property
    # tables) were previously falling through to sentence-level
    # splitting, which cuts through table rows mid-description and
    # packs many unrelated properties (~15+) into a single chunk.
    # That makes the resulting embedding represent "a grab-bag of
    # config properties" rather than any one property specifically,
    # which hurts retrieval precision for questions about a single
    # named property (e.g. "default value of X").
    #
    # This splits by table row instead, and caps how many rows share
    # a chunk (config.table_rows_per_chunk), so each chunk stays
    # focused on a small, coherent set of properties. The table
    # header row is repeated in every chunk so column meaning
    # (Property Name / Default / Meaning / Since Version) isn't lost.

    def _is_markdown_table(self, text):

        lines = [line for line in text.split("\n") if line.strip()]

        if not lines:
            return False

        pipe_lines = [line for line in lines if line.strip().startswith("|")]

        # Require a meaningful number of table rows, and that they make
        # up the bulk of this text, so we don't misfire on a small
        # table embedded in mostly-prose content (which fits under
        # max_words anyway and never reaches this method).
        return len(pipe_lines) >= 3 and (len(pipe_lines) / len(lines)) > 0.5

    def _split_markdown_table(self, text):

        lines = text.split("\n")

        i = 0
        leading_text = []

        # Preserve any intro prose before the table starts.
        while i < len(lines) and not lines[i].strip().startswith("|"):
            leading_text.append(lines[i])
            i += 1

        header_lines = []

        # Capture the header row and the "---" separator row, if present,
        # so every resulting chunk keeps its column context.
        while i < len(lines) and lines[i].strip().startswith("|") and len(header_lines) < 2:

            candidate = lines[i]
            cells = [c.strip() for c in candidate.strip().strip("|").split("|")]
            is_separator = all(
                c != "" and set(c) <= {"-", " ", ":"}
                for c in cells
            )

            if header_lines and not is_separator:
                # Second table line isn't a separator row -- this table
                # has no "---" row; treat what we have as data instead.
                break

            header_lines.append(candidate)
            i += 1

        row_lines = [line for line in lines[i:] if line.strip()]

        if not row_lines:
            # Nothing resembling data rows -- fall back to the
            # existing word-level splitter rather than guessing.
            return self._split_words(text)

        header_block = "\n".join(leading_text + header_lines).strip()

        group_size = max(1, self.config.table_rows_per_chunk)

        chunks = []
        for start in range(0, len(row_lines), group_size):
            group = row_lines[start:start + group_size]
            piece = (
                (header_block + "\n" + "\n".join(group)).strip()
                if header_block
                else "\n".join(group)
            )
            chunks.append(piece)

        return chunks

    def _split_xml_properties(self, text):

        import re

        properties = re.findall(
            r"<property>.*?</property>",
            text,
            flags=re.DOTALL
        )

        if not properties:
            return self._split_words(text)

        chunks = []

        current = ""

        for prop in properties:

            candidate = (
                current + "\n\n" + prop
                if current
                else prop
            )

            if self.word_count(candidate) <= self.config.max_words:

                current = candidate

            else:

                if current:
                    chunks.append(current)

                current = prop

        if current:
            chunks.append(current)

        return chunks