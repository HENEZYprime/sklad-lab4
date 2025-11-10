import sqlite3
import os

def connect():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, '../db/sklad.db')
    return sqlite3.connect(db_path)

# ----- Product -----
def show_all_products():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Product")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def add_product(name, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Product (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    conn.close()

def update_product(product_id, name, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE Product SET name=?, price=? WHERE id=?", (name, price, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Product WHERE id=?", (product_id,))
    conn.commit()
    conn.close()

# ----- Customer -----
def add_customer(name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Customer (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def update_customer(customer_id, name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE Customer SET name=? WHERE id=?", (name, customer_id))
    conn.commit()
    conn.close()

def delete_customer(customer_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Customer WHERE id=?", (customer_id,))
    conn.commit()
    conn.close()

def show_all_customers():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Customer")
    for row in cursor.fetchall():
        print(row)
    conn.close()

# ----- Order -----
def add_order(customer_id, order_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO 'Order' (customer_id, order_date) VALUES (?, ?)",
        (customer_id, order_date)
    )
    conn.commit()
    conn.close()

def delete_order(order_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM 'Order' WHERE id=?", (order_id,))
    conn.commit()
    conn.close()

def show_all_orders():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM 'Order'")
    for row in cursor.fetchall():
        print(row)
    conn.close()

# ----- OrderItem -----
def add_order_item(order_id, product_id, quantity):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO OrderItem (order_id, product_id, quantity) VALUES (?, ?, ?)",
        (order_id, product_id, quantity)
    )
    conn.commit()
    conn.close()

def delete_order_item(item_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM OrderItem WHERE id=?", (item_id,))
    conn.commit()
    conn.close()

def show_all_order_items():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM OrderItem")
    for row in cursor.fetchall():
        print(row)
    conn.close()

# ===========================
if __name__ == "__main__":
    while True:
        cmd = input("Команда (add_customer, add_product, show_all, exit): ")
        if cmd == "add_customer":
            name = input("Имя клиента: ")
            add_customer(name)
        elif cmd == "add_product":
            name = input("Название товара: ")
            price = float(input("Цена: "))
            add_product(name, price)
        elif cmd == "show_all":
            print("\n--- Все товары ---")
            show_all_products()
            print("\n--- Все клиенты ---")
            show_all_customers()
            print("\n--- Все заказы ---")
            show_all_orders()
            print("\n--- Все позиции заказа ---")
            show_all_order_items()
        elif cmd == "exit":
            break
        else:
            print("Неизвестная команда")