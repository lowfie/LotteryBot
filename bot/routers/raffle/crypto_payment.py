from aiogram import Router
from aiogram.types import CallbackQuery

from bot.keyboards.inline.raffle import back_to_raffle_menu


crypto_payment = Router()


@crypto_payment.callback_query(lambda call: call.data.split(":")[0] == "Crypto")
async def send_payment_methods(call: CallbackQuery) -> None:
    await call.message.edit_text(
        "<b>Временно недоступно</b>",
        reply_markup=await back_to_raffle_menu()
    )
