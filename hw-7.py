# hw-7

import sqlite3

db_name = 'hw.db'


def create_table(sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            print("Таблица создана успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблицы: {e}")


def insert_product(product):
    try:
        sql = '''INSERT INTO products 
        (product_title, price, quantity)
        VALUES (?, ?, ?)
        '''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
            print(f"Товар '{product[0]}' добавлен успешно!")
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении товара: {e}")


def update_product_quantity(product_id, new_quantity):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (new_quantity, product_id))
            print(f"Количество товара с id {product_id} обновлено до {new_quantity}")
    except sqlite3.Error as e:
        print(f"Ошибка при обновлении количества: {e}")


def update_product_price(product_id, new_price):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (new_price, product_id))
            print(f"Цена товара с id {product_id} обновлена до {new_price}")
    except sqlite3.Error as e:
        print(f"Ошибка при обновлении цены: {e}")


def delete_product(product_id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (product_id,))
            print(f"Товар с id {product_id} удалён")
    except sqlite3.Error as e:
        print(f"Ошибка при удалении товара: {e}")


def select_all_products():
    try:
        sql = '''SELECT * FROM products'''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(f"Ошибка при выборке всех товаров: {e}")

def select_products_by_price_and_quantity(price_limit, quantity_limit):
    try:
        sql = '''SELECT * FROM products WHERE price < ? AND quantity > ?'''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (price_limit, quantity_limit))
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print(f"Нет товаров дешевле {price_limit} сом и с количеством больше {quantity_limit}.")
    except sqlite3.Error as e:
        print(e)

def search_products_by_title(search_term):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, ('%' + search_term + '%',))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(f"Ошибка при поиске товара: {e}")


sql_to_create_products_table = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price DECIMAL(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

create_table(sql_to_create_products_table)

products = [
    ('Мыло детское', 45.50, 10),
    ('Шампунь', 120.50, 5),
    ('Зубная паста', 80.00, 7),
    ('Гель для душа', 99.99, 4),
    ('Крем для рук', 60.00, 15),
    ('Жидкое мыло', 40.00, 20),
    ('Губка для мытья посуды', 20.00, 30),
    ('Зубная щетка', 55.00, 8),
    ('Маска для лица', 150.00, 3),
    ('Лосьон после бритья', 200.00, 5),
    ('Дезодорант', 90.00, 12),
    ('Пена для ванн', 130.00, 9),
    ('Крем для лица', 250.00, 4),
    ('Масло для волос', 175.00, 6),
    ('Пастила', 25.00, 50)
]

for product in products:
    insert_product(product)

update_product_quantity(1, 20)

update_product_price(2, 100.00)

delete_product(3)

print("\nВсе товары:")
select_all_products()

print("\nТовары дешевле 50 сом и с количеством больше 10:")
select_products_by_price_and_quantity(50, 10)

print("\nПоиск товаров по названию 'мыло':")
search_products_by_title('мыло')
