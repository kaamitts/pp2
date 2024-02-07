import math

def polygon_area(sides):
    n = len(sides)
    if n < 3:
        return 0  # Многоугольник с меньше чем 3 сторонами не имеет площади

    perimeter = sum(sides)
    s = perimeter / 2
    area = math.sqrt(s)
    for side in sides:
        area *= (s - side)
    return math.sqrt(area)

# Пример использования функции:
sides = [float(input(f"Введите длину стороны {i + 1}: ")) for i in range(int(input("Введите количество сторон многоугольника: ")))]
area = polygon_area(sides)
print("Площадь многоугольника:", area)