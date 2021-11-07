import telebot
from control_db import delete_task, init_db, add_to_users, add_to_tasklist, read_data_in_taskist, delete_task, update_tasklist

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет. Я бот, который хранит список твоих дел. Напиши мне /help для просмотра доступных команд")
    add_to_users(message.chat.id)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 
                    "Список доступных команд: \n"
                    "/ls - выводит список дел \n"
                    "/del - удаляет заметку по номеру")

@bot.message_handler(commands=['ls'])
def show_tasklist(message):
    text = read_data_in_taskist(message.chat.id)
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['del'])
def about_del(messege):
    bot.send_message(messege.chat.id, "Напишите номер задачи, которую хотите удалить")

@bot.message_handler(regexp="\d+")
def del_task(message):
    delete_task(message.chat.id, int(message.text))
    update_tasklist(message.chat.id, int(message.text))
    bot.send_message(message.chat.id, "Задание под номером " + message.text + " удалено")
    

@bot.message_handler(content_types=['text'])
def add_task(message):
    add_to_tasklist(message.chat.id, message.text)
    bot.send_message(message.chat.id, "Задание " + message.text + " добавлено в список дел")


if __name__ == '__main__':
    init_db()
    bot.polling(non_stop=True)