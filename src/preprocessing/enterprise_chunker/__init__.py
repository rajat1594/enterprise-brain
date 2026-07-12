"""
Enterprise Chunker

Public API for the Enterprise Chunker package.
"""

from .config import ChunkConfig
from .models import (
    Document,
    Section,
    Chunk,
    ChunkStatistics,
    chunk_to_dict,
)
from .parser import MarkdownParser
from .packer import SectionPacker
from .splitter import RecursiveSplitter
from .writer import ChunkWriter

__version__ = "1.0.0"

__all__ = [
    "ChunkConfig",
    "Document",
    "Section",
    "Chunk",
    "ChunkStatistics",
    "chunk_to_dict",
    "MarkdownParser",
    "SectionPacker",
    "RecursiveSplitter",
    "ChunkWriter",
]