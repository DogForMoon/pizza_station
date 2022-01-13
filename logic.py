import telebot
import random
import time
import text
from variables import bot, pizza_in_progress, pizza


def beauty_con(data):
    if data:
        res = "Вот твои заказы:\n\n"
        for i in data:
            p = [pizza[j][0] for j in range(len(pizza)) if pizza[j][1] == i[4]][0]
            t = time.ctime(i[2])
            res += f"id заказа: {i[0]}\nпицца: {p}\nперемена: {i[3]}\nвремя заказа: {t}\n\n"
        return res
    return text.no_orders


def order_id():
    num0 = str(random.randint(100, 999))
    num1 = str(random.randint(100, 999))
    return num0 + num1


def finall_steps(text_, call_, reply_):
            bot.edit_message_text(text=text_, chat_id=call_.message.chat.id, message_id=call_.message.message_id, reply_markup=reply_)
            for i in pizza_in_progress[call_.message.chat.id]:
                bot.delete_message(call_.message.chat.id, i)
            del pizza_in_progress[call_.message.chat.id]


def edit_message(text_, call_, reply_):
    return bot.edit_message_text(text=text_, chat_id=call_.message.chat.id, message_id=call_.message.message_id, reply_markup=reply_)


def markup_create_pizza():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    for i in pizza:
        markup.add(telebot.types.InlineKeyboardButton(i[0], callback_data=i[1]))
    return markup


def markup_create_break():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    breaks = ["1-ая", "2-ая", "3-я", "4-ая", "5-ая", "6-ая", "7-ая"]
    for i in range(len(breaks)):
        markup.add(telebot.types.InlineKeyboardButton(breaks[i], callback_data=str(i)))
    return markup


def markup_create_ids(orders):
    markup = telebot.types.InlineKeyboardMarkup(row_width=4)
    for order in orders:
        markup.add(telebot.types.InlineKeyboardButton(order, callback_data=order))
    return markup
