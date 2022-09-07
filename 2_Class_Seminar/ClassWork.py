# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81

n = int(input('Введите кол-во элементов в последовательности: '))
step = 1
for i in range(n):
    print(step, end=' ')
    step = step * (-3)

# решение в одну строку
print(*[(-3) ** i for i in range(int(input('Введите кол-во элементов в последовательности: ')))])


# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#     *Пример:*
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# d = {}
# d = dict()
# d[0] = 88003332211
# print(d)

n = int(input())
d = {}
# x = 1
for i in range(1, n + 1):
    d[i] = 3 * i + 1
    # x += 1
print(d)

# или
print({k: (3*k + 1) for k in range(1, n + 1)})


# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Пример:
#     1: мама мыла раму
#     2: ма
# Результат: 2

stroka1 = input()
stroka2 = input()
print(stroka1.count(stroka2))

# в питтоне есть индексы отрицательные
arr = [435, 241, 1, 34, 42]
#                    -2  -1
print(arr[-1])