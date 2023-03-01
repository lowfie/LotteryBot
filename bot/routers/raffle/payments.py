from aiogram import Router
from aiogram.types import CallbackQuery

from bot.keyboards.inline.raffle import back_to_raffle_menu
from bot.keyboards.inline.payments import payment_methods, amount_money
from bot.const.phrases import phrase_enter_payment_amount, phrase_choose_payment_method


payment_raffle = Router()


@payment_raffle.callback_query(lambda call: call.data == "become_member")
async def choose_amount(call: CallbackQuery):
    await call.message.edit_text(
        text=await phrase_enter_payment_amount(),
        reply_markup=await amount_money(),
    )


@payment_raffle.callback_query(lambda call: call.data in [":100", ":200", ":500", ":1000", ":3000"])
async def choose_payment(call: CallbackQuery):
    await call.message.edit_text(
        text=await phrase_choose_payment_method(),
        reply_markup=await payment_methods(call.data)
    )


@payment_raffle.callback_query(lambda call: call.data.split(":")[0] == "Crypto")
async def send_payment_methods(call: CallbackQuery) -> None:
    await call.message.delete()
    await call.message.answer(
        "<b>Временно недоступно</b>",
        reply_markup=await back_to_raffle_menu()
    )
