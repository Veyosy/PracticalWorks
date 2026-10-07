m = int(input("Введите начальное количество организмов: "))
p = int(input("Введите увеличение в процентах: "))
n = int(input("Введите количество дней: "))

population = m

for day in range(1, n + 1):
    print(f"{day} {population}")
    population = population + population * p / 100