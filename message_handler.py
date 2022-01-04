from logic import bot, markup_create_pizza, markup_create_break, edit_message
import text
import telebot

@bot.message_handler(commands=["start"])
def welcome(message):
    bot.reply_to(message, text.welcome_text)


@bot.message_handler(commands=["help"])
def help_mes(message):
    bot.reply_to(message, text.help_text)


@bot.message_handler(commands=["pizza"])
def pizza(message):
    bot.send_message(message.chat.id, text.pizza_text, reply_markup=markup_create_pizza())


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == "mar543":
            edit_message(text.break_text, call, markup_create_break())
        elif call.data == "pep054":
            edit_message(text.break_text, call, markup_create_break())
        elif call.data == "fch345":
            edit_message(text.break_text, call, markup_create_break())
        if call.data == '0':
            edit_message(text.order_done, call, None)
        elif call.data == '1':
            edit_message(text.order_done, call, None)
        elif call.data == '2':
            edit_message(text.order_done, call, None)
        elif call.data == '3':
            edit_message(text.order_done, call, None)
        elif call.data == '4':
            edit_message(text.order_done, call, None)
        elif call.data == '5':
            edit_message(text.order_done, call, None)
        elif call.data == '6':
            edit_message(text.order_done, call, None)


@bot.callback_query_handler(func=lambda call: True)
def test_callback(call): # <- passes a CallbackQuery type object to your function
    telebot.logger.info(call)


@bot.message_handler(content_types=['text'])
def message_ans(message):
    bot.reply_to(message, text.message_ans_text)


bot.infinity_polling()
