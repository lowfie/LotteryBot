from aiogram import Router
from aiogram.types import CallbackQuery

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from app.database.models import Raffle, User
from bot.keyboards.inline.raffle import back_to_raffle_menu
from bot.keyboards.inline.payments import (
    payment_methods,
    amount_money,
    yoomoney_check_payment
)
from bot.const.phrases import (
    phrase_enter_payment_amount,
    phrase_choose_payment_method,
    phrase_participation_in_drawing,
    phrase_making_payment
)

from libs.yoomoney.client import Client
from settings import YOOMONEY_TOKEN

yoo_payment = Router()


@yoo_payment.callback_query(lambda call: call.data == "become_member")
async def choose_amount(call: CallbackQuery):
    await call.message.edit_text(
        text=await phrase_enter_payment_amount(),
        reply_markup=await amount_money(),
    )


@yoo_payment.callback_query(lambda call: call.data in [":100", ":200", ":500", ":1000", ":3000"])
async def choose_payment(call: CallbackQuery):
    await call.message.edit_text(
        text=await phrase_choose_payment_method(),
        reply_markup=await payment_methods(call.data)
    )


@yoo_payment.callback_query(lambda call: call.data.split(":")[0] == "UMoney")
async def send_payment_methods(call: CallbackQuery) -> None:
    await call.message.edit_text(
        text=await phrase_making_payment(),
        reply_markup=await yoomoney_check_payment(call.data)
    )


@yoo_payment.callback_query(lambda call: call.data.split(":")[0] == "yoomoney_check")
async def check_payment(call: CallbackQuery, session: AsyncSession) -> None:
    client = Client(YOOMONEY_TOKEN)
    label_payment_uuid = call.data.split(":")[1]
    history = client.operation_history(label=label_payment_uuid)
    for operation in history.operations:
        if operation.label == label_payment_uuid and operation.status == "success":
            user_id = (await session.execute(
                select(User.id)
                .where(User.tg_id.__eq__(call.message.chat.id))
            )).scalar()
            await session.execute(
                insert(Raffle)
                .values(user_id=user_id, donated=operation.amount)
            )
            await session.commit()
            await call.message.edit_text(
                text=await phrase_participation_in_drawing(),
                reply_markup=await back_to_raffle_menu()
            )
