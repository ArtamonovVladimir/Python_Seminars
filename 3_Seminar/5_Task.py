# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def input_data_check():
    i = True
    while i:
        try:
            input_number = int(
                input('Введите положительное число N, для расчета последовательности Фибоначи: '))
            i = False
        except ValueError:
            print('Ввод данных не верен, повторите ввод!')
    return input_number


def fibonachi_plus(number):
    n_1 = 0
    n_2 = 1
    if number == 0 or number == 1:
        return 1
    else:
        for i in range(2, number + 1):
            result = n_1 + n_2
            n_1 = n_2
            n_2 = result
        return result


def fibonachi_minus(number):
    number = - number
    result = (-1)**(number+1)*fibonachi_plus(number)
    return result


input_number = input_data_check()
fibonachi = []
for i in range(-input_number, input_number + 1):
    if i == 0:
        fibonachi.append(0)
    elif i < 0:
        fibonachi.append(fibonachi_minus(i))
    elif i > 0:
        fibonachi.append(fibonachi_plus(i))

print(fibonachi)
