import telebot
import keyboards
import PersonalCommands
import SearchSeries

bot = telebot.TeleBot('1215578709:AAExaTAxqks3rgp3HuRfVDRBacCso6F1llI')
users = {}


def spam(message):
    bot.send_message(message.chat.id, 'Бот пока не умеет анализировать данные в таком формате',
                     reply_markup=keyboards.keyboard1)


def start(message):
    bot.send_message(message.chat.id,
                     'Добро пожаловать, здесь у тебя полно возможностей, надеемся тебе понравится',
                     reply_markup=keyboards.keyboard1)
    PersonalCommands.beginning(message)


def other_handlers(message):
    spam(message)


def for_photo(message):
    PersonalCommands.beginning(message)
    if users[message.from_user.id] == "find_picture":
        SearchSeries.search_similar_photo(message)
        users[message.from_user.id] = "join"
    else:
        spam(message)
