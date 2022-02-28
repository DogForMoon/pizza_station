from variables import bot, ids
from time import sleep
import text
from logic import checker_runner, edit_message
from DB_orders import db_add
from DB_pizza import db_del
import threading
import asyncio


@bot.message_handler(commands=['start'])
async def start(message):
    global ids
    await bot.send_message(message.chat.id, text.start)
    await bot.send_message(message.chat.id, text.info)
    ids.add(message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data.split()[-1] == 'ready')
async def callback_ready(call):
    if call.message:
        print(call.data.split())
        if db_add(call.data.split()) and db_del(call.data.split()[0]):
            await edit_message(text.send_notification(call), call, None)
        else:
            await edit_message(text.error, call, None)


@bot.callback_query_handler(func=lambda call: call.data.split()[-1] == "cancel")
async def callback_cancel(call):
    if call.message:
        if db_add(call.data.split()) and db_del(call.data.split()[0]):
            await edit_message(text.delete, call, None)
        else:
            await edit_message(text.error, call, None)


t = threading.Thread(target=checker_runner)
t.start()

while True:
    try:
        asyncio.run(bot.infinity_polling())
    except:
        sleep(10)
