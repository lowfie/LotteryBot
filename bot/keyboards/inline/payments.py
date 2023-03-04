from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from libs.yoomoney.quickpay.quickpay import Quickpay

import uuid


async def yoomoney_check_payment(callback: str) -> InlineKeyboardMarkup:
    amount = float(callback.split(":")[1])
    label_payment_uuid = str(uuid.uuid1())
    quickpay = Quickpay(
        receiver="410019014512803",
        quickpay_form="shop",
        targets="Sponsor this project",
        paymentType="SB",
        sum=amount,
        label=label_payment_uuid
    )
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="Оплатить",
            url=str(quickpay.redirected_url),
            callback_data=callback + f":pay"),
    )
    builder.row(
        InlineKeyboardButton(
            text="Проверить оплату",
            callback_data=f"yoomoney_check:{label_payment_uuid}")
    )
    builder.row(
        InlineKeyboardButton(text="Назад", callback_data="back_raffle")
    )
    return builder.as_markup(resize_keyboard=True)


async def payment_methods(amount: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="ЮMoney", callback_data="UMoney" + amount),
        InlineKeyboardButton(text="Крипта", callback_data="Crypto" + amount)
    )
    builder.row(
        InlineKeyboardButton(text="Назад", callback_data="back_raffle")
    )
    return builder.as_markup(resize_keyboard=True)


async def amount_money() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="3000р", callback_data=":3000"),
        InlineKeyboardButton(text="1000р", callback_data=":1000"),
        InlineKeyboardButton(text="500р", callback_data=":500"),
    )
    builder.row(
        InlineKeyboardButton(text="200р", callback_data=":200"),
        InlineKeyboardButton(text="100р", callback_data=":100")
    )
    builder.row(
        InlineKeyboardButton(text="Назад", callback_data="back_raffle")
    )
    return builder.as_markup(resize_keyboard=True)



