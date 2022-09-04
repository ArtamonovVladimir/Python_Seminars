# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

from operator import truediv


def input_data_check():
    i = True
    while i:
        try:
            input_number = int(input(
                'Введите номер четверти (от 1 до 4, включительно): '))
            i = False
        except ValueError:
            print('Ввод данных не верен, повторите ввод!')
    return input_number


def quarter_coordinates_check(number):
    if number == 1:
        print(f"Координаты X > 0 и Y > 0")
    elif number == 2:
        print(f"Координаты X < 0 и Y > 0")
    elif number == 3:
        print(f"Координаты X < 0 и Y < 0")
    elif number == 4:
        print(f"Координаты X > 0 и Y < 0")
    else:
        print(f"Вы ввели несуществующую область!!!")


quarter = input_data_check()
quarter_coordinates_check(quarter)
