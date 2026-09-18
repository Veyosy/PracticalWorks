import math

# - вводим угол в градусах
x = input("Кидай угол в градусах: ")

# - переводим строку в число
x = float(x)

# - переводим градусы в радианы
x = math.radians(x)

# - считаем синус
sin_x = math.sin(x)

# - считаем косинус
cos_x = math.cos(x)

# - считаем тангенс
tan_x = math.tan(x)

# - возводим тангенс в квадрат
tan_x = tan_x ** 2

# - складываем все значения
result = sin_x + cos_x + tan_x

# - выводим ответ
print(result)