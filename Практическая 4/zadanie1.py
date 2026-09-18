import math

# - вводим число
x = input("Давай сюда число: ")

# - переводим строку в число
x = float(x)

# - округляем вниз
x1 = math.floor(x)

# - округляем вверх
x2 = math.ceil(x)

# - складываем
result = x1 + x2

# - ответ
print(result)
