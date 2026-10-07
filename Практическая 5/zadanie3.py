# - курс доллара к рублю
USD_TO_RUB = 95.50


# - функция перевода долларов в рубли
def convert_usd_to_rub(amount_usd):
    """
    Переводит сумму из долларов в рубли.

    Args:
        amount_usd (float): Сумма в долларах.

    Returns:
        float: Сумма в рублях.
    """
    return amount_usd * USD_TO_RUB


# - ввод суммы в долларах
amount_usd = float(input("Введите бабки в долларах: "))

# - перевод долларов в рубли
amount_rub = convert_usd_to_rub(amount_usd)

# - вывод результата
print(f"Сумма в рублях: {amount_rub:.2f} руб.")