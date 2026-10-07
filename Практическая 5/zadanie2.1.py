weight, height = map(float,(input("Введите вес в кг и рост в метрах").split()))
imt = weight / (height * height)
print(f"Ваш ИМТ: {imt:.1f} кг/м2")