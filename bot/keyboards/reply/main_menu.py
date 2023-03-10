from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


async def user_main_markup() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Розыгрыш"),
        # KeyboardButton(text="Попросить помощь")
    )
    return builder.as_markup(resize_keyboard=True)
