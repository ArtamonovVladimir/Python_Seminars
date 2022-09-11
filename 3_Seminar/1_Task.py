# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random

qty_elements = int(input('Введите количество элементов: '))
elements_list = []
sum = 0
for i in range(qty_elements):
    elements_list.append(random.randint(0, 10))
    if i % 2 != 0:
        sum += elements_list[i]

print(elements_list)
print(f'Сумма элементов списка, стоящих на нечётной позиции равна {sum}')
