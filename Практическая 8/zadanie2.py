all_even = True

for i in range(10):
    number = int(input("Введите число: "))

    if number % 2 != 0:
        all_even = False

if all_even:
    print("YES")
else:
    print("NO")