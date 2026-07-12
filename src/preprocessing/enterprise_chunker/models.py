"""
Enterprise Chunker Data Models

These dataclasses represent the core objects used throughout the
Enterprise Chunker pipeline.
"""

from dataclasses import dataclass, field
from typing import List, Optional


# ----------------------------------------------------------------------
# Document
# ----------------------------------------------------------------------

@dataclass
class Document:
    """
    Represents one Markdown document.
    """

    document_id: str
    filename: str
    source: str

    text: str

    word_count: int
    character_count: int

    sections: List["Section"] = field(default_factory=list)


# ----------------------------------------------------------------------
# Section
# ----------------------------------------------------------------------

@dataclass
class Section:
    """
    Represents one logical markdown section.

    Example:

    ## Broadcast Hash Join

    <content>
    """

    document_id: str

    section_number: int

    heading: str

    heading_level: int

    text: str

    word_count: int

    parent_heading: Optional[str] = None

    chunks: List["Chunk"] = field(default_factory=list)


# ----------------------------------------------------------------------
# Chunk
# ----------------------------------------------------------------------

@dataclass
class Chunk:
    """
    Final retrieval unit.

    Every chunk should be independently understandable.
    """

    chunk_id: str

    document_id: str

    filename: str

    source: str

    section_number: int

    chunk_number: int

    heading: str

    heading_path: List[str]

    text: str

    word_count: int

    character_count: int


# ----------------------------------------------------------------------
# Chunk Statistics
# ----------------------------------------------------------------------

@dataclass
class ChunkStatistics:

    documents: int = 0

    sections: int = 0

    chunks: int = 0

    total_words: int = 0

    average_chunk_words: float = 0

    largest_chunk_words: int = 0

    smallest_chunk_words: int = 999999999

    tiny_chunks: int = 0

    oversized_chunks: int = 0

    def update(self, chunk: Chunk):

        self.chunks += 1

        self.total_words += chunk.word_count

        self.largest_chunk_words = max(
            self.largest_chunk_words,
            chunk.word_count
        )

        self.smallest_chunk_words = min(
            self.smallest_chunk_words,
            chunk.word_count
        )

    def finalize(self):

        if self.chunks:

            self.average_chunk_words = round(
                self.total_words / self.chunks,
                2
            )


# ----------------------------------------------------------------------
# JSON Serialization
# ----------------------------------------------------------------------

def chunk_to_dict(chunk: Chunk):

    return {
        "chunk_id": chunk.chunk_id,
        "document_id": chunk.document_id,
        "filename": chunk.filename,
        "source": chunk.source,
        "section_number": chunk.section_number,
        "chunk_number": chunk.chunk_number,
        "heading": chunk.heading,
        "heading_path": chunk.heading_path,
        "word_count": chunk.word_count,
        "character_count": chunk.character_count,
        "text": chunk.text,
    }