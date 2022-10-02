# 1.Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random as rd


def input_data_check():
    i = True
    while i:
        try:
            input_number = int(
                input('Введите какое кол-во оценок сгенирировать: '))
            i = False
        except ValueError:
            print('Ввод данных не верен, повторите ввод!')
    return input_number


def get_random_number():
    rand_num = rd.randint(1, 5)
    return rand_num


numbers = []
min = 5
max = 1
in_num = input_data_check()
for i in range(0, in_num):
    number = get_random_number()
    if min > number:
        min = number
    elif max < number:
        max = number
    numbers.append(number)

print(f'Вввод: {numbers}\n')
new_numbers = [min if number == max else number for number in numbers]
print(f'Выввод: {new_numbers}\n')
