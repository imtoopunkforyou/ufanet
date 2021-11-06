import sqlite3
from control_db import Database

db = Database()
db.add_to_users(22)
db.add_to_users(13)
db.add_to_users(199)

db.add_to_tasklist(22, 'первая строчка')
db.add_to_tasklist(22, 'вторая строчка')
db.add_to_tasklist(22, 'третья строчка')
db.add_to_tasklist(22, 'четвертая строчка')
db.add_to_tasklist(22, 'пятая строчка')

db.add_to_tasklist(13, 'первая строчка')
db.add_to_tasklist(13, 'вторая строчка')
db.add_to_tasklist(13, 'третья строчка')
db.add_to_tasklist(13, 'четвертая строчка')
db.add_to_tasklist(13, 'пятая строчка')

db.add_to_tasklist(199, 'первая строчка')
db.add_to_tasklist(199, 'вторая строчка')
db.add_to_tasklist(199, 'третья строчка')
db.add_to_tasklist(199, 'четвертая строчка')
db.add_to_tasklist(199, 'пятая строчка')

db.delete_task(22, 3)
print("юзер номер 22 " + db.read_data_in_taskist(22))
print("\n")

print("юзер номер 13 " + db.read_data_in_taskist(13))
print("\n")

print("юзер номер 199 " + db.read_data_in_taskist(199))
print("\n")

