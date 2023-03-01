import random

from typing import Any
from sqlalchemy import select, func, delete

from bot.time import get_moscow_datetime
from app.database.models import Winner, Raffle, User
from app.database.session import async_session


async def random_winner() -> dict[str, Any]:
    async with async_session() as session:
        # user's total donated
        total_donated_users = (await session.execute(
            select(User.tg_id, func.sum(Raffle.donated))
            .join(User)
            .group_by(Raffle.user_id)
        )).all()

        admin_ids = (await session.execute(
            select(User.tg_id)
            .where(User.is_admin.__eq__(True))
        )).all()
        admin_ids = [admin_id[0] for admin_id in admin_ids]

        if total_donated_users:
            total_bank = (await session.execute(select(func.sum(Raffle.donated)))).scalar()
            user_ids, chances = [], []
            for user, user_donation in total_donated_users:
                user_ids.append(user)
                chances.append(100 * (user_donation / total_bank))
            winner_tg_id = random.choices(user_ids, weights=chances, k=1)[0]
            winner_id, winner_tg_username = (await session.execute(
                select(User.id, User.tg_username)
                .where(User.tg_id.__eq__(winner_tg_id)))
            ).first()

            user = Winner(user_id=winner_id, date_of_victory=get_moscow_datetime(), prize=total_bank)
            session.add(user)
            # clear users who participated in the contest
            await session.execute(delete(Raffle))
            await session.commit()

            return {"winner_tag": winner_tg_username, "total_bank": total_bank, "admin_ids": admin_ids}
        return {"admin_ids": admin_ids}
