import random
import aiohttp

async def fetch_random_anime():
    url = "https://shikimori.one/api/animes"
    params = {
        "limit": 50,
        "order": "popularity",
        "page": random.randint(1, 20)
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()
            anime = random.choice(data)

            full_title = anime.get("name", "")
            japanese_title = anime.get("japanese", "")
            rating = anime.get("score", "N/A")
            genres = ", ".join([g["russian"] for g in anime.get("genres", [])])
            image_url = f"https://shikimori.one{anime['image']['original']}"
            url_to_anime = f"https://shikimori.one/animes/{anime['id']}"
            description = anime.get("description", "Нет описания")

            return {
                "title": full_title,
                "title_jp": japanese_title,
                "rating": rating,
                "genres": genres,
                "image_url": image_url,
                "description": description[:500] + "...",
                "url": url_to_anime
            }
