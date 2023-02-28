from aiogram import Router, types
from aiogram.filters import Command

from bot.filter import IsAdmin
from bot.routers.admin.yoomoney_registration import yoomoney_register

admin_router = Router()
admin_router.include_router(yoomoney_register)


@admin_router.message(IsAdmin(), Command(commands="test"))
async def test_admin(message: types.Message) -> None:
    await message.answer(text="<b>В разработке!</b>")
