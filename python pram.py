def rectangle_area(width, height):
    return width * height
 
# Пример использования функции
width = float(input("Введите ширину прямоугольника: "))
height = float(input("Введите высоту прямоугольника: "))
area = rectangle_area(width, height)
print("Площадь прямоугольника равна", area)