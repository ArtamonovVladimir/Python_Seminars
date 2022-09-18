# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math


def input_data_check():
    i = True
    while i:
        try:
            input_number = int(
                input('Введите натуральное число N: '))
            i = False
        except ValueError:
            print('Ввод данных не верен, повторите ввод!')
    return input_number


def multiplier(number):
    multy = list()
    print(math.ceil(number**0.5))
    for i in range(2, math.ceil(number**0.5)):
        while number % i == 0:
            multy.append(i)
            number /= i
    if number != 1:
        multy.append(number)
    return multy


print(multiplier(input_data_check()))
