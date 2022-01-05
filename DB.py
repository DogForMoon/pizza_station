import sqlite3

connection = sqlite3.connect('location.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS pizza(
    orderid INT,
    time INT,
    break INT,
    pizzaid INT,
    );
    """)

connection.commit()
