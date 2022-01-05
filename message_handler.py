from logic import bot, markup_create_pizza, markup_create_break, edit_message, finall_steps, pizza_in_progress
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
    global pizza_in_progress
    if message.chat.id in pizza_in_progress :
        mes = bot.send_message(message.chat.id, text.order_in_progress)
        pizza_in_progress[message.chat.id].add(mes.message_id)
    else:
        pizza_in_progress[message.chat.id] = set()
        bot.send_message(message.chat.id, text.pizza_text, reply_markup=markup_create_pizza())


@bot.message_handler(commands=["order_info"])
def order_info(message):
    bot.send_message(message.chat.id, "In developing")


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
            finall_steps(text.order_done, call, None)
        elif call.data == '1':
            finall_steps(text.order_done, call, None)
        elif call.data == '2':
            finall_steps(text.order_done, call, None)
        elif call.data == '3':
            finall_steps(text.order_done, call, None)
        elif call.data == '4':
            finall_steps(text.order_done, call, None)
        elif call.data == '5':
            finall_steps(text.order_done, call, None)
        elif call.data == '6':
            finall_steps(text.order_done, call, None)


@bot.message_handler(content_types=['text'])
def message_ans(message):
    bot.reply_to(message, text.message_ans_text)


bot.infinity_polling()
