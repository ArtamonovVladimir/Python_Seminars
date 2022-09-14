# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и
#    меньшее число. В качестве символа-разделителя используйте пробел.

from math import sqrt
stroka = '3, 4, 5, 6'
x = stroka.split(', ')
for i in range(len(x)):
    x[i] = int(x[i])
max_list = x[0]
min_list = x[0]
for i in x:
    if max_list < i:
        max_list = i
    if min_list > i:
        min_list = i
print(max_list, min_list)


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

#     1) с помощью математических формул нахождения корней квадратного уравнения

#     2) с помощью дополнительных библиотек Python

# D = b ** 2 - 4 * a * c
# x1 = (-b + sqrt(D)) // 2 * a
# x2 = (-b - sqrt(D)) // 2 * a


A = int(input('Число А: '))
B = int(input('Число B: '))
C = int(input('Число C: '))
D = B * B - 4 * A * C
if D > 0:
    x1 = ((-B) + D ** 0.5) / 2 * A
    x2 = ((-B) - sqrt(D)) / 2 * A
    print(round(x1, 3), round(x2, 3))
elif D == 0:
    x1 = (-B) / 2 * A
    print(x1)
else:
    print('корней нет')


# 3. Задайте два числа. Напишите программу, которая
#    найдёт НОК (наименьшее общее кратное) этих двух чисел.

# (Алгорит Евклида) - НОД
# НОК = (a * b) / НОД(a, b)

a = int(input())
b = int(input())
p = a * b

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
nod = a + b
nok = p // nod
print(nok)
