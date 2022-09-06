# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

def input_data_check():
    i = True
    while i:
        try:
            input_number = int(input('Введите число: '))
            if input_number == 0 or input_number < 0:
                print('Попробуйте ввести еще раз и число больше 0')
                continue
            i = False
        except ValueError:
            print('Ввод данных не верен, повторите ввод!')
    return input_number


sum = 0
number = input_data_check()
for i in range(1, number + 1):
    sum += i
print(f'Сумма чисел между 1 и {number} равна {sum}')
