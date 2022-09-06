# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

def input_data_check():
    i = True
    while i:
        try:
            input_number = int(
                input('Введите число ддя поиска его наименьшего натурального делителя: '))
            if input_number <= 1:
                print('Попробуйте ввести еще раз и число больше 0')
                continue
            i = False
        except ValueError:
            print('Ввод данных не верен, повторите ввод!')
    return input_number


number = input_data_check()
if number % 2 == 0:
    print('Наименьший натуральный делитель равен 2')
elif number % 3 == 0:
    print('Наименьший натуральный делитель равен 3')
else:
    for i in range(5, number + 1, 2):
        # print(i)
        if number % i == 0:
            print(f'Наименьший натуральный делитель равен {i}')
            break
