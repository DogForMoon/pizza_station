import telebot
import asyncio
import random
import time
import text
from variables import bot, pizza_in_progress, pizza
from DB_orders import get_orders, del_orders


def beauty_con(data):
    if data:
        res = "Вот твои заказы:\n\n"
        for i in data:
            p = [pizza[j][0] for j in range(len(pizza)) if pizza[j][1] == i[4]][0]
            t = time.ctime(i[2])
            res += text.beauty_text(i[0], p, i[3], t)
        return res
    return text.no_orders


def order_id():
    num0 = str(random.randint(100, 999))
    num1 = str(random.randint(100, 999))
    return num0 + num1


async def finall_steps(text_, call_, reply_):
    await bot.edit_message_text(text=text_,
                                chat_id=call_.message.chat.id,
                                message_id=call_.message.message_id,
                                reply_markup=reply_)
    for i in pizza_in_progress[call_.message.chat.id]:
        await bot.delete_message(call_.message.chat.id, i)
    del pizza_in_progress[call_.message.chat.id]


async def edit_message(text_, call_, reply_):
    await bot.edit_message_text(text=text_,
                                chat_id=call_.message.chat.id,
                                message_id=call_.message.message_id,
                                reply_markup=reply_)


def markup_create_pizza():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    for i in pizza:
        markup.add(telebot.types.InlineKeyboardButton(i[0],
                   callback_data=i[1]))
    return markup


def markup_create_break():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    t = time.localtime(time.time())
    t = t[3]*60 + t[4] + 50
    breaks = {"1-ая": (520, 560),
              "2-ая": (600, 615),
              "3-я": (655, 675),
              "4-ая": (715, 730),
              "5-ая": (770, 785),
              "6-ая": (825, 845),
              "7-ая": (23456, 23456)} #  885 900
    breaks_list = []
    for i in breaks:
        if t <= breaks[i][0]:
            breaks_list.append(i)
    if breaks_list:
        for i in breaks_list:
            markup.add(telebot.types.InlineKeyboardButton(i, callback_data=int(i[0])))
        return markup
    return False


def markup_create_onemore():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(telebot.types.InlineKeyboardButton("Добавить ещё один продукт в заказ", callback_data="onemore"))
    markup.add(telebot.types.InlineKeyboardButton("Продолжить оформление заказа", callback_data="stop"))
    return markup


def markup_create_ids(orders):
    markup = telebot.types.InlineKeyboardMarkup(row_width=4)
    for order in orders:
        markup.add(telebot.types.InlineKeyboardButton(order,
                                                      callback_data=order))
    return markup


async def ready_orders_checker():
    while True:
        data = get_orders()
        if data:
            for i in data:
                if del_orders(i[0]):
                    if i[-1] == "ready":
                        await bot.send_message(i[1], text.order_is_ready(i[0]))
                    elif i[-1] == "cancel":
                        await bot.send_message(i[1], text.order_is_cancel(i[0]))
                else:
                    await bot.send_message(i[1], text.error_text)
        time.sleep(5)


def ready_orders_checker_runner():
    asyncio.run(ready_orders_checker())
