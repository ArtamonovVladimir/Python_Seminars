# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

from operator import truediv


def input_data_check():
    i = True
    while i:
        try:
            input_number = int(input(
                'Введите цифру, обозначающую день недели (от 1 до 7, включительно), которую проверим, является ли этот день выходным: '))
            i = False
        except ValueError:
            print('Ввод данных не верен, повторите ввод!')
    return input_number


def weekend_day_check(number):
    if number % 6 == 0 or number % 7 == 0:
        print(f'ДА. День {number} является выходным.')
    else:
        print(f'НЕТ. День {number} НЕ является выходным.')


day_number = input_data_check()
weekend_day_check(day_number)
