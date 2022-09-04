# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи.

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


def fibonachi(number):
    n_1 = 0
    n_2 = 1
    if number == 0 or number == 1:
        print(f'Результат Фибоначи числа {number} равен 1')
    else:
        for i in range(2, number + 1):
            result = n_1 + n_2
            n_1 = n_2
            n_2 = result
        print(f'Результат Фибоначи числа {number} равен {result}')


number = input_data_check()
fibonachi(number)
