from telebot.async_telebot import AsyncTeleBot


TOKEN = "TOKEN"
bot = AsyncTeleBot(TOKEN)
pizza_id = str()

pizza = [("Маргарита", "mar543"),
         ("Пепперони", "pep054"),
         ("Пицца четыре сыра", "fch345")]

pizza_in_progress = {}
sticker = "CAACAgIAAxkBAAEDptlh2y0YYtVROH-2OuGj\
-AETTs77hgACMQADTGrIFxOa-QgbeyCZIwQ"
