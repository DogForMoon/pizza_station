import sqlite3
import os


def get_orders():
    cursor.execute("""SELECT * FROM orders""")
    results = cursor.fetchall()
    return results


def del_orders(order_id):
    try:
        cursor.execute(f"""DELETE FROM orders
                            WHERE orderid = {order_id};
                            """)
        connection.commit()
        return True
    except Exception as e:
        print(f'\n{e}\n')
        return False


connection = sqlite3.connect(os.getcwd() + '\\sheff\\orders.db',
                             check_same_thread=False)
cursor = connection.cursor()
