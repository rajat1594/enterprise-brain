"""
Enterprise Chunker CLI

Runs the complete Enterprise Chunking pipeline.

Pipeline

Markdown Documents
        ↓
Markdown Parser
        ↓
Section Packer
        ↓
Recursive Splitter
        ↓
Chunk Objects
        ↓
JSONL Writer
"""

from pathlib import Path

from .config import ChunkConfig
from .models import Chunk, ChunkStatistics
from .parser import MarkdownParser
from .packer import SectionPacker
from .splitter import RecursiveSplitter
from .writer import ChunkWriter


class EnterpriseChunker:

    def __init__(self, config=None):

        self.config = config or ChunkConfig()

        self.parser = MarkdownParser()

        self.packer = SectionPacker(self.config)

        self.splitter = RecursiveSplitter(self.config)

        self.writer = ChunkWriter(self.config)

        self.stats = ChunkStatistics()

    @staticmethod
    def word_count(text):

        return len(text.split())

    def build_chunks(self):

        all_chunks = []
        tiny_chunks = []
        oversized_chunks = []

        files = sorted(
            self.config.input_dir.glob("*.md")
        )

        self.stats.documents = len(files)

        for doc_number, file in enumerate(files, start=1):

            print(f"Processing {file.name}")

            text = file.read_text(
                encoding=self.config.encoding,
                errors="ignore"
            )

            document = self.parser.parse(
                document_id=f"spark_{doc_number:06d}",
                filename=file.name,
                source=self.config.source_name,
                text=text
            )

            packed_sections = self.packer.pack(
                document.sections
            )

            self.stats.sections += len(
                packed_sections
            )

            chunk_number = 1

            for section in packed_sections:

                pieces = self.splitter.split(
                    section.text
                )

                for idx, piece in enumerate(pieces):

                    if (
                        idx > 0
                        and self.config.preserve_headings
                    ):

                        piece = (
                            f"## {section.heading}\n\n"
                            + piece
                        )

                    chunk = Chunk(

                        chunk_id=f"{document.document_id}_{chunk_number:04d}",

                        document_id=document.document_id,

                        filename=document.filename,

                        source=document.source,

                        section_number=section.section_number,

                        chunk_number=chunk_number,

                        heading=section.heading,

                        heading_path=[
                            section.heading
                        ],

                        text=piece,

                        word_count=self.word_count(piece),

                        character_count=len(piece)
                    )

                    if chunk.word_count < self.config.min_words:
                        self.stats.tiny_chunks += 1
                        tiny_chunks.append({
                            "filename": chunk.filename,
                            "heading": chunk.heading,
                            "word_count": chunk.word_count,
                            "text": chunk.text
                        })

                    if chunk.word_count > self.config.max_words:
                        self.stats.oversized_chunks += 1

                        oversized_chunks.append({
                            "filename": chunk.filename,
                            "heading": chunk.heading,
                            "word_count": chunk.word_count,
                            "text": chunk.text
                        })

                    self.stats.update(chunk)

                    all_chunks.append(chunk)

                    chunk_number += 1

        import json
        output_dir = self.config.output_dir
        with open(output_dir / "tiny_chunks.json", "w", encoding="utf-8") as f:
            json.dump(tiny_chunks, f, indent=2, ensure_ascii=False)
        with open(output_dir / "oversized_chunks.json", "w", encoding="utf-8") as f:
            json.dump(oversized_chunks, f, indent=2, ensure_ascii=False)

        return all_chunks

    def run(self):

        chunks = self.build_chunks()

        self.writer.write_chunks(chunks)

        self.writer.write_statistics(
            self.stats
        )

        self.writer.print_summary(
            self.stats
        )


def main():

    EnterpriseChunker().run()


if __name__ == "__main__":
    main()