n = int(input("Введите количество чисел: "))

first = int(input("Введите число: "))
second = int(input("Введите число: "))

if first > second:
    maximum = first
    second_maximum = second
else:
    maximum = second
    second_maximum = first

for i in range(n - 2):
    number = int(input("Введите число: "))

    if number > maximum:
        second_maximum = maximum
        maximum = number

    elif number > second_maximum:
        second_maximum = number

print(maximum)
print(second_maximum)