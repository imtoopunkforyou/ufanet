import sqlite3
import re

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        # Создаём бд, если её нет
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS 'users'(id TEXT UNIQUE)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS 'tasklist'(user TEXT NOT NULL, 
                                                                    number INTEGER NOT NULL, 
                                                                    text TEXT NOT NULL,
                                                                    FOREIGN KEY (user) REFERENCES users(id))""")
        self.connection.commit()
    
    def add_to_users(self, id): # Функция добавляет нового пользователя в таблицу users
        insert = f"""INSERT INTO 'users'  VALUES ('{id}')"""
        with self.connection:
            self.cursor.execute(insert)
            self.connection.commit()


    def add_to_tasklist(self, user, text):  # Функция добавляет данные в таблицу tasklist
        with self.connection:
            select = self.cursor.execute(f"""SELECT Count(*) FROM 'tasklist' WHERE user='{user}'""")
            for i in select:
                number = int(re.findall('\d+', str(i))[0]) + 1
        insert = f"""INSERT INTO 'tasklist'  VALUES ('{user}','{number}','{text}')"""
        with self.connection:
            self.cursor.execute(insert)
            self.connection.commit()
            
    
    def read_data_in_taskist(self, user):  # Чтение данных из таблицы 'tasklist'
        select = f"""SELECT number, text FROM tasklist WHERE user={user}"""
        with self.connection:
            select = self.cursor.execute(select)
            result = 'Номер задачи | Задача \n' + '\n'.join(['. '.join(map(str, i)) for i in select])
        return result


    def delete_task(self, user, number):  # Удаление данных из таблицы 'tasklist'
        # Удаляем таску по номеру
        delete = f"""DELETE FROM tasklist WHERE user='{user}' AND number='{number}'"""
        with self.connection:
            self.cursor.execute(delete)
            self.connection.commit()

        # # Апдейтим номера заданий после удаления
        # with self.connection:
        #     old_numbers = []
        #     new_numbers = []
        #     select_numbers = self.cursor.execute(f"""SELECT number FROM tasklist WHERE user='{user}'""")
        #     for i in select_numbers:
        #         old_numbers.append(i[0])
        #     for i in range(0, len(old_numbers)):
        #         if old_numbers[i]>number:
        #             new_numbers.append(old_numbers[i]-1)
        #     for i in range(0, len(new_numbers)):
        #         update = f"""UPDATE tasklist SET number='{new_numbers[i]}' WHERE number>'{new_numbers[i]}' AND user='{user}'"""
        #         self.cursor.execute(update)
        #         self.connection.commit()

        
    # def update_task(self, user):
    #     # Апдейтим номера заданий после удаления
    #     temp = []
    #     with self.connection:
    #         all_numbers = self.cursor.execute(f"""SELECT number FROM tasklist WHERE user='{user}'""")
    #         for i in all_numbers:
    #             temp.append(i[0])