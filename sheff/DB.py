import sqlite3
import os


def db_get(chat_id):
    cursor.execute(f"""SELECT * FROM pizza
                        WHERE chatid = {chat_id};
                        """)
    results = cursor.fetchall()
    return results


def db_del(order_id):
    try:
        cursor.execute(f"""DELETE FROM pizza
                            WHERE orderid = {order_id};
                            """)
        connection.commit()
        return True
    except Exception as e:
        print(f'\n{e}\n')
        return False


connection = sqlite3.connect(os.getcwd + 'sheff\\pizza.db',
                             check_same_thread=False)
cursor = connection.cursor()
