from time import ctime


def callback_ready(order_id, chat_id):
    return f"ready {order_id} {chat_id}"


def callback_cancel(order_id, chat_id):
    return f"cancel {order_id} {chat_id}"


def send_notification(call_):
    return f"Ученику отправлено уведомление о готовности заказа №{call_.data.split()[1]}"


def beauty_order(i, p):
    return f"id заказа: {i[0]}\nвремя заказа: {ctime(i[2])}\nперемена выдачи: {i[3]}\nнаименование товара: {p}"


error = "Произошла ошибка на сервере. Попробуйте позже"
ready = "заказ готов"
cancel = "Отменить заказ"
start = "Инициирую запуск"
info = "Чат-бот автоматически обновляет заказы. Когда заказ отдан, он удаляется"
