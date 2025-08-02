from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = [
    [KeyboardButton(text='Привет'), KeyboardButton(text='Пока')],
]

main_keyboard = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)