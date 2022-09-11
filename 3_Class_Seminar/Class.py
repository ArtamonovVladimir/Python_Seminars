# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора
# псевдослучайных чисел. (https://proglib.io/p/psutil-in-python)

# import time
# from random import randint

# arr = list()
# for i in range(10):
#     number = randint(1, 5)
#     time.sleep(1)
#     arr.append(int(str(time.time())[-number:]))
# print(*arr)


# 2. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

# arr = ['bbb21dd', 'Hello', 'World']
# n = '21'
# flag = False
# for stroka in arr:
#     if n in stroka:
#         flag = True
#         print('yes')
# if flag == False:
#     print('no')


# 3. Напишите программу, которая определит позицию второго вхождения
#  строки в списке либо сообщит, что её нет.
# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

arr = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
print(arr)
search = input()
count = 0
index = 0
i = 0
while count < 2 and i < len(arr):
    if arr[i] == search:
        index = i
        count += 1
    i += 1
if count == 2:
    print(index)
else:
    print('Not found')

# From Denis

list_1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
string = input('введите строку: ')
count = 0
i = 0
flag = True
while i < len(list_1) and flag:
    if string == list_1[i]:
        count += 1
        if count == 2:
            flag = False
            print(i)
    i += 1

if flag:
    print(-1)


# Доп задачка: https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=6&id_topic=117&id_problem=723
