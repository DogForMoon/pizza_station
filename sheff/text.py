from time import ctime
from variables import pizza_cat


def callback_ready(order_id, chat_id):
    return f"{order_id} {chat_id} ready"


def callback_cancel(order_id, chat_id):
    return f"{order_id} {chat_id} cancel"
  

def send_notification(call_):
    return f"Ученику отправлено уведомление о готовности заказа №{call_.data.split()[0]}"


def beauty_order(i):
    p = i[4]
    p_beaut = str()
    prev = int()
    for k in range(6, len(p)+6, 6):
        pizza_id = p[prev:k]
        for l in pizza_cat:
            for pro in pizza_cat[l]:
                if pro[1] == pizza_id:
                    p_beaut += f"\n~{pro[0]},"
        prev = k
    p_beaut = p_beaut[:-2]
    return f"id заказа: {i[0]}\nвремя заказа: {ctime(i[2])}\nперемена выдачи: {i[3]}\nнаименования: {p_beaut}"


error = "Произошла ошибка на сервере. Попробуйте позже"
ready = "заказ готов"
delete = "Заказ удалён"
cancel = "Отменить заказ"
start = "Инициирую запуск"
info = "Чат-бот автоматически обновляет заказы. Когда заказ отдан, он удаляется"
