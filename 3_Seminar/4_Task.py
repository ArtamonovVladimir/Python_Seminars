# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def input_data_check():
    i = True
    while i:
        try:
            input_number = int(
                input('Введите число, которое будем переводить в двоичную систему исчисления: '))
            i = False
        except ValueError:
            print('Ввод данных не верен, повторите ввод!')
    return input_number


number = input_data_check()
new_number = ''
while number > 0:
    new_number = str(number % 2) + new_number
    number = number // 2
print(f'Число в двоичной системе исчисления будет равно {new_number}')
