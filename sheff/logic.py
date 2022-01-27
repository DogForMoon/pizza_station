from variables import bot, pizza, ids, already_in_turn
from DB_pizza import db_get
from time import sleep
import text
import telebot
import asyncio


def order_in_turn_markup(order_id, chat_id):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(telebot.types.InlineKeyboardButton(text.ready, callback_data=text.callback_ready(order_id, chat_id)))
    markup.add(telebot.types.InlineKeyboardButton(text.cancel, callback_data=text.callback_cancel(order_id, chat_id)))
    return markup


async def edit_message(text_, call_, reply_):
    await bot.edit_message_text(text=text_,
                                chat_id=call_.message.chat.id,
                                message_id=call_.message.message_id,
                                reply_markup=reply_)


def beauty_orders(i):
    global already_in_turn
    p = str()
    for j in pizza:
        if i[4] == j[1]:
            p = j[0]
            break
    b = text.beauty_order(i, p)
    already_in_turn.add(i[0])
    return b


async def checker():
    while True:
        data = db_get()
        if data:
            for i in data:
                if i[0] not in already_in_turn:
                    for j in ids:
                        await bot.send_message(j,
                                               beauty_orders(i),
                                               reply_markup=order_in_turn_markup(i[0], i[1]))
        sleep(5)


def checker_runner():
    asyncio.run(checker())
#  /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/wilfi/Desktop/pizza_station/sheff/logic.py
