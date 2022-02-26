# ufanet
Test task for ufanet

# Задача

Написать телеграм бота для ведения задач (обычный to do).

# Функционал

* Возможность создать задачу.
* Возможность посмотреть список всех задач.
* Возможность отметить задачу выполненной (она удаляется)

# Стэк

— Python 3

— pyTelegramBotAPI

— Postgresql(psycopg2)

# Установка и запуск

Вы можете использовать виртуальное окружение на вашей машине, если вам так удобнее.

* ``git clone https://github.com/imtoopunkforyou/ufanet.git``
* ``cd ~/ufanet``
* ``pip install -r requirements.txt``
* ``python3 bot.py``

# TODO

* Добавить возможность указать при создании задачи кастомное время напоминания. Пользователю в это время приходит уведомление от бота с текстом задачи.