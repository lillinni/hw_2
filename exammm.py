import sqlite3

conn = sqlite3.connect('store_inventory2.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    code VARCHAR(2) PRIMARY KEY,
    title VARCHAR(150)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS store (
    store_id INTEGER PRIMARY KEY,
    title VARCHAR(100)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    title VARCHAR(250),
    category_code VARCHAR(2),
    unit_price FLOAT,
    stock_quantity INTEGER,
    store_id INTEGER,
    FOREIGN KEY (category_code) REFERENCES categories (code),
    FOREIGN KEY (store_id) REFERENCES store (store_id)
)
''')

categories = [
    ('FD', 'Food'),
    ('CL', 'Clothes'),
    ('EL', 'Electronics'),
    ('HM', 'Home Appliances'),
    ('BK', 'Books'),
    ('SN', 'Snacks')
]

for code, title in categories:
    cursor.execute("INSERT OR IGNORE INTO categories (code, title) VALUES (?, ?)", (code, title))

stores = [
    (1, 'Asia'),
    (2, 'Globus'),
    (3, 'Spar'),
    (4, 'Metro'),
    (5, 'Perekrestok'),
    (6, 'Auchan')
]

for store_id, title in stores:
    cursor.execute("INSERT OR IGNORE INTO store (store_id, title) VALUES (?, ?)", (store_id, title))

products = [
    (1, 'Chocolate', 'FD', 10.5, 129, 1),
    (2, 'Apple', 'FD', 2.0, 200, 2),
    (3, 'T-shirt', 'CL', 15.0, 75, 3),
    (4, 'Laptop', 'EL', 1200.0, 30, 4),
    (5, 'Vacuum Cleaner', 'HM', 250.0, 20, 5),
    (6, 'Cooking Book', 'BK', 25.0, 50, 6),
    (7, 'Banana', 'FD', 0.5, 300, 2),
    (8, 'Jeans', 'CL', 40.0, 40, 3),
    (9, 'Smartphone', 'EL', 800.0, 15, 4),
    (10, 'Toaster', 'HM', 45.0, 10, 5),
    (11, 'Snickers', 'SN', 1.2, 100, 1),
    (12, 'Novel', 'BK', 15.0, 60, 6)
]

for product_id, title, category_code, unit_price, stock_quantity, store_id in products:
    cursor.execute(
        "INSERT OR IGNORE INTO products (id, title, category_code, unit_price, stock_quantity, store_id) VALUES (?, ?, ?, ?, ?, ?)",
        (product_id, title, category_code, unit_price, stock_quantity, store_id)
    )

conn.commit()

def display_products(store_id):
    cursor.execute('''
    SELECT products.title, categories.title, products.unit_price, products.stock_quantity
    FROM products
    JOIN categories ON products.category_code = categories.code
    WHERE products.store_id = ?
    ''', (store_id,))
    
    products = cursor.fetchall()
    
    if products:
        for product in products:
            print(f"Название продукта: {product[0]}")
            print(f"Категория: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество на складе: {product[3]}\n")
    else:
        print("В этом магазине нет доступных продуктов.\n")

def main():
    while True:
        print("Вы можете отобразить список продуктов по выбранному id магазина из")
        print("перечня магазинов ниже, для выхода из программы введите цифру 0:")
        
        cursor.execute("SELECT store_id, title FROM store")
        stores = cursor.fetchall()
        
        for store in stores:
            print(f"{store[0]}: {store[1]}")
        
        user_input = input("Введите ID магазина (или 0 для выхода): ")
        
        if user_input == '0':
            break
        
        try:
            store_id = int(user_input)
            if store_id in [store[0] for store in stores]:
                display_products(store_id)
            else:
                print("Неверный ID магазина. Попробуйте снова.\n")
        except ValueError:
            print("Пожалуйста, введите корректный ID магазина.\n")

if __name__ == '__main__':
    main()

conn.close()
