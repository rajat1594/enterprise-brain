"""
Enterprise Chunker Configuration

This module contains all configurable parameters used by the
Enterprise Chunker. No business logic should exist here.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ChunkConfig:
    """
    Configuration object for EnterpriseChunker.
    """

    # ------------------------------------------------------------------
    # Input / Output
    # ------------------------------------------------------------------

    input_dir: Path = Path("knowledge/spark/filtered")
    output_dir: Path = Path("knowledge/spark/chunks")

    output_filename: str = "chunks.jsonl"
    stats_filename: str = "chunk_stats.json"

    # ------------------------------------------------------------------
    # Chunk Size
    # ------------------------------------------------------------------

    # Preferred chunk size
    target_words: int = 450

    # Hard upper limit
    max_words: int = 800

    # Merge chunks below this size
    min_words: int = 50

    # Number of overlapping words between neighbouring chunks
    overlap_words: int = 50

    # Max number of markdown table rows packed into a single chunk when
    # splitting large tables (see preserve_tables). Kept small so each
    # chunk's embedding stays specific to a handful of properties/rows
    # instead of blending many unrelated ones together.
    table_rows_per_chunk: int = 4

    # ------------------------------------------------------------------
    # Parsing Behaviour
    # ------------------------------------------------------------------

    preserve_headings: bool = True
    preserve_code_blocks: bool = True
    preserve_tables: bool = True
    merge_small_sections: bool = True
    recursive_split: bool = True

    # ------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------

    source_name: str = "spark"

    include_document_path: bool = True
    include_heading_path: bool = True
    include_word_count: bool = True
    include_character_count: bool = True

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    validate_chunks: bool = True
    fail_on_large_chunk: bool = False
    report_tiny_chunks: bool = True
    report_large_chunks: bool = True

    # ------------------------------------------------------------------
    # Misc
    # ------------------------------------------------------------------

    encoding: str = "utf-8"
    ignore_read_errors: bool = True