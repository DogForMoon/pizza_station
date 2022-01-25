from telebot.async_telebot import AsyncTeleBot


TOKEN = "5007353537:AAE-wXaPZDCOiBoJx8dIZGeaplQeE3pTZXA"
bot = AsyncTeleBot(TOKEN)
ids = set()
already_in_turn = set()
pizza = [("Маргарита", "mar543"),
         ("Пепперони", "pep054"),
         ("Пицца четыре сыра", "fch345")]
