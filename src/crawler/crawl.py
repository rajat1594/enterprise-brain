import asyncio
import re
from pathlib import Path

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy

SOURCE_NAME = "spark"

START_URL = "https://spark.apache.org/docs/latest/"

ALLOWED_DOMAIN = "spark.apache.org"

ALLOWED_PATH_PREFIX = "/docs/latest/"

OUTPUT_DIR = Path("knowledge/spark")


def safe_filename(url: str) -> str:
    """
    Convert URL into a safe markdown filename.
    """

    url = url.replace("https://", "")
    url = url.replace("http://", "")

    url = re.sub(r"[^\w\-./]", "", url)

    url = url.replace("/", "_")

    if not url.endswith(".md"):
        url += ".md"

    return url


async def main():

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    config = CrawlerRunConfig(

        deep_crawl_strategy=BFSDeepCrawlStrategy(

            max_depth=10,

            include_external=False,

            max_pages=10000

        ),

        stream=False,

        verbose=True

    )

    async with AsyncWebCrawler() as crawler:

        results = await crawler.arun(

            START_URL,

            config=config

        )

    print(f"\nTotal pages crawled: {len(results)}\n")

    for result in results:

        if not result.success:
            continue

        filename = safe_filename(result.url)

        output_path = OUTPUT_DIR / filename

        output_path.write_text(

            result.markdown,

            encoding="utf-8"

        )

        print(f"Saved: {filename}")


if __name__ == "__main__":
    asyncio.run(main())