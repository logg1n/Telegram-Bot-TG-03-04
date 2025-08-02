# utils/cat_api.py
import aiohttp

API_URL = "https://api.thecatapi.com/v1/images/search"


async def get_random_cat() -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as response:
            data = await response.json()
            return data[0]["url"]

async def get_breed_cat(breed_id: str) -> str:
    params = {"breed_ids": breed_id, "limit": 1}
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL, params=params) as response:
            data = await response.json()
            print(data)

            return data[0]["url"]
