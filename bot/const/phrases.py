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
