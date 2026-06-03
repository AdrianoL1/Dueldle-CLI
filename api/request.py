import aiohttp
import os
from dotenv import load_dotenv
from models.champion import Character

load_dotenv()

API_URL = os.getenv("API_URL")

async def bulk_insert(raw_champions: list[dict]) -> None:
    champions = [
        Character(
            name = c["name"],
            gender = c["pronouns"],
            roles = [c["role"]],
            species = c["species"],
            regions = c["regions"],
            resource = c["resource"],
            range = c["range_type"],
            release_date = int(c["release_date"]),
            character_img_url = f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{c['name']}_0.jpg"
        ).model_dump(by_alias=True)
        for c in raw_champions
    ]

    async with aiohttp.ClientSession() as session:
        for i in range(0, len(champions), 10):
            batch = champions[i:i + 10]
            async with session.post(f"{API_URL}/bulk-insert", json={"champions": batch}) as res:
                if res.status != 201:
                    body = await res.text()
                    print(f"Failed batch {i // 10 + 1}: {res.status} — {body}")

                print(f"Inserted batch {i // 10 + 1}")
