from gc import callbacks

import telebot
from telebot import types
bot = telebot.TeleBot("8085889161:AAFa-keP9B8D2l8j6GbAYYRb5yY0xjmiNFU")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        obj = types.InlineKeyboardMarkup()
        bttn1 = types.InlineKeyboardButton('Начало',callback_data='1')
        bttn2 = types.InlineKeyboardButton('Синтаксис',callback_data='2')
        bttn3 = types.InlineKeyboardButton('Типы данных', callback_data='3')
        bttn4 = types.InlineKeyboardButton('Условные операторы', callback_data='4')
        bttn5 = types.InlineKeyboardButton('Циклы', callback_data='5')
        bttn6 = types.InlineKeyboardButton('Конец', callback_data='6')
        obj.row(bttn1,bttn2,)
        obj.row(bttn3,bttn4,)
        obj.row(bttn5, bttn6, )
        bot.send_message(message.from_user.id, "текст",reply_markup=obj)
    else:
        bot.send_message(message.from_user.id, "ступид какроуч велкоме ту зе дед трэп")


bot.polling()

