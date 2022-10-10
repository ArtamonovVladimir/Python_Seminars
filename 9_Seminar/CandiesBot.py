# Игра в конфеты через Телеграм Бота


from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5503815330:AAHXdJCZCBQQFMWFg3NsqjwZemGRUj0jUAg')
updater = Updater(token='5503815330:AAHXdJCZCBQQFMWFg3NsqjwZemGRUj0jUAg')
dispatcher = updater.dispatcher

number_candies = 0
candy_step = 0


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите количество конфет в розыгрыше:')

def count_candies(update, context):
    global number_candies
    i = True
    while i:
        try:
            number_candies = int(update.message.text)
            i = False
        except ValueError:
            context.bot.send_message(update.effective_chat.id, 'Ввод данных не верен, повторите ввод!')            
    


# def candy_check(qty, max_step):
#     i = True
#     while i:
#         try:
#             input_number = int(input('Ваш ход: '))
#             if input_number > max_step or input_number > qty:
#                 print(
#                     f' Вы превысили кол-во за один ход {max_step} или кол-во оставшихся конфет {qty}')
#                 continue
#             i = False
#         except ValueError:
#             print('Ввод данных не верен, повторите ввод!')
#     return input_number


# def play_pc(candies, max, level):
#     if level == 1:
#         pc_take = int(candies % (max+1))
#     else:
#         if max <= candies:
#             pc_take = rd.randint(1, max)
#         else:
#             pc_take = rd.randint(1, candies)
#     return pc_take


# def game_play(qty_candy, level, first, max):
#     f = 0
#     if first != 1:
#         f = 2
#     while qty_candy > 0:
#         if f == 2:
#             step = play_pc(qty_candy, max, level)
#             print(f'Играет ПК: {step}')
#             f = 1
#         else:
#             step = candy_check(qty_candy, max)
#             f = 2
#         qty_candy -= step
#         print(f'Конфет осталось {qty_candy}')
#     if f == 2:
#         print('Победили Вы!')
#     else:
#         print('Победил ПК :(')


# candies_qty = input_data_check(
#     'Введите количество конфет, которое будет разыграно: ')
# candies_step = input_data_check(
#     'Введите количество конфет, которое можно максимум взять за ход: ')
# diff_level = input_data_check(
#     'Введите уровень сложности игры с ПК (1 - сложно, 2 - стандартно): ')
# first_player = input_data_check(
#     'Введите кто начнет первым (1 - Вы, 2 - ПК): ')

def message(update, context):
    text = update.message.text
    words = text.split(' ')
    some_new = []
    for i in words:
        if 'абв' not in i:
            some_new.append(i)
    new_text = ' '.join(some_new)
    context.bot.send_message(update.effective_chat.id,
                             f'Как-то так: {new_text}')

start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()  # ctrl + c