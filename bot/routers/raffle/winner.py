from aiogram import Router
from aiogram.types import CallbackQuery

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc, select

from app.database.models import Winner, User
from bot.const.phrases import list_winners_of_daily_drawing
from bot.keyboards.inline.raffle import back_to_raffle_menu


winner_raffle = Router()


@winner_raffle.callback_query(lambda call: call.data == "winners")
async def show_winners(call: CallbackQuery, session: AsyncSession) -> None:
    winners = (await session.execute(
        select(User.tg_username, Winner.prize)
        .join(Winner, Winner.user_id == User.id)
        .order_by(desc(Winner.date_of_victory))
        .limit(10)
    )).all()

    await call.message.edit_text(
        text=await list_winners_of_daily_drawing(winners),
        reply_markup=await back_to_raffle_menu()
    )
