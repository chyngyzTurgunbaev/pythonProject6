import sqlite3

# Функция для создания базы данных и таблиц
def create_database():
    # Подключение к базе данных (если нет, будет создана новая)
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # Создание таблицы countries
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    ''')

    # Добавление записей в таблицу countries
    cursor.execute("INSERT INTO countries (title) VALUES ('Кыргызстан')")
    cursor.execute("INSERT INTO countries (title) VALUES ('Германия')")
    cursor.execute("INSERT INTO countries (title) VALUES ('Китай')")

    # Создание таблицы cities
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            area REAL DEFAULT 0,
            country_id INTEGER,
            FOREIGN KEY (country_id) REFERENCES countries(id)
        )
    ''')

    # Добавление записей в таблицу cities
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Бишкек', 123.45, 1)")   # Кыргызстан
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Ош', 89.7, 1)")         # Кыргызстан
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Берлин', 891.9, 2)")    # Германия
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Пекин', 16410.54, 3)")  # Китай

    # Создание таблицы students
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city_id INTEGER,
            FOREIGN KEY (city_id) REFERENCES cities(id)
        )
    ''')

    # Добавление записей в таблицу students
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Иван', 'Иванов', 1)")    # Бишкек
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Петр', 'Петров', 2)")    # Ош
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Анна', 'Мюллер', 3)")    # Берлин

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()

# Создание базы данных и таблиц при запуске программы
if __name__ == "__main__":
    create_database()
    print("База данных успешно создана и заполнена.")
import sqlite3


# Функция для получения списка городов из базы данных
def get_cities_from_db():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    conn.close()
    return cities


# Функция для получения учеников по id города
def get_students_by_city_from_db(city_id):
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    query = """
        SELECT students.first_name, students.last_name, countries.title AS country, cities.title AS city, cities.area
        FROM students
        JOIN cities ON students.city_id = cities.id
        JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
    """
    cursor.execute(query, (city_id,))
    students = cursor.fetchall()
    conn.close()
    return students


# Функция для вывода списка городов и поиска учеников
def main():
    while True:
        # Вывод списка городов
        cities = get_cities_from_db()
        print("\nСписок городов:")
        for city in cities:
            print(f"{city[0]}. {city[1]}")

        # Запрос id города у пользователя
        try:
            city_id = int(input("\nВведите id города для вывода учеников (для выхода введите 0): "))
            if city_id == 0:
                break
            # Проверка наличия введенного id в списке городов
            if any(city_id == city[0] for city in cities):
                students = get_students_by_city_from_db(city_id)
                if students:
                    print("\nУченики в выбранном городе:")
                    for student in students:
                        print(
                            f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]}")
                else:
                    print("В выбранном городе нет учеников.")
            else:
                print("Города с таким id нет в списке.")
        except ValueError:
            print("Ошибка: введите корректное значение id города (целое число).")


if __name__ == "__main__":
    main()
