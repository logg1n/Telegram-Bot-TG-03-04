# routers.py

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from telegram.keyboards.reply_keyboard import main_keyboard
from telegram.keyboards.inline_keyboard import url_keyboard, dynamic_keyboard, sub_dynamic_keyboard

def get_router(db):
    router = Router()

    @router.message(Command("start"))
    async def start(message: Message):
        await message.answer(
            f"👋 Привет, {message.from_user.first_name}!\n"
            "Я умею добавлять студентов и показывать список.\n"
            "Доступные команды:\n"
            "/add <имя> <возраст> <класс>\n"
            "/get — показать всех студентов или фильтровать"
        , reply_markup=main_keyboard)

    @router.message(F.text.in_(["Привет", "Пока"]))
    async def handle_hi_bye(message: Message):
        name = message.from_user.first_name
        if message.text == "Привет":
            await message.answer(f"Привет, {name}!")
        else:
            await message.answer(f"До свидания, {name}!")

    @router.message(Command("links"))
    async def links(message: Message):
        await message.reply("Ссылки", reply_markup=url_keyboard)

    @router.message(Command("dynamic"))
    async def dynamic(message: Message):
        await message.answer("JR", reply_markup=dynamic_keyboard)

    @router.callback_query(F.data == "show_more")
    async def call_dynamic(callback: CallbackQuery):
        await callback.message.edit_text("Опции", reply_markup=sub_dynamic_keyboard)

    @router.message(Command("add"))
    async def add(message: Message):
        parts = message.text.strip().split(maxsplit=3)
        if len(parts) != 4:
            await message.answer("❌ Формат: /add <имя> <возраст> <класс>")
            return

        _, name, age, grade = parts
        try:
            student = db.add_instance(name=name, age=int(age), grade=grade)
            await message.answer(f"✅ Добавлен: {student.name}, {student.age} лет, класс {student.grade}")
        except Exception as e:
            await message.answer(f"❌ Ошибка добавления: {e}")

    @router.message(Command("get"))
    async def get(message: Message):
        args = message.text.strip().split()[1:]
        session = db.Session()

        try:
            query = session.query(db.model_class)
            filters = {}
            if args:
                if len(args) >= 1:
                    filters["name"] = args[0]
                if len(args) >= 2:
                    try:
                        filters["age"] = int(args[1])
                    except ValueError:
                        pass
                if len(args) >= 3:
                    filters["grade"] = args[2]
                query = query.filter_by(**filters)

            results = query.all()
            if not results:
                await message.answer("📭 Нет совпадений.")
                return

            text = "\n".join([f"{s.id}. {s.name}, {s.age} лет, класс {s.grade}" for s in results])
            await message.answer(f"📚 Найдено: {len(results)}\n{text}")
        finally:
            session.close()

    return router
