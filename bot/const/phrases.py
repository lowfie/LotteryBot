async def phrase_for_start_first_greeting(data: str) -> str:
    text = \
        f"""<b>Привет {data}</b> \n\nДанный бот создан для помощи нашим братьям Армянам. """ + \
        """Каждый день здесь будут раздаваться деньги, собранные со всех желающих.""" + \
        """Каждый, кто внес N рублей, автоматически становится участником розыгрыша."""
    return text


async def phrase_of_daily_draw(data: dict) -> str:
    if "winner_tag" in data:
        text = f"Тег победителя: <b>@{data['winner_tag']}\n</b>" \
               f"Сумма выигрыша: <b>{data['total_bank']}</b>"
    else:
        text = "Участники отсутствуют!"
    return text


async def back_to_main_menu() -> str:
    text = "Вы вернулись в главное меню!"
    return text


async def list_winners_of_daily_drawing(winners) -> str:
    if winners:
        winners_text = "".join(f"{num}. @{winner[0]} — {winner[1]}₽\n" for num, winner in enumerate(winners, start=1))
    else:
        winners_text = "Пока никто не победил"
    text = f"<b>Список последних 10 победителей:</b> \n\n{winners_text}\n"
    return text


async def phrase_current_prize(prize: float) -> str:
    prize_fix = float("{0:.2f}".format(prize))
    text = f"<b>Текущий банк:</b> {prize_fix}₽"
    return text


async def phrase_enter_payment_amount() -> str:
    text = "<b>Введите сумму оплаты</b>\n\n<i>Чем больше сумма, тем больше шанс</i>"
    return text


async def phrase_choose_payment_method() -> str:
    text = "Выберете способ оплаты"
    return text


async def phrase_making_payment() -> str:
    text = "Совершите оплату и проверьте её!"
    return text


async def phrase_participation_in_drawing() -> str:
    text = "Поздравляем, вы участвуете в розыгрыше!\nВы можете пополнить счёт и увеличить свой шанс."
    return text
