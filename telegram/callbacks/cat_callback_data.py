from aiogram.filters.callback_data import CallbackData


class CatCallbackData(CallbackData, prefix="cat"):
    action: str