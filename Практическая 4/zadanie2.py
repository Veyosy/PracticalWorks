import math

# - координаты первой точки
x1 = input("Где первая точка по x? ")
y1 = input("А по y где она? ")

# - координаты второй точки
x2 = input("Теперь вторая точка по x: ")
y2 = input("Ну и y второй точки: ")

# - переводим значения в числа
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

# - находим разницу координат
a = x1 - x2
b = y1 - y2

# - возводим в квадрат
a = a ** 2
b = b ** 2

# - складываем
result = a + b

# - извлекаем корень
distance = math.sqrt(result)

# - ответ
print(distance)



import math

x1, y1 = map(float, input("Введите координаты первой точки (x y): ").split())
x2, y2 = map(float, input("Введите координаты второй точки (x y): ").split())

distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print("Евклидово расстояние:", distance)

import math

# Ввод данных
x1, y1 = map(float, input("Введите координаты первой точки (x y): ").split())
x2, y2 = map(float, input("Введите координаты второй точки (x y): ").split())

# Нахождение длины
d = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

print(f"Евклидово расстояние: {d:.2f} метров")