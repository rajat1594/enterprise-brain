"""
Chunk Writer

Responsible for writing chunks to JSONL and generating
chunking statistics.
"""

import json
from pathlib import Path

from .models import Chunk, ChunkStatistics, chunk_to_dict
from .config import ChunkConfig


class ChunkWriter:

    def __init__(self, config: ChunkConfig):

        self.config = config

        self.output_dir = config.output_dir

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.chunk_file = (
            self.output_dir
            / config.output_filename
        )

        self.stats_file = (
            self.output_dir
            / config.stats_filename
        )

    # --------------------------------------------------------
    # Write JSONL
    # --------------------------------------------------------

    def write_chunks(
        self,
        chunks: list[Chunk]
    ):

        with open(
            self.chunk_file,
            "w",
            encoding="utf-8"
        ) as writer:

            for chunk in chunks:

                writer.write(
                    json.dumps(
                        chunk_to_dict(chunk),
                        ensure_ascii=False
                    )
                )

                writer.write("\n")

    # --------------------------------------------------------
    # Write Statistics
    # --------------------------------------------------------

    def write_statistics(
        self,
        stats: ChunkStatistics
    ):

        stats.finalize()

        output = {
            "documents": stats.documents,
            "sections": stats.sections,
            "chunks": stats.chunks,
            "total_words": stats.total_words,
            "average_chunk_words": stats.average_chunk_words,
            "largest_chunk_words": stats.largest_chunk_words,
            "smallest_chunk_words": stats.smallest_chunk_words,
            "tiny_chunks": stats.tiny_chunks,
            "oversized_chunks": stats.oversized_chunks
        }

        with open(
            self.stats_file,
            "w",
            encoding="utf-8"
        ) as writer:

            json.dump(
                output,
                writer,
                indent=4
            )

    # --------------------------------------------------------
    # Console Report
    # --------------------------------------------------------

    def print_summary(
        self,
        stats: ChunkStatistics
    ):

        stats.finalize()

        print("=" * 60)
        print("Enterprise Chunker Summary")
        print("=" * 60)

        print(f"Documents            : {stats.documents}")
        print(f"Sections             : {stats.sections}")
        print(f"Chunks               : {stats.chunks}")
        print(f"Total Words          : {stats.total_words:,}")
        print(f"Average Chunk Words  : {stats.average_chunk_words}")
        print(f"Largest Chunk        : {stats.largest_chunk_words}")
        print(f"Smallest Chunk       : {stats.smallest_chunk_words}")
        print(f"Tiny Chunks          : {stats.tiny_chunks}")
        print(f"Oversized Chunks     : {stats.oversized_chunks}")

        print()
        print(f"Chunks File          : {self.chunk_file}")
        print(f"Statistics File      : {self.stats_file}")

        print("=" * 60)