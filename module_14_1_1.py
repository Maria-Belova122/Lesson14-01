# ЗАДАНИЕ ПО ТЕМЕ "Создание БД, добавление, выбор и удаление элементов"

import sqlite3

# Подключение к базе данных SQLite (или создание, если она не существует)
connection = sqlite3.connect('not_telegram.db')
# Создание курсора
cursor = connection.cursor()

# Создание таблицы Users (если она еще не существует)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Удаление записей из Таблицы Users (если в ней уже есть записи)
cursor.execute('''
DELETE FROM Users
''')

# Добавление 10 записей в таблицу Users
for i in range(10):
    j = i + 1
    cursor.execute('''
INSERT INTO Users (username, email, age, balance)
VALUES (?, ?, ?, ?)
''', (f'User{j}', f'example{j}@gmail.com', f'{j * 10}', '1000'))

# Обновление (замена) баланса для каждой 2-й записи, начиная с 1-й
cursor.execute('''
UPDATE Users SET balance = ? WHERE id % 2 = 1
''', (500,))

# Удаление каждой 3-й записи, начиная с 1-й
cursor.execute('''
DELETE FROM Users WHERE id % 3 = 1
''')

# Извлечение из таблицы Users записей с возрастом, не равным 60
cursor.execute('''
SELECT username, email, age, balance FROM Users WHERE age != ?
''', (60,))
users = cursor.fetchall()
# Вывод результатов на консоль
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connection.commit()
connection.close()
