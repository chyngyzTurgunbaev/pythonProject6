import sqlite3

# Функция для создания базы данных и таблицы products
def create_database():
    try:
        # Подключение к базе данных (если базы данных нет, она будет автоматически создана)
        db = sqlite3.connect('hw.db')
        cur = db.cursor()

        # Создание таблицы products
        cur.execute('''CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL,
            price FLOAT NOT NULL DEFAULT 0.0,
            quantity INTEGER NOT NULL DEFAULT 0
        )''')

        # Сохранение изменений и закрытие соединения
        db.commit()
        db.close()
        print("База данных успешно создана и таблица products добавлена.")
    except Exception as e:
        print(f"Ошибка при создании базы данных: {e}")

# Вызов функции для создания базы данных и таблицы
create_database()
# Функция для добавления товаров в таблицу products
def add_products():
    try:
        db = sqlite3.connect('hw.db')
        cur = db.cursor()

        # Список товаров для добавления
        products = [
            ("Молоко", 70.5, 10),
            ("Хлеб", 50.0, 20),
            ("Яйца", 90.2, 15),
            ("Сыр", 120.75, 8),
            ("Масло", 150.0, 12),
            ("Кофе", 250.0, 5),
            ("Чай", 120.0, 18),
            ("Сахар", 45.5, 30),
            ("Мука", 55.0, 25),
            ("Вода", 30.0, 40),
            ("Сок", 80.0, 10),
            ("Яблоки", 65.0, 22),
            ("Бананы", 55.5, 17),
            ("Апельсины", 70.0, 13),
            ("Гречка", 95.0, 9)
        ]

        # Вставка товаров в таблицу
        for product in products:
            cur.execute("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", product)

        # Сохранение изменений и закрытие соединения
        db.commit()
        db.close()
        print("Товары успешно добавлены в таблицу products.")
    except Exception as e:
        print(f"Ошибка при добавлении товаров: {e}")

# Функция для изменения количества товара по его ID
def change_quantity_by_id(product_id, new_quantity):
    try:
        db = sqlite3.connect('hw.db')
        cur = db.cursor()

        # Обновление количества товара по ID
        cur.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))

        # Проверка наличия изменений
        if cur.rowcount > 0:
            print(f"Количество товара с ID {product_id} успешно изменено на {new_quantity}.")
        else:
            print(f"Товар с ID {product_id} не найден.")

        # Сохранение изменений и закрытие соединения
        db.commit()
        db.close()
    except Exception as e:
        print(f"Ошибка при изменении количества товара: {e}")

# Функция для изменения цены товара по его ID
def change_price_by_id(product_id, new_price):
    try:
        db = sqlite3.connect('hw.db')
        cur = db.cursor()

        # Обновление цены товара по ID
        cur.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))

        # Проверка наличия изменений
        if cur.rowcount > 0:
            print(f"Цена товара с ID {product_id} успешно изменена на {new_price}.")
        else:
            print(f"Товар с ID {product_id} не найден.")

        # Сохранение изменений и закрытие соединения
        db.commit()
        db.close()
    except Exception as e:
        print(f"Ошибка при изменении цены товара: {e}")

# Функция для удаления товара по его ID
def delete_product_by_id(product_id):
    try:
        db = sqlite3.connect('hw.db')
        cur = db.cursor()

        # Удаление товара по ID
        cur.execute("DELETE FROM products WHERE id = ?", (product_id,))

        # Проверка наличия удаленных записей
        if cur.rowcount > 0:
            print(f"Товар с ID {product_id} успешно удален.")
        else:
            print(f"Товар с ID {product_id} не найден.")

        # Сохранение изменений и закрытие соединения
        db.commit()
        db.close()
    except Exception as e:
        print(f"Ошибка при удалении товара: {e}")

# Функция для выборки всех товаров из таблицы и их вывода в консоль
def select_all_products():
    try:
        db = sqlite3.connect('hw.db')
        cur = db.cursor()

        # Выборка всех товаров из таблицы
        cur.execute("SELECT * FROM products")
        products = cur.fetchall()

        # Вывод товаров в консоль
        if products:
            print("Список всех товаров в базе данных:")
            for product in products:
                print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}, Количество: {product[3]}")
        else:
            print("В базе данных нет товаров.")

        # Закрытие соединения
        db.close()
    except Exception as e:
        print(f"Ошибка при выборке всех товаров: {e}")

# Функция для выборки товаров по условиям цены и количества и их вывода в консоль
def select_products_by_conditions(limit_price, limit_quantity):
    try:
        db = sqlite3.connect('hw.db')
        cur = db.cursor()

        # Выборка товаров по условиям
        cur.execute("SELECT * FROM products WHERE price < ? AND quantity > ?", (limit_price, limit_quantity))
        products = cur.fetchall()

        # Вывод товаров в консоль
        if products:
            print(f"Товары с ценой меньше {limit_price} сом и количеством больше {limit_quantity} штук:")
            for product in products:
                print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}, Количество: {product[3]}")
        else:
            print("Товары по заданным условиям не найдены.")

        # Закрытие соединения
        db.close()
    except Exception as e:
        print(f"Ошибка при выборке товаров по условиям: {e}")

# Функция для поиска товаров по части названия и их вывода в консоль
def search_products_by_title(search_term):
    try:
        db = sqlite3.connect('hw.db')
        cur = db.cursor()

        # Поиск товаров по части названия
        cur.execute("SELECT * FROM products WHERE product_title LIKE ?", ('%' + search_term + '%',))
        products = cur.fetchall()

        # Вывод товаров в консоль
        if products:
            print(f"Результаты поиска по запросу '{search_term}':")
            for product in products:
                print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}, Количество: {product[3]}")
        else:
            print(f"По запросу '{search_term}' товары не найдены.")

        # Закрытие соединения
        db.close()
    except Exception as e:
        print(f"Ошибка при поиске товаров по названию: {e}")

# Тестирование функций
if __name__ == "__main__":
    # Добавление 15 различных товаров
    add_products()

    # Изменение количества товара по ID
    change_quantity_by_id(1, 15)

    # Изменение цены товара по ID
    change_price_by_id(2, 55.0)


