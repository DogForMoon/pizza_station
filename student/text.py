def order_del(order):
    deleted_order = f"Заказ с id {order} успешно удалён"
    return deleted_order


def order_is_cancel(order_id):
    return f"Заказ №{order_id} был отменён поваром"


def order_is_ready(order_id):
    return f"Заказ №{order_id} ждёт тебя! Ты можешь забрать его в буфете"


def order_done(order):
    order_done_ = f"Твой заказ уже готовится!\nВот id твоего заказа:\
 {order}\nЕсли хочешь узнать информацию по своему заказу,\
 отправь /orders_info\nЕсли хочешь удалить свой заказ\
 отправь /cancel_order"
    return order_done_


def beauty_text(i_0, p, i_3, t):
    return f"id заказа: {i_0}\nпицца: {p}\nперемена: {i_3}\nвремя\
 заказа: {t}\n\n"


welcome_text = """Привет! Это чат-бот для заказа пиццы.
Пиши /pizza и оформляй заказ!
Если хочешь узнать что я умею, пиши /help"""

help_text = """Вот что я умею:
/pizza - оформление заказа пиццы
/orders_info - узнать информацию по заказам
/cancel_order - удалить заказ
/about - информация о чат-боте и создателях"""

message_ans_text = "Я не умею отвечать на сообщения, только на команды😕"

pizza_text = "Я гляжу, ты решил выбрать пиццу! Смотри, что у меня есть:"

break_text = "Отличный вкус! Теперь выбери перемену к которой её приготовить:"

order_in_progress = "Походу ты не завершил оформление заказа. Попробуй\
 снова после того, как закончишь с предыдущим заказом"

error_text = "Упс.. На сервере технические шоколадки"

delete_text = "Выбери id заказа, который хочешь удалить:"

no_orders = "У тебя нет заказов в очереди"

no_orders_to_cancel = "У тебя нет заказов, которые можно отменить"

not_time = "Сегодня уже нельзя заказать пиццу. Возвращайся завтра"

about_text = """Как ты уже понял это школьный проект. Над проектом работали\
 Лёша Алексеев (дизайн, техническая информация) и Игорь Михелев\
 (разработчик), а также руководитель проекта Игорь Александрович.
Если ты заметил какие-то ошибки в работе бота или у тебя есть предложения пиши\
 сюда -> @wilfii"""

technical_info = """Немного занудства от разработчика ~_~
1. Заказать пиццу можно только в день выдачи.
2. Удалить заказ можно максимум за урок до выдачи пиццы (за 40 минут, если\
 быть точнее). Поэтому если в меню удаления заказов нету того, который\
 ты хочешь удалить, значит время вышло.
3. Заказать пиццу также можно только на следующую перемену (50 минут, чтобы\
 было время отменить заказ)
Занудство закончилось UWU"""

easter_text = 'О, ты нашёл пасхалку. Держи бесплатную пиццу'

one_more_order = "Хочешь что-нибудь добавить в свой заказ?"
