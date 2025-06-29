import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import InputMediaPhoto
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN, CHANNEL_USERNAME
from anime_fetcher import fetch_random_anime
from scheduler import schedule_jobs

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(storage=MemoryStorage())

async def send_anime_post():
    anime = await fetch_random_anime()
    text = (
        f"<b>🎬 {anime['title']} ({anime['title_jp']})</b>\n"
        f"⭐ <b>Рейтинг:</b> {anime['rating']}\n"
        f"🏷 <b>Жанры:</b> {anime['genres']}\n\n"
        f"{anime['description']}\n\n"
        f"<a href='{anime['url']}'>🔗 Подробнее</a>"
    )
    await bot.send_photo(chat_id=CHANNEL_USERNAME, photo=anime['image_url'], caption=text)

async def main():
    await schedule_jobs(send_anime_post)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
