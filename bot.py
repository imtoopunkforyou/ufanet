import telebot
import re
from control_db import count_number_in_tasklist, delete_task, init_db, add_to_users, add_to_tasklist, read_data_in_taskist, delete_task, update_tasklist
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

# Обработка сообщения /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет. Я бот, который хранит список твоих дел.\n"
                    "Напиши мне сообщение, и я добавлю его в список твоих задач. \n"
                    "Напиши мне /help для просмотра доступных команд")
    add_to_users(message.chat.id)

# Обработка сообщения /help
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 
                    "Список доступных команд: \n"
                    "/list - выводит список дел \n"
                    "/del - удаляет заметку по номеру")

# Обработка сообщения /list
@bot.message_handler(commands=['list'])
def show_tasklist(message):
    text = read_data_in_taskist(message.chat.id)
    bot.send_message(message.chat.id, text)

# Обработка сообщения /del
@bot.message_handler(commands=['del'])
def del_task(messege):
    if re.search('\d+', messege.text):
        number = int(re.findall('\d+', messege.text)[0])
        if number == 0 or number>count_number_in_tasklist(messege.chat.id):
            bot.send_message(messege.chat.id, "Задание под номером " +str(number)+ " не существует")
        else:
            delete_task(messege.chat.id, number)
            update_tasklist(messege.chat.id, number)
            bot.send_message(messege.chat.id, "Задание под номером " +str(number)+ " удалено")
    else:
        bot.send_message(messege.chat.id, "Напишите /del *номер задачи, которую хотите удалить*")

# Обработка сообщений(заданий)
@bot.message_handler(content_types=['text'])
def new_task(message):
    add_to_tasklist(message.chat.id, message.text)
    bot.send_message(message.chat.id, "Задание " + message.text + " добавлено в список дел")

if __name__ == '__main__':
    init_db()
    bot.polling(non_stop=True)