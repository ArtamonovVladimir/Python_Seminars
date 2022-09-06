# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

from operator import truediv


def input_data_check(col):
    # i = True
    text = ['x', 'y', 'z']
    xyz_list = []
    k = 0
    for k in range(col):
        print(k)
        i = True
        while i:
            try:
                input_number = int(
                    input(f'Введите число, обозначающее {text[k]}: '))
                i = False
                xyz_list.append(input_number)
            except ValueError:
                print('Ввод данных не верен, повторите ввод!')

    return xyz_list


def condition_check(xyz_check):
    if (not (xyz_check[0] or xyz_check[1] or xyz_check[2])) == (not (xyz_check[0]) and not (xyz_check[1]) and not (xyz_check[2])):
        print('ИСТИННО!')
    else:
        print('НЕТ, НЕ ИСТИННО!')


quantity = 3
xyz_cond = input_data_check(quantity)
condition_check(xyz_cond)
