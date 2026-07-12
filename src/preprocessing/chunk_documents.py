"""
Entry point for Enterprise Chunker.
"""

from enterprise_chunker.cli import EnterpriseChunker


def main():
    chunker = EnterpriseChunker()
    chunker.run()


if __name__ == "__main__":
    main()