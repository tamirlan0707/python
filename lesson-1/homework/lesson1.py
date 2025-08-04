# lesson1

# task-1 Given a side of square. Find its perimeter and area.

side = float(input("Укажите ширину квадрата: "))
perimetr = 4 * side
area = side ** 2
print(f"Перимитр квадрата: {perimetr}")
print(f"Площадь квадрата: {area}")

# task-2 Given diameter of circle. Find its length.

import math
diameter = float(input("Введите диаметр круга: "))
length = math.pi * diameter
print(f"Длина окужности: {length}")

# task-3 Given two numbers a and b. Find their mean.

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
mean = (a+b) / 2
print(f"Среднее значение: {mean}")

# task-4 Given two numbers a and b. Find their sum, product and square of each number.

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
sum_ab = a+b
product_ab = a*b
square_a = a ** 2
square_b = b ** 2
print(f"Сумма: {sum_ab}")
print(f"Произведение: {product_ab}")
print(f"Квадрат первого числа: {square_a}")
print(f"Квадрат второго числа: {square_b}")
