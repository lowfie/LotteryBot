import asyncio

from bot.const.phrases import phrase_of_daily_draw
from app.celery.init import celery_app
from app.celery.logic.raffle import random_winner


@celery_app.task
def send_message_everyone_task(chat_id: int, text: str) -> None:
    from bot.bot import bot
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.send_message(chat_id=chat_id, text=text))


@celery_app.task
def notification_daily_drawing() -> None:
    from bot.bot import bot
    loop = asyncio.get_event_loop()
    value = loop.run_until_complete(random_winner())
    text = loop.run_until_complete(phrase_of_daily_draw(value))
    for admin_id in value["admin_ids"]:
        loop.run_until_complete(bot.send_message(chat_id=admin_id, text=text))
