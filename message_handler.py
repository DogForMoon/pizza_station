from logic import bot, markup_create_pizza, markup_create_break, edit_message, finall_steps, pizza_in_progress, order_id, beauty_con, markup_create_ids
from DB import db_add, db_get, db_del
from variables import pizza_id
import text
import time


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


@bot.message_handler(commands=["orders_info"])
def order_info(message):
    bot.send_message(message.chat.id, beauty_con(db_get(message.chat.id)))


@bot.message_handler(commands=["cancel_order"])
def cancel_order(message):
    orders = [i[0] for i in db_get(message.chat.id)]
    bot.send_message(message.chat.id, text.delete_text, reply_markup=markup_create_ids(orders))


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data in {"mar543", "pep054", "fch345"}:
            edit_message(text.break_text, call, markup_create_break())
            global pizza_id
            pizza_id = call.data

        if call.data in {'0', '1', '2', '3', '4', '5', '6'}:
            order = order_id()
            data = [order, str(call.message.chat.id), str(time.time())[:10], call.data, pizza_id]
            if db_add(data):
                finall_steps(text.order_done(order), call, None)
            else:
                finall_steps(text.error_text, call, None)
        
        if int(call.data) in [i[0] for i in db_get(call.message.chat.id)]:
            if db_del(call.data):
                edit_message(text.order_del(call.data), call, None)
            else:
                edit_message(text.error_text, call, None)


@bot.message_handler(content_types=['text'])
def message_ans(message):
    bot.reply_to(message, text.message_ans_text)


bot.infinity_polling()
