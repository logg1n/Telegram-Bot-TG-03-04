from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from telegram.callbacks import CatCallbackData
from telegram.keyboards import breeds_keyboard
from telegram.utils import get_random_cat, get_breed_cat

cat_router = Router()

@cat_router.message(Command("cat"))
async def show_cat_menu(msg: Message):
    await msg.answer("Выбери тип котика:", reply_markup=breeds_keyboard)

@cat_router.callback_query(CatCallbackData.filter())
async def process_cat_callback(call: CallbackQuery):
    url = await get_random_cat()
    await call.message.answer_photo(url)
