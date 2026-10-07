import random

status = input("Введите статус заказа: ")

match status:
    case "pending":
        time = random.randint(1, 3)
        print(f"📦 Статус: В ожидании")
        print(f"Описание: Заказ ожидает обработки")
        print(f"Примерное время: {time} ч.")

    case "processing":
        time = random.randint(1, 5)
        print(f"⚙️ Статус: В обработке")
        print(f"Описание: Ваш заказ обрабатывается")
        print(f"Примерное время: {time} ч.")

    case "shipped":
        time = random.randint(2, 5)
        print(f"✈️ Статус: Отправлено")
        print(f"Описание: Ваш заказ находится в пути")
        print(f"Примерное время: {time} дн.")

    case "delivered":
        print(f"✅ Статус: Доставлено")
        print(f"Описание: Заказ успешно доставлен")
        print(f"Примерное время: заказ уже доставлен")

    case "cancelled":
        print(f"❌ Статус: Отменено")
        print(f"Описание: Заказ был отменен")
        print(f"Примерное время: доставка отменена")

    case _:
        print(f"❌ Ошибка: неизвестный статус")
        print(f"Доступные статусы: pending, processing, shipped, delivered, cancelled")