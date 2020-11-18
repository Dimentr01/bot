import telebot
import keyboards
import my_personal_commands
import search_serii_by_picture

bot = telebot.TeleBot('1215578709:AAExaTAxqks3rgp3HuRfVDRBacCso6F1llI')
users = {}


def spam(message):
    bot.send_message(message.chat.id, 'Бот пока не умеет анализировать данные в таком формате',
                     reply_markup=keyboards.keyboard1)


def start(message):
            bot.send_message(message.chat.id,
                             'Добро пожаловать, здесь у тебя полно возможностей, надеемся тебе понравится',
                             reply_markup=keyboards.keyboard1)
            users[message.from_user.id] = "join"


def other_handlers(message):
    spam(message)


def for_photo(message):
    my_personal_commands.beginning(message)
    if users[message.from_user.id] == "find_picture":
        search_serii_by_picture.search_similar_photo(message)
        users[message.from_user.id] = "join"
    else:
        spam(message)
