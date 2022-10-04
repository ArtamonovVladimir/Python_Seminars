
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5503815330:AAHXdJCZCBQQFMWFg3NsqjwZemGRUj0jUAg')
updater = Updater(token='5503815330:AAHXdJCZCBQQFMWFg3NsqjwZemGRUj0jUAg')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите текст, из которого нужно удалить слова с словосочетанием "абв":')


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
