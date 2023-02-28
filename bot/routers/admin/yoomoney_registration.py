from aiogram import Router, types
from aiogram.filters import Command

from bot.filter import IsAdmin
from libs.yoomoney.auth.authorize import Authorize
from settings import APP_HOSTNAME, YOOMONEY_CLIENT_ID

yoomoney_register = Router()

auth = Authorize(
    client_id=YOOMONEY_CLIENT_ID,
    redirect_url=APP_HOSTNAME
)


@yoomoney_register.message(IsAdmin(), Command(commands="ysession"))
async def yoomoney_session(message: types.Message) -> None:
    auth_session_code = await auth.auth_session_code()
    await message.answer(
        f"Перейдите по ссылке и скопируйте её:\n\n{auth_session_code}",
        disable_web_page_preview=True
    )


@yoomoney_register.message(IsAdmin(), Command(commands="ytoken"))
async def yoomoney_token(message: types.Message) -> None:
    code = message.text[8:]
    token = await auth.get_yoomoney_token(code)
    await message.answer(f"<b>Никому не показывайте этот токен:</b>\n\n{token}")
