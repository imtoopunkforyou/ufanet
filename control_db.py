import sqlite3
import re

# Инициализация бд
def init_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    # Создаём бд, если её нет
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'users'(id TEXT UNIQUE)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'tasklist'(user TEXT NOT NULL, 
                                                                number INTEGER NOT NULL, 
                                                                text TEXT NOT NULL,
                                                                FOREIGN KEY (user) REFERENCES users(id))""")
    connection.commit()

# Функция возвращает количество задач у определенного юзера
def count_number_in_tasklist(user):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    select_count_number = cursor.execute(f"""SELECT Count(*) FROM 'tasklist' WHERE user='{user}'""")
    for i in select_count_number:
        count_number = int(re.findall('\d+', str(i))[0])
    return count_number
    
 # Функция добавляет нового пользователя в таблицу users
def add_to_users(id):
    insert = f"""INSERT OR IGNORE INTO 'users'  VALUES ('{id}')"""
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(insert)
    connection.commit()


# Функция добавляет данные в таблицу tasklist
def add_to_tasklist(user, text):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    number = count_number_in_tasklist(user) + 1
    insert = f"""INSERT INTO 'tasklist'  VALUES ('{user}','{number}','{text}')"""
    cursor.execute(insert)
    connection.commit()
            
 # Чтение данных из таблицы tasklist
def read_data_in_taskist(user):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    select = f"""SELECT number, text FROM tasklist WHERE user={user}"""
    select = cursor.execute(select)
    result = 'Номер задачи | Задача \n' + '\n'.join(['. '.join(map(str, i)) for i in select])
    return result


 # Удаление данных из таблицы tasklist
def delete_task(user, number):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    delete = f"""DELETE FROM tasklist WHERE user='{user}' AND number='{number}'"""
    cursor.execute(delete)
    connection.commit()

    
# Апдейтим номера задач после удаления
def update_tasklist(user, number):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    count_number = count_number_in_tasklist(user)
    #ставим флаг
    flag = count_number - number + 1
    for i in range(0, flag):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        update = f"""UPDATE tasklist SET number='{number}' WHERE number='{number+1}' AND user='{user}'"""
        cursor.execute(update)
        connection.commit()
        number+=1

