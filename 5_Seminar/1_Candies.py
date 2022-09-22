import random as rd


def input_data_check(text):
    i = True
    while i:
        try:
            input_number = int(input(f'{text}'))
            i = False
        except ValueError:
            print('Ввод данных не верен, повторите ввод!')
    return input_number


def candy_check(qty, max_step):
    i = True
    while i:
        try:
            input_number = int(input('Ваш ход: '))
            if input_number > max_step or input_number > qty:
                print(
                    f' Вы превысили кол-во за один ход {max_step} или кол-во оставшихся конфет {qty}')
                continue
            i = False
        except ValueError:
            print('Ввод данных не верен, повторите ввод!')
    return input_number


def play_pc(candies, max, level):
    if level == 1:
        pc_take = int(candies % (max+1))
    else:
        if max <= candies:
            pc_take = rd.randint(1, max)
        else:
            pc_take = rd.randint(1, candies)
    return pc_take


def game_play(qty_candy, level, first, max):
    f = 0
    if first != 1:
        f = 2
    while qty_candy > 0:
        if f == 2:
            step = play_pc(qty_candy, max, level)
            print(f'Играет ПК: {step}')
            f = 1
        else:
            step = candy_check(qty_candy, max)
            f = 2
        qty_candy -= step
        print(f'Конфет осталось {qty_candy}')
    if f == 2:
        print('Победили Вы!')
    else:
        print('Победил ПК :(')


candies_qty = input_data_check(
    'Введите количество конфет, которое будет разыграно: ')
candies_step = input_data_check(
    'Введите количество конфет, которое можно максимум взять за ход: ')
diff_level = input_data_check(
    'Введите уровень сложности игры с ПК (1 - сложно, 2 - стандартно): ')
first_player = input_data_check(
    'Введите кто начнет первым (1 - Вы, 2 - ПК): ')


game_play(candies_qty, diff_level, first_player, candies_step)
