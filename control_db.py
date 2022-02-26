import psycopg2
import re
from psycopg2 import Error


class Database:
    # Подключение к database под ролью user
    def __init__(self):
        try:
            self.connection = psycopg2.connect(user="tg_bot",
                                               password="As12345",
                                               host="localhost",
                                               port="5432",
                                               database="tg_bot")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL (метод __init__): \n", error)

    # Создаём table users, если её нет

    def create_table_users(self):
        CREATE = """CREATE TABLE IF NOT EXISTS users (id TEXT UNIQUE)"""
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(CREATE)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL (метод create_table): \n", error)
        finally:
            cursor.close()

    # Создаём собственную таблицу для каждого user
    def create_table_user_with_id(self, user):
        CREATE = f"""CREATE TABLE IF NOT EXISTS user_with_id_{user}(user_id TEXT NOT NULL, 
                                                                        number SERIAL NOT NULL, 
                                                                        text TEXT NOT NULL,
                                                                        FOREIGN KEY (user_id) REFERENCES users(id))"""
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(CREATE)
        except (Exception, Error) as error:
            print(
                "Ошибка при работе с PostgreSQL (метод create_table_user_with_id): \n", error)
        finally:
            cursor.close()

    # Функция возвращает количество задач у определенного юзера
    def count_number_in_tasklist(self, user):
        SELECT = f"""SELECT count(*) FROM user_with_id_{user}"""
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(SELECT)
                records = cursor.fetchone()
                return records[0]
        except (Exception, Error) as error:
            print(
                "Ошибка при работе с PostgreSQL (метод  count_number_in_tasklist): \n", error)
        finally:
            cursor.close()

    # Функция добавляет нового пользователя в таблицу users
    def add_to_users(self, user):
        INSERT = f"""INSERT INTO users (id) VALUES ('{user}') ON CONFLICT (id) DO NOTHING"""
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(INSERT)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL (метод add_to_users): \n", error)
        finally:
            cursor.close()

    # Функция добавляет данные в таблицу user_with_id
    def add_to_user_with_id(self, user, text):
        INSERT = f"""INSERT INTO user_with_id_{user}(user_id, text) VALUES ('{user}', '{text}')"""
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(INSERT)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL (метод add_to_user_with_id): \n", error)
        finally:
            cursor.close()

    # Чтение данных из таблицы user_with_id
    def read_data_in_user_with_id(self, user):
        SELECT = f"""SELECT number, text FROM user_with_id_{user}"""
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(SELECT)
                ls = cursor.fetchall()
                result = 'Номер задачи | Задача \n' + \
                    '\n'.join(['. '.join(map(str, i)) for i in ls])
                return result
        except (Exception, Error) as error:
            print(
                "Ошибка при работе с PostgreSQL (метод read_data_in_user_with_id): \n", error)
        finally:
            cursor.close()

    # Удаление данных из таблицы user_with_id
    def delete_task(self, user, number):
        DELETE = f"""DELETE FROM user_with_id_{user} WHERE number={number}"""
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(DELETE)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL (метод delete_task): \n", error)
        finally:
            cursor.close()

    # Апдейтим номера задач после удаления
    def update_tasks(self, user):
        SEQUENCE = """CREATE SEQUENCE IF NOT EXISTS seq START 1"""
        ALTER_SEQUNCE = """ALTER SEQUENCE seq RESTART WITH 1"""
        UPDATE = f"""UPDATE user_with_id_{user} SET number=nextval('seq')"""
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(SEQUENCE)
                cursor.execute(ALTER_SEQUNCE)
                cursor.execute(UPDATE)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL (метод delete_task): \n", error)
        finally:
            cursor.close()
