# - вводим номер места
place = input("Кидай номер места: ")

# - переводим строку в целое число
place = int(place)

# - находим номер купе
compartment = (place - 1) // 4 + 1

# - ответ
print("Номер купе:",compartment)


# Вводим номер места
place_number = int(input("Кидай номер места: "))

# Находим номер купе
compartment_number = (place_number - 1) // 4 + 1

# Выводим результат
print("Номер купе:", compartment_number)


SEATS_PER_COMPARTMENT = 4
place_number = int(input("Кидай номер места: "))
compartment_number = (place_number - 1) // SEATS_PER_COMPARTMENT + 1
print("Номер купе:", compartment_number)
