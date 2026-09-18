# - вводим номер места
place = input("Кидай номер места: ")

# - переводим строку в целое число
place = int(place)

# - находим номер купе
compartment = (place - 1) // 4 + 1

# - выводим ответ
print(compartment)