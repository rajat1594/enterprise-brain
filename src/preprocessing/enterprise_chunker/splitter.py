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