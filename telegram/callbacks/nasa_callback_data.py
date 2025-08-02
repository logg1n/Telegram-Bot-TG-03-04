from aiogram.filters.callback_data import CallbackData


class NasaCallbackData(CallbackData, prefix="nasa"):
    action: str