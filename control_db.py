import sqlite3
import re



class Database:
    # Инициализация бд
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    # Создаём бд, если её нет
    def create_table(self):
        with self.connection:
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS 'users'(id TEXT UNIQUE)""")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS 'tasklist'(user TEXT NOT NULL, 
                                                                    number INTEGER NOT NULL, 
                                                                    text TEXT NOT NULL,
                                                                    FOREIGN KEY (user) REFERENCES users(id))""")
            self.connection.commit()

    # Функция возвращает количество задач у определенного юзера
    def count_number_in_tasklist(self, user):
        SELECT = f"""SELECT Count(*) FROM 'tasklist' WHERE user='{user}'"""
        with self.connection:
            select_count_number = self.cursor.execute(SELECT)
            for i in select_count_number:
                count_number = int(re.findall('\d+', str(i))[0])
            return count_number

    # Функция добавляет нового пользователя в таблицу users
    def add_to_users(self, id):
        INSERT = f"""INSERT OR IGNORE INTO 'users'  VALUES ('{id}')"""
        with self.connection:
            self.cursor.execute(INSERT)
            self.connection.commit()

    # Функция добавляет данные в таблицу tasklist
    def add_to_tasklist(self, user, text):
        number = self.count_number_in_tasklist(user) + 1
        INSERT = f"""INSERT INTO 'tasklist'  VALUES ('{user}','{number}','{text}')"""
        with self.connection:
            self.cursor.execute(INSERT)
            self.connection.commit()

    # Чтение данных из таблицы tasklist
    def read_data_in_taskist(self, user):
        SELECT = f"""SELECT number, text FROM tasklist WHERE user={user}"""
        with self.connection:
            SELECT = self.cursor.execute(SELECT)
            result = 'Номер задачи | Задача \n' + \
                '\n'.join(['. '.join(map(str, i)) for i in SELECT])
            return result
        
    # Удаление данных из таблицы tasklist
    def delete_task(self, user, number):
        DELETE = f"""DELETE FROM tasklist WHERE user='{user}' AND number='{number}'"""
        with self.connection:
            self.cursor.execute(DELETE)
            self.connection.commit()

    # Апдейтим номера задач после удаления
    def update_tasklist(self, user, number):
        UPDATE = f"""UPDATE tasklist SET number='{number}' WHERE number='{number+1}' AND user='{user}'"""
        flag = self.count_number_in_tasklist(user) - number + 1
        count = 0
        while count != flag:
            with self.connection:
                self.cursor.execute(UPDATE)
                self.connection.commit()
            return self.update_tasklist(user, number+1)