import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        # Создаём бд, если её нет
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS 'users'(id INTEGER UNIQUE)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS 'tasklist'(user INTEGER NOT NULL, 
                                                                    number INTEGER NOT NULL, 
                                                                    text TEXT NOT NULL,
                                                                    FOREIGN KEY (user) REFERENCES users(id))""")
        self.connection.commit()

    def add_to_users(self, id):
        insert = f"""INSERT INTO 'users'  VALUES ('{id}')"""
        with self.connection:
            self.cursor.execute(insert)
            self.connection.commit()


    def add_to_tasklist(self, user, number, text):  # Функция добавляет данные в таблицу 'tasklist'
        insert = f"""INSERT INTO 'tasklist'  VALUES ('{user}','{number}','{text}')"""
        with self.connection:
            self.cursor.execute(insert)
            self.connection.commit()
            


    def read_data_in_taskist(self, user):  # Чтение данных из таблицы 'tasklist'
        select = f"""SELECT number, text FROM tasklist WHERE user={user}"""
        with self.connection:
            select = self.cursor.execute(select)
            self.connection.commit()
            result = '*Номер задачи | Задача* \n' + '\n'.join(['| '.join(map(str, i)) for i in select])
        return result


    def delete_task(self, user, number):  # Удаление данных из таблицы 'tasklist'
        delete = f"""DELETE FROM tasklist WHERE user='{user}' AND number='{number}'"""
        with self.connection:
            self.cursor.execute(delete)
            self.connection.commit()
        return f'Задание под номером {number} удалено.'