import telebot
from control_db import Database

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    userid = message.chat.id
    bot.send_message(userid, "Привет. Я бот, который хранит список твоих дел. Напиши мне /help для просмотра доступных команд")


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 
                    "Список доступных команд: \n"
                    "/ls - выводит список дел \n"
                    "/del - удаляет заметку по номеру")

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text + str(message.chat.id))

if __name__ == '__main__':
    bot.polling(non_stop=True)