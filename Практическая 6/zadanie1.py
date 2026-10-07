temperature = float(input("Введите температуру: "))
pressure = int(input("Введите верхнее давление: "))
pulse = int(input("Введите пульс: "))

if temperature < 35 or temperature > 38 or pressure < 105 or pressure > 140 or pulse < 55 or pulse > 110:
    print("Требуется врач")

elif 36 <= temperature <= 37 and 110 <= pressure <= 130 and 60 <= pulse <= 100:
    print("Нормальное состояние")

else:
    print("Легкое недомогание")