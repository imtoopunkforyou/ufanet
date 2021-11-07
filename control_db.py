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
    
 # Функция добавляет нового пользователя в таблицу users
def add_to_users(id):
    insert = f"""INSERT INTO 'users'  VALUES ('{id}')"""
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(insert)
    connection.commit()


# Функция добавляет данные в таблицу tasklist
def add_to_tasklist(user, text):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    select = cursor.execute(f"""SELECT Count(*) FROM 'tasklist' WHERE user='{user}'""")
    for i in select:
        number = int(re.findall('\d+', str(i))[0]) + 1
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
    #выделяем количество записей
    select_count_number = cursor.execute(f"""SELECT Count(*) FROM 'tasklist' WHERE user='{user}'""")
    for i in select_count_number:
        count_number = int(re.findall('\d+', str(i))[0])
    #ставим флаг
    flag = count_number - number + 1
    for i in range(0, flag):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        update = f"""UPDATE tasklist SET number='{number}' WHERE number='{number+1}' AND user='{user}'"""
        cursor.execute(update)
        connection.commit()
        number+=1



# def update_tasklist(user, number):
#     connection = sqlite3.connect("database.db")
#     cursor = connection.cursor()
#     old_numbers = []
#     new_numbers = []
#     select_numbers = cursor.execute(f"""SELECT number FROM tasklist WHERE user='{user}'""")
#     for i in select_numbers:
#         old_numbers.append(i[0])
#     for i in range(0, len(old_numbers)):
#         if old_numbers[i]>number:
#             new_numbers.append(old_numbers[i]-1)
#     return old_numbers, new_numbers


    # new_number = []
    # connection = sqlite3.connect("database.db")
    # cursor = connection.cursor()
    # select_count_number = cursor.execute(f"""SELECT Count(*) FROM 'tasklist' WHERE user='{user}'""")
    # for i in select_count_number:
    #     count_number = int(re.findall('\d+', str(i))[0])
    # cursor.execute(f"""UPDATE tasklist SET number=0 WHERE user='{user}'""")
    # for i in range(1, count_number+1):
    #     new_number.append(i)
    




    # old_numbers = []
    # new_numbers = []
    # select_numbers = cursor.execute(f"""SELECT number FROM tasklist WHERE user='{user}'""")
    # for i in select_numbers:
    #     old_numbers.append(i[0])
    # for i in range(0, len(old_numbers)):
    #     if old_numbers[i]>number:
    #         new_numbers.append(old_numbers[i]-1)
    # for i in range(0, len(new_numbers)):
    #     update = f"""UPDATE tasklist SET number='{new_numbers[i]}' WHERE number>'{new_numbers[i]}' AND user='{user}'"""
    #     cursor.execute(update)
    #     connection.commit()

    # select_count_number = cursor.execute(f"""SELECT Count(*) FROM 'tasklist' WHERE user='{user}'""")
    # for i in select_count_number:
    #     count_number = int(re.findall('\d+', str(i))[0])
    # for i in range(1, count_number+1):
    #     update = f"""UPDATE tasklist SET number='{i}' WHERE user='{user}' AND number>'{i}'"""
    #     cursor.execute(update)
    #     connection.commit()