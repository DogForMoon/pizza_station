import telebot
from variables import bot, pizza, ids, already_in_turn
from DB_pizza import db_get
from time import sleep, ctime
import telebot
import asyncio


def order_in_turn_markup(chat_id):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(telebot.types.InlineKeyboardButton("Заказ готов", callback_data=f"ready {chat_id}"))
    markup.add(telebot.types.InlineKeyboardButton("Отменить заказ", callback_data=(f"cancel {chat_id}")))
    return markup


def beauty_orders(i):
    global already_in_turn
    p = str()
    for j in pizza:
        if i[4] == j:
            p = j[0]
            break
    b = f"id заказа: {i[0]}\nвремя заказа: {ctime(i[2])}\nперемена выдачи: {i[3]}\nнаименование товара: {p}"
    already_in_turn.add(i[0])
    return b


async def checker():
    while True:
        data = db_get()
        if data:
            for i in data:
                for j in ids:
                    if i[0] not in already_in_turn:
                        await bot.send_message(j, beauty_orders(i), reply_markup=order_in_turn_markup(i[1]))
        sleep(10)


def checker_runner():
    asyncio.run(checker())
#  /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/wilfi/Desktop/pizza_station/sheff/logic.py
