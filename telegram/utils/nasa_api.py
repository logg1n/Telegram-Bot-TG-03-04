# utils/nasa_api.py
import aiohttp

NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"
NASA_MARS_URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
NASA_KEY = "DEMO_KEY"  # замените на свой, если есть

async def get_apod() -> dict:
    params = {"api_key": NASA_KEY}
    async with aiohttp.ClientSession() as session:
        async with session.get(NASA_APOD_URL, params=params) as response:
            data = await response.json()
            return {
                "url": data.get("url"),
                "title": data.get("title", "Картинка дня от NASA")
            }

async def get_mars_photo(sol: int = 1000) -> dict:
    params = {
        "api_key": NASA_KEY,
        "sol": sol,
        "camera": "NAVCAM"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(NASA_MARS_URL, params=params) as response:
            data = await response.json()
            photos = data.get("photos", [])
            if not photos:
                return {"url": None, "title": "Нет фото с указанного SOL"}
            return {
                "url": photos[0]["img_src"],
                "title": f"Mars photo from SOL {sol}"
            }
