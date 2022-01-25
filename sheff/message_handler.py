from variables import bot, ids
from time import sleep
from logic import checker_runner
import threading
import asyncio


@bot.message_handler(commands=['start'])
async def start(message):
    global ids
    await bot.send_message(message.chat.id, "Инициирую запуск")
    await bot.send_message(message.chat.id, "Чат-бот автоматически обновляет заказы. Когда заказ отдан, он удаляется")
    ids.add(message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data.split()[0] == 'ready')
async def callback_ready(call):
    if call.message:
        # отправляем сообщение ученику, что заказ готов
        pass


@bot.callback_query_handler(func=lambda call: call.data.split()[0] == "cancel")
async def callback_cancel(call):
    if call.message:
        # отправляем сообщение о удалении заказа, удаляем из базы
        pass


t = threading.Thread(target=checker_runner)
t.start()

while True:
    try:
        asyncio.run(bot.infinity_polling()) #  bot.polling(none_stop=True, interval=0)
    except:
        sleep(10)
