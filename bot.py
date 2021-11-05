import telebot

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text + str(message.chat.id))

if __name__ == '__main__':
    bot.polling(non_stop=True)