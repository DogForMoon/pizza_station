import telebot


TOKEN = "5002588810:AAH42vrIteF9F2aJYwNeY2RS9HU370OT6AQ"
bot = telebot.TeleBot(TOKEN)
pizza_id = str()
pizza = [("Маргарита", "mar543"), ("Пепперони", "pep054"), ("Пицца четыре сыра", "fch345")]
pizza_in_progress = {}
sticker = "CAACAgIAAxkBAAEDptlh2y0YYtVROH-2OuGj-AETTs77hgACMQADTGrIFxOa-QgbeyCZIwQ"