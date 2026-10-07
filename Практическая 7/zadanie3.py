COFFEE_PRICE = 120
TEA_PRICE = 80
JUICE_PRICE = 100
WATER_PRICE = 50
LEMONADE_PRICE = 90

drink = input("Выберите напиток (1-5 или название): ").lower()

match drink:
    case "1" | "кофе":
        name = "Кофе ☕"
        price = COFFEE_PRICE

    case "2" | "чай":
        name = "Чай 🍵"
        price = TEA_PRICE

    case "3" | "сок":
        name = "Сок 🧃"
        price = JUICE_PRICE

    case "4" | "вода":
        name = "Вода 💧"
        price = WATER_PRICE

    case "5" | "лимонад":
        name = "Лимонад 🥤"
        price = LEMONADE_PRICE

    case _:
        print(f"Ошибка: такого напитка нет")
        name = ""

if name != "":
    count = int(input("Введите количество порций: "))

    if count > 0:
        total = price * count

        discount_code = input("Введите код скидки или нажмите Enter: ").upper()

        if discount_code == "STUDENT":
            discount = total * 0.2
        else:
            discount = 0

        final_price = total - discount

        if count == 1:
            portion = "порция"
        elif 2 <= count <= 4:
            portion = "порции"
        else:
            portion = "порций"

        print(f"==============================")
        print(f"       ☕ КВИТАНЦИЯ КАФЕ ☕")
        print(f"==============================")
        print(f"Товар: {name}")
        print(f"Цена за порцию: {price} руб.")
        print(f"Количество: {count} {portion}")
        print(f"Сумма: {total} руб.")

        if discount > 0:
            print(f"Скидка STUDENT (20%): {discount} руб.")

        print(f"------------------------------")
        print(f"💰 К ОПЛАТЕ: {final_price} руб.")
        print(f"==============================")

    else:
        print(f"Ошибка: количество должно быть больше 0")