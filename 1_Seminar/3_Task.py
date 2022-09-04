# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

from operator import truediv
import random


def get_random_number(min, max):
    rand_num = random.randint(min, max)
    return rand_num


def condition_check(x, y):
    # x = int(x_coord)
    # y = int(y_coord)
    if x == 0 or y == 0:
        print(f"Координаты X {x} и/или Y {y} равны нулю")
    elif x > 0 and y > 0:
        print(f"Координаты X {x} и Y {y} находится в Первой четверти")
    elif x < 0 and y > 0:
        print(f"Координаты X {x} и Y {y} находится в Второй четверти")
    elif x < 0 and y < 0:
        print(f"Координаты X {x} и Y {y} находится в Третей четверти")
    elif x > 0 and y < 0:
        print(f"Координаты X {x} и Y {y} находится в Четвертая четверть")


x_coordinate = get_random_number(-9999999999, 9999999999)
y_coordinate = get_random_number(-9999999999, 9999999999)
condition_check(x_coordinate, y_coordinate)
