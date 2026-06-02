import aiohttp
from aiohttp import ClientSession
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

DATA_URL = os.getenv("DATA_URL")
WIKI_URL = os.getenv("WIKI_URL")

async def fetch_page(session: ClientSession, url: str) -> str:
    async with session.get(url) as res:
        return await res.text()

async def get_champions_slugs() -> list[str]:
    async with aiohttp.ClientSession() as session:
        async with session.get(DATA_URL) as res:
            data: dict = await res.json()

    slugs = [f"{champion_data['name'].replace("'", '%27')}"
             for champion_data in data["data"].values()]

    print(f"Total: {len(slugs)} champions")
    return slugs

async def get_champions_pages(slugs: list[str]) -> list[str]:
    semaphore = asyncio.Semaphore(10)

    async def fetch_champion(slug: str):
        async with semaphore:
            wiki_html, universe_html = await asyncio.gather(
                fetch_page(session, f"{WIKI_URL}/{slug}"),
                fetch_page(session, f"{WIKI_URL}/Universe:{slug}")
            )

            return {
                slug: {
                    "wiki": wiki_html,
                    "universe": universe_html
                }
            }

    async with aiohttp.ClientSession() as session:
        tasks = []
        for slug in slugs:
            tasks.append(fetch_champion(slug))
        return await asyncio.gather(*tasks)
