from variables import bot


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "")


@bot.message_handler(commands=["show"])
def show(message):
    bot.send_message(message.chat.id, "")


bot.infinity_polling()
