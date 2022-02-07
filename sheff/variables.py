from telebot.async_telebot import AsyncTeleBot


TOKEN = "TOKEN"
bot = AsyncTeleBot(TOKEN)
ids = set()
already_in_turn = set()
pizza = [("Маргарита", "mar543"),
         ("Пепперони", "pep054"),
         ("Пицца четыре сыра", "fch345")]
