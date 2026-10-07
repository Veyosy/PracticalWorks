x1 = int(input("Столбец первой клетки: "))
y1 = int(input("Строка первой клетки: "))
x2 = int(input("Столбец второй клетки: "))
y2 = int(input("Строка второй клетки: "))

if not (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8):
    print("Ошибка ввода")

elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print("YES")

else:
    print("NO")