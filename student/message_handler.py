from logic import bot, markup_create_pizza, markup_create_break,\
     edit_message, finall_steps, pizza_in_progress, order_id,\
          beauty_con, markup_create_ids
from DB import db_add, db_get, db_del
from variables import pizza_id, sticker
import text
import time


@bot.message_handler(commands=["start"])
async def welcome(message):
    await bot.reply_to(message, text.welcome_text)


@bot.message_handler(commands=["help"])
async def help_mes(message):
    await bot.reply_to(message, text.help_text)


@bot.message_handler(commands=["pizza"])
async def pizza(message):
    global pizza_in_progress
    if message.chat.id in pizza_in_progress:
        mes = await bot.send_message(message.chat.id, text.order_in_progress)
        pizza_in_progress[message.chat.id].add(mes.message_id)
    else:
        pizza_in_progress[message.chat.id] = set()
        await bot.send_message(message.chat.id,
                               text.pizza_text,
                               reply_markup=markup_create_pizza())


@bot.message_handler(commands=["orders_info"])
async def order_info(message):
    await bot.send_message(message.chat.id, beauty_con(db_get(message.chat.id)))


@bot.message_handler(commands=["cancel_order"])
async def cancel_order(message):
    orders = [i[0] for i in db_get(message.chat.id) if int(i[2])+2400 >= time.time()]
    if orders:
        await bot.send_message(message.chat.id,
                               text.delete_text,
                               reply_markup=markup_create_ids(orders))
    else:
        await bot.send_message(message.chat.id, text.no_orders_to_cancel)


@bot.message_handler(commands=['about'])
async def about_mes(message):
    await bot.send_message(message.chat.id, text.about_text)
    await bot.send_message(message.chat.id, text.technical_info)


@bot.message_handler(commands=["easter_egg"])
async def easter(message):
    await bot.send_message(message.chat.id, text.easter_text)
    await bot.send_sticker(message.chat.id, sticker)


@bot.callback_query_handler(func=lambda call: call.data in {"mar543", "pep054", "fch345"})
async def callback_pizza(call):
    if call.message:
        markup = markup_create_break()
        if markup:
            await edit_message(text.break_text, call, markup)
            global pizza_id
            pizza_id = call.data
        else:
            await finall_steps(text.not_time, call, None)


@bot.callback_query_handler(func=lambda call: call.data in {'1', '2', '3', '4', '5', '6', '7'})
async def callback_break(call):
    if call.message:
        order = order_id()
        data = [order,
                str(call.message.chat.id),
                str(time.time())[:10],
                call.data,
                pizza_id]
        if db_add(data):
            await finall_steps(text.order_done(order), call, None)
        else:
            await finall_steps(text.error_text, call, None)


@bot.callback_query_handler(func=lambda call: call.data.isnumeric() and int(call.data) in [i[0] for i in db_get(call.message.chat.id)])
async def callback_del(call):
    if call.message:
        if db_del(call.data):
            await edit_message(text.order_del(call.data), call, None)
        else:
            await edit_message(text.error_text, call, None)


@bot.message_handler(content_types=['text'])
async def message_ans(message):
    await bot.reply_to(message, text.message_ans_text)


import asyncio
asyncio.run(bot.polling())
