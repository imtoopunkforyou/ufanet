import sqlite3
from control_db import Database

db = Database()
db.add_to_users(22)
db.add_to_users(13)
db.add_to_users(199)

db.add_to_tasklist(22, 1, 'первая строчка')
db.add_to_tasklist(22, 2, 'вторая строчка')
db.add_to_tasklist(22, 3, 'третья строчка')
db.add_to_tasklist(22, 4, 'четвертая строчка')
db.add_to_tasklist(22, 5, 'пятая строчка')

db.add_to_tasklist(13, 1, 'первая строчка')
db.add_to_tasklist(13, 2, 'вторая строчка')
db.add_to_tasklist(13, 3, 'третья строчка')
db.add_to_tasklist(13, 4, 'четвертая строчка')
db.add_to_tasklist(13, 5, 'пятая строчка')

db.add_to_tasklist(199, 1, 'первая строчка')
db.add_to_tasklist(199, 2, 'вторая строчка')
db.add_to_tasklist(199, 3, 'третья строчка')
db.add_to_tasklist(199, 4, 'четвертая строчка')
db.add_to_tasklist(199, 5, 'пятая строчка')

print("юзер номер 22 " + db.read_data_in_taskist(22))
print("\n")

print("юзер номер 13 " + db.read_data_in_taskist(13))
print("\n")

print("юзер номер 199 " + db.read_data_in_taskist(199))
print("\n")