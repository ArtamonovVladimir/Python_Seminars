# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

def input_data_check():
    i = True
    while i:
        try:
            input_number = int(
                input('Введите число, которое будет для расчета точности числа Пи после запятой: '))
            i = False
        except ValueError:
            print('Ввод данных не верен, повторите ввод!')
    return input_number


def calculation_Pi(number):
    Pi = (1/16**0) * (4/(8 * 0 + 1) - 2 /
                      (8 * 0 + 4) - 1/(8 * 0 + 5) - 1/(8 * 0 + 6))
    for i in range(1, number):
        Pi += (1/16**i) * (4/(8 * i + 1) - 2 /
                           (8 * i + 4) - 1/(8 * i + 5) - 1/(8 * i + 6))
    return Pi


x = input_data_check()
print(round(calculation_Pi(x), x))
