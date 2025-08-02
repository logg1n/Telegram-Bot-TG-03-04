import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from config import config
from routes import get_router
from routes import cat_router
from routes import nasa_router
from database import ORMManager, Student

db = ORMManager("sqlite:///school_data.db", Student)
bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher()


async def main():
    db.create_table()

    commands = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="add", description="Добавить студента: /add <имя> <возраст> <класс>"),
        BotCommand(command="get", description="Получить список студентов или отфильтровать по параметрам"),
        BotCommand(command="help", description="Помощь по командам бота"),
        BotCommand(command="links", description="Кнопки с ссылками"),
        BotCommand(command="nasa", description="Получить снимок"),
        BotCommand(command="cat", description="Получить случайного котика")

    ]

    await bot.set_my_short_description("📚 Бот для работы со студентами")
    await bot.set_my_commands(commands)

    dp.include_router(get_router(db))
    dp.include_router(nasa_router)
    dp.include_router(cat_router)

    await dp.start_polling(bot)

    await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("❌ Бот остановлен вручную")
