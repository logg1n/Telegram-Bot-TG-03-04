from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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