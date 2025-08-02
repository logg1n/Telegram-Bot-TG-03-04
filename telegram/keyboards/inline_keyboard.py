from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from telegram.callbacks import CatCallbackData, NasaCallbackData

dynamic_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
    ]
)

sub_dynamic_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
        [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
    ]
)

url_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📰 Новости", url="https://news.google.com")],
        [InlineKeyboardButton(text="🎵 Музыка", url="https://music.youtube.com")],
        [InlineKeyboardButton(text="🎬 Видео", url="https://www.youtube.com")]
    ]
)

breeds_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🐱 Случайный котик", callback_data=CatCallbackData(action="random_cat").pack())],
    ]
)


nasa_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🪐 Картинка дня", callback_data=NasaCallbackData(action="apod_nasa").pack())],
        [InlineKeyboardButton(text="🚀 Mars фото (Curiosity)", callback_data=NasaCallbackData(action="mars_photo_nasa").pack())]
    ]
)

