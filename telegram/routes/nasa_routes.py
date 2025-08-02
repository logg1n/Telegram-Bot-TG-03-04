from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from telegram.callbacks import NasaCallbackData
from telegram.keyboards import nasa_keyboard
from telegram.utils import get_apod, get_mars_photo

nasa_router = Router()

@nasa_router.message(Command("nasa"))
async def show_nasa_menu(msg: Message):
    await msg.answer("Выбери космический контент:", reply_markup=nasa_keyboard)

@nasa_router.callback_query(NasaCallbackData.filter())
async def process_nasa_callback(call: CallbackQuery, callback_data: NasaCallbackData):
    if callback_data.action == "apod_nasa":
        data = await get_apod()
    elif callback_data.action == "mars_photo_nasa":
        data = await get_mars_photo()
    await call.message.answer_photo(data["url"], caption=data["title"])
