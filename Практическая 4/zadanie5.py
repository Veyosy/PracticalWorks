# - вводим количество минут
minutes = input("Сколько минут будем переводить? ")

# - переводим значение в целое число
minutes = int(minutes)

# - полные часы
hours = minutes // 60

# - оставшиеся минуты
rest_minutes = minutes % 60

# - результат
print(minutes, "мин - это", hours, "час", rest_minutes, "минут")