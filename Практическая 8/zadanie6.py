import random

secret_number = random.randint(1, 10)
guessed = False

for attempt in range(3):
    number = int(input("Введите число от 1 до 10: "))

    if number == secret_number:
        print("Угадал!")
        guessed = True
        break

    elif number < secret_number:
        print("Неверно. Нужно больше")

    else:
        print("Неверно. Нужно меньше")

if not guessed:
    print(f"Ты не угадал. Правильный ответ: {secret_number}")