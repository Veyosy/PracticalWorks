# - значение числа пи
PI = 3.14


# - функция расчета площади прямоугольника
def calculate_rectangle_area(width, height):
    """
    Вычисляет площадь прямоугольника.

    Args:
        width (float): Ширина прямоугольника.
        height (float): Высота прямоугольника.

    Returns:
        float: Площадь прямоугольника.
    """
    return width * height


# - функция расчета площади круга
def calculate_circle_area(radius):
    """
    Вычисляет площадь круга.

    Args:
        radius (float): Радиус круга.

    Returns:
        float: Площадь круга.
    """
    return PI * radius ** 2


# - ввод ширины и высоты прямоугольника
width, height = map(
    float,
    input("Введите ширину и высоту прямоугольника: ").split()
)

# - расчет площади прямоугольника
rectangle_area = calculate_rectangle_area(width, height)

# - ввод радиуса круга
radius = float(input("Введите радиус круга: "))

# - расчет площади круга
circle_area = calculate_circle_area(radius)

# - вывод результатов
print(f"Площадь прямоугольника: {rectangle_area:.2f}")
print(f"Площадь круга: {circle_area:.2f}")