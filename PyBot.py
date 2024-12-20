import telebot

bot = telebot.TeleBot("8085889161:AAFa-keP9B8D2l8j6GbAYYRb5yY0xjmiNFU")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id,"ступид какроуч велкоме ту зе дед трэп?")
        bot.send_photo(message.chat.id, "https://i.pinimg.com/736x/fa/f9/52/faf9525d0295bcfeba156a6723c401d6.jpg")
    else:
        bot.send_message(message.from_user.id, "Чтобы начать, напиши команду /start")
bot.polling()