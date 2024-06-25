import sqlite3


def create_database():
    conn = sqlite3.connect('extralesson.db')
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    # Создание таблицы категорий
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS categories (
        code VARCHAR(2) PRIMARY KEY,
        title VARCHAR(150)
    )
    """)

    # Вставка данных в таблицу категорий
    cursor.execute(""" INSERT INTO categories (code, title) VALUES ('FD', 'Food Products')""")
    cursor.execute(""" INSERT INTO categories (code, title) VALUES ('EL', 'Electronics')""")
    cursor.execute(""" INSERT INTO categories (code, title) VALUES ('CL', 'Clothes')""")

    # Создание таблицы магазинов
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS store (
        store_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(100)
    )
    """)

    # Вставка данных в таблицу магазинов
    cursor.execute(""" INSERT INTO store (title) VALUES ('Asia')""")
    cursor.execute(""" INSERT INTO store (title) VALUES ('Globus')""")
    cursor.execute(""" INSERT INTO store (title) VALUES ('Spar')""")

    # Создание таблицы продуктов
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(250),
        category_code VARCHAR(2),
        unit_price FLOAT,
        stock_quantity INTEGER,
        store_id INTEGER,
        FOREIGN KEY (category_code) REFERENCES categories (code),
        FOREIGN KEY (store_id) REFERENCES store (store_id)
    )
    """)

    # Вставка данных в таблицу продуктов
    cursor.execute(""" INSERT INTO products (title, category_code, unit_price, stock_quantity, store_id) 
                       VALUES ('Chocolate', 'FD', 10.5, 129, 1)""")
    cursor.execute(""" INSERT INTO products (title, category_code, unit_price, stock_quantity, store_id) 
                       VALUES ('Jeans', 'CL', 120.0, 55, 2)""")
    cursor.execute(""" INSERT INTO products (title, category_code, unit_price, stock_quantity, store_id) 
                       VALUES ('T-Shirt', 'CL', 0.0, 15, 3)""")

    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()


# Вызов функции создания базы данных и таблиц
create_database()
import sqlite3


def display_menu_and_stores():
    print("Вы можете отобразить список продуктов по выбранному id магазина из")
    print("перечня магазинов ниже, для выхода из программы введите цифру 0:\n")

    # Подключение к базе данных
    conn = sqlite3.connect('extralesson.db')
    cursor = conn.cursor()

    try:
        # Вывод списка магазинов
        cursor.execute("SELECT store_id, title FROM store")
        stores = cursor.fetchall()

        for store_id, title in stores:
            print(f"{store_id}. {title}")

        # Запрос на ввод id магазина
        while True:
            store_id_input = input("\nВведите id магазина (0 для выхода): ")

            # Проверка на корректность ввода id магазина
            try:
                store_id = int(store_id_input)
                if store_id == 0:
                    print("Программа завершена.")
                    break

                # Поиск продуктов по выбранному магазину
                cursor.execute("""
                    SELECT p.title, c.title, p.unit_price, p.stock_quantity
                    FROM products p
                    JOIN categories c ON p.category_code = c.code
                    WHERE p.store_id = ?
                """, (store_id,))

                products = cursor.fetchall()

                # Отображение информации о продуктах
                print("\nПродукты в магазине:")
                for product in products:
                    product_title, category_title, unit_price, stock_quantity = product
                    print(f"Название продукта: {product_title}")
                    print(f"Категория: {category_title}")
                    print(f"Цена: {unit_price}")
                    print(f"Количество на складе: {stock_quantity}\n")

            except ValueError:
                print("Некорректный ввод. Введите число.")
                continue

    finally:
        conn.close()


# Вызов функции отображения меню и магазинов
display_menu_and_stores()