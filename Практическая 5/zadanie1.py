# - налоговая ставка
TAX_RATE = 0.13

# - ввод годового дохода
income = float(input("Введите годовой черный доход: "))

# - расчет суммы налога
tax = income * TAX_RATE

# - расчет дохода после вычета налога
income_after_tax = income - tax

# - вывод результатов
print(f"Общая сумма грязных денег: {income:,.2f} руб.".replace(",", " "))
print(f"Сумма наложика: {tax:,.2f} руб.".replace(",", " "))
print(f"Сумма чистых денюшек на ручки: {income_after_tax:,.2f} руб.".replace(",", " "))