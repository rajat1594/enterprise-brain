"""
Markdown Parser

Converts a markdown document into structured Section objects.
"""

import re

from .models import Document, Section


class MarkdownParser:
    """
    Parses Markdown documents into logical sections.
    """

    HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)

    @staticmethod
    def word_count(text: str) -> int:
        return len(text.split())

    @staticmethod
    def character_count(text: str) -> int:
        return len(text)

    def parse(
        self,
        document_id: str,
        filename: str,
        source: str,
        text: str
    ) -> Document:

        document = Document(
            document_id=document_id,
            filename=filename,
            source=source,
            text=text,
            word_count=self.word_count(text),
            character_count=self.character_count(text),
        )

        document.sections = self._extract_sections(
            document_id=document_id,
            text=text
        )

        return document

    def _extract_sections(
        self,
        document_id: str,
        text: str
    ):

        matches = list(self.HEADING_PATTERN.finditer(text))

        sections = []

        # Document without headings
        if not matches:

            sections.append(
                Section(
                    document_id=document_id,
                    section_number=1,
                    heading="Document",
                    heading_level=0,
                    text=text.strip(),
                    word_count=self.word_count(text),
                )
            )

            return sections

        heading_stack = []

        for i, match in enumerate(matches):

            level = len(match.group(1))
            heading = match.group(2).strip()

            start = match.start()

            if i + 1 < len(matches):
                end = matches[i + 1].start()
            else:
                end = len(text)

            section_text = text[start:end].strip()

            while heading_stack and heading_stack[-1][0] >= level:
                heading_stack.pop()

            heading_stack.append((level, heading))

            parent = (
                heading_stack[-2][1]
                if len(heading_stack) > 1
                else None
            )

            section = Section(
                document_id=document_id,
                section_number=len(sections) + 1,
                heading=heading,
                heading_level=level,
                parent_heading=parent,
                text=section_text,
                word_count=self.word_count(section_text),
            )

            sections.append(section)

        return sections