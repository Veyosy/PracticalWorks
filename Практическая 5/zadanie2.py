# - ввод веса и роста через пробел
weight, height = map(
    float,input("Введите вес и рост через пробел: ").split()


# - расчет ИМТ
bmi = weight / (height * height)

# - вывод результата
print(f"Ваш ИМТ: {bmi:.1f}")