import sqlite3
from control_db import delete_task, init_db, add_to_users, add_to_tasklist, read_data_in_taskist, delete_task, update_tasklist2


init_db()
add_to_users(22)
add_to_users(13)
add_to_users(199)

add_to_tasklist(22, 'первая строчка')
add_to_tasklist(22, 'вторая строчка')
add_to_tasklist(22, 'третья строчка')
add_to_tasklist(22, 'четвертая строчка')
add_to_tasklist(22, 'пятая строчка')

add_to_tasklist(13, 'первая строчка')
add_to_tasklist(13, 'вторая строчка')
add_to_tasklist(13, 'третья строчка')
add_to_tasklist(13, 'четвертая строчка')
add_to_tasklist(13, 'пятая строчка')

add_to_tasklist(199, 'первая строчка')
add_to_tasklist(199, 'вторая строчка')
add_to_tasklist(199, 'третья строчка')
add_to_tasklist(199, 'четвертая строчка')
add_to_tasklist(199, 'пятая строчка')

delete_task(22, 3)
print("юзер номер 22 " + read_data_in_taskist(22))
print("\n")

print("юзер номер 13 " + read_data_in_taskist(13))
print("\n")

print("юзер номер 199 " + read_data_in_taskist(199))
print("\n")

print(update_tasklist2(22,3))
print(read_data_in_taskist(22))

