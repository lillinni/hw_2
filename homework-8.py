import sqlite3

conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL
);
''')

cursor.execute('''
INSERT INTO countries (title) VALUES 
('Кыргызстан'),
('Германия'),
('Китай');
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    area REAL DEFAULT 0,
    country_id INTEGER REFERENCES countries(id)
);
''')

cursor.execute('''
INSERT INTO cities (title, area, country_id) VALUES 
('Бишкек', 300.0, 1),
('Ош', 180.0, 1),
('Берлин', 891.8, 2),
('Мюнхен', 310.7, 2),
('Шанхай', 6340.5, 3),
('Пекин', 16410.54, 3),
('Гуанчжоу', 7434.4, 3);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    city_id INTEGER REFERENCES cities(id)
);
''')

cursor.execute('''
INSERT INTO students (first_name, last_name, city_id) VALUES 
('Али', 'Ибраимов', 1),
('Султан', 'Орозбеков', 2),
('Марта', 'Шмидт', 3),
('Джон', 'Мюллер', 4),
('Чжан', 'Вэй', 5),
('Мэй', 'Ли', 6),
('Ли', 'Хуан', 7),
('Юрген', 'Вагнер', 3),
('Фатима', 'Акматова', 1),
('Тим', 'Шнайдер', 4),
('Аня', 'Иванова', 2),
('Том', 'Хоффман', 4),
('Юрий', 'Петров', 6),
('Нина', 'Чжан', 5),
('Тянь', 'Линь', 7);
''')

conn.commit()

print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
cursor.execute("SELECT id, title FROM cities;")
cities = cursor.fetchall()

for city in cities:
    print(f"{city[0]}: {city[1]}")

city_id = int(input("Введите id города: "))

if city_id != 0:
    cursor.execute('''
    SELECT s.first_name, s.last_name, c.title, co.title, c.area
    FROM students s
    JOIN cities c ON s.city_id = c.id
    JOIN countries co ON c.country_id = co.id
    WHERE c.id = ?;
    ''', (city_id,))
    
    students = cursor.fetchall()

    if students:
        print(f"\nУчащиеся из города с id {city_id}:")
        for student in students:
            print(f"Имя: {student[0]}, Фамилия: {student[1]}, Город: {student[2]}, Страна: {student[3]}, Площадь города: {student[4]}")
    else:
        print("Нет учеников в этом городе")
else:
    print("Вы вышли из программы")

conn.close()
