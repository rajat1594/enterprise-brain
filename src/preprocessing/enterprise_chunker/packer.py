"""
Section Packer

Responsible for combining small markdown sections into
retrieval-friendly chunks before recursive splitting.

Example:

Section 1 -> 120 words
Section 2 -> 180 words
Section 3 -> 90 words

↓

One packed section (~390 words)

This dramatically improves chunk quality compared to treating every
markdown heading as an independent chunk.
"""

from typing import List

from .config import ChunkConfig
from .models import Section


class SectionPacker:

    def __init__(self, config: ChunkConfig):
        self.config = config

    @staticmethod
    def word_count(text: str) -> int:
        return len(text.split())

    def pack(
        self,
        sections: List[Section]
    ) -> List[Section]:

        if not sections:
            return []

        packed_sections = []

        current_section = None

        for section in sections:

            # --------------------------------------------------
            # First section
            # --------------------------------------------------

            if current_section is None:
                current_section = section
                continue

            # --------------------------------------------------
            # Large sections remain independent
            # --------------------------------------------------

            if (
                current_section.word_count >= self.config.target_words
            ):

                packed_sections.append(current_section)
                current_section = section
                continue

            # --------------------------------------------------
            # Calculate merged size
            # --------------------------------------------------

            combined_words = (
                current_section.word_count
                + section.word_count
            )

            # --------------------------------------------------
            # Merge if still within target
            # --------------------------------------------------

            if combined_words <= (self.config.target_words - self.config.overlap_words):

                current_section.text += (
                    "\n\n"
                    + section.text
                )

                current_section.word_count = combined_words

                continue

            # --------------------------------------------------
            # Otherwise flush current
            # --------------------------------------------------

            packed_sections.append(current_section)

            current_section = section

        # ------------------------------------------------------
        # Flush last section
        # ------------------------------------------------------

        if current_section is not None:
            packed_sections.append(current_section)

        # ------------------------------------------------------
        # Merge tiny trailing section
        # ------------------------------------------------------

        if len(packed_sections) >= 2:

            last = packed_sections[-1]
            previous = packed_sections[-2]

            if (
                last.word_count < self.config.min_words
                and (
                    previous.word_count
                    + last.word_count
                ) <= self.config.max_words
            ):

                previous.text += "\n\n" + last.text

                previous.word_count += last.word_count

                packed_sections.pop()

        # ------------------------------------------------------
        # Renumber sections
        # ------------------------------------------------------

        for idx, section in enumerate(
            packed_sections,
            start=1
        ):

            section.section_number = idx

        return packed_sections