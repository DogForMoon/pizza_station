import telebot
import json


TOKEN = "5002588810:AAH42vrIteF9F2aJYwNeY2RS9HU370OT6AQ"
bot = telebot.TeleBot(TOKEN)
pizza = [("Маргарита", "mar543"), ("Пепперони", "pep054"), ("Пицца четыре сыра", "fch345")]
pizza_in_progress = {}


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
