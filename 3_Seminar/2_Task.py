# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from math import ceil
import random

qty_elements = int(input('Введите количество элементов: '))
elements_list = []
new_array = []
for i in range(qty_elements):
    elements_list.append(random.randint(0, 10))

for i in range(ceil(qty_elements/2)):
    new_array.append(elements_list[i]*elements_list[-1-i])

print(elements_list)
print(f'Произведение пар чисел списка равна {new_array}')
