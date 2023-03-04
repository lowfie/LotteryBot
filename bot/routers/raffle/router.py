from typing import Union

from aiogram import Router, F
from aiogram.types import (
    Message,
    CallbackQuery
)

from bot.keyboards.inline.raffle import set_raffle_menu, back_to_raffle_menu
from bot.const.phrases import phrase_current_prize
from bot.routers.raffle.yoomoney_payment import yoo_payment
from bot.routers.raffle.winner import winner_raffle
from bot.routers.raffle.crypto_payment import crypto_payment

from app.database.models import Raffle

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func


raffle_router = Router()
raffle_router.include_router(yoo_payment)
raffle_router.include_router(winner_raffle)
raffle_router.include_router(crypto_payment)


@raffle_router.message(F.text == "Розыгрыш")
@raffle_router.callback_query(lambda call: call.data == "back_raffle")
async def main_raffle_menu(message: Message or CallbackQuery) -> Union[Message, bool]:
    kwargs = {"text": "<b>Испытай удачу!</b>", "reply_markup": await set_raffle_menu()}
    if isinstance(message, CallbackQuery):
        return await message.message.edit_text(**kwargs)
    return await message.answer(**kwargs)


@raffle_router.callback_query(lambda call: call.data == "current_prize")
async def send_current_prize(call: CallbackQuery, session: AsyncSession):
    prize = (await session.execute(select(func.sum(Raffle.donated)))).scalar()
    prize = 0 if prize is None else float(prize)
    await call.message.edit_text(
        text=await phrase_current_prize(prize),
        reply_markup=await back_to_raffle_menu()
    )
