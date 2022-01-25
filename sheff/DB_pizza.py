import sqlite3
import os


def db_get():
    cursor.execute(f"""SELECT * FROM pizza""")
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


connection = sqlite3.connect(os.getcwd() + '\\student\\pizza.db',
                             check_same_thread=False)
cursor = connection.cursor()
