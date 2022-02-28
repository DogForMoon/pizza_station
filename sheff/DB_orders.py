from msilib.schema import Error
import sqlite3
import os


def db_add(data):
    try:
        cursor.execute("INSERT INTO orders VALUES(?, ?, ?)", data)
        connection.commit()
        return True
    except Error:
        return False


connection = sqlite3.connect(os.getcwd() + '\\sheff\\orders.db',
                             check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS orders
    (
    orderid INT,
    chatid INT,
    status STR
    )""")

connection.commit()
