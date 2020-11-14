#! /usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
from PIL import Image
import urllib
import cv2
import emoji
import imagehash
import time
import pymysql

while True:
    try:
        conn = pymysql.connect(host='localhost',
                               database='onepunchman',
                               user='root',
                               password='aH$2ucutROA1')
        cursor = conn.cursor()

        bot = telebot.TeleBot('1215578709:AAExaTAxqks3rgp3HuRfVDRBacCso6F1llI')
        users = {}

        # telebot.apihelper.proxy = {'https':'socks5h://88.198.50.103:1080'}


        # code: join=begin, heroes=back to persi, idea=for idea, find_seria=find seria, a-class=back to heroes, persi=glav menu
        # a-class-row...=back to a-class, battles-return to glav


        keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard1.add(emoji.emojize('Смотреть серии :clapper:', use_aliases=True))
        keyboard1.row(emoji.emojize('Найти серию по битве :boom:', use_aliases=True), emoji.emojize('Найти серию по фразе '
                                                                                                    ':speech_balloon:',
                                                                                                    use_aliases=True))
        keyboard1.add(emoji.emojize('Найти серию по картинке :sunrise_over_mountains:', use_aliases=True))
        keyboard1.add(emoji.emojize('О персонажах :globe_with_meridians:', use_aliases=True))
        keyboard1.add(emoji.emojize('Другое :envelope:', use_aliases=True))

        keyboard_phrases = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_phrases.add('Ввести фразу')
        keyboard_phrases.add('Посмотреть список фраз')
        keyboard_phrases.add('Как это работает?')
        keyboard_phrases.add('Назад')

        keyboard_phrases_list = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_phrases_list.add('Фразы Сайтамы')
        keyboard_phrases_list.add('Фразы других персонажей')
        keyboard_phrases_list.add('Диалоги')
        keyboard_phrases_list.add('Назад')

        keyboard_persi = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_persi.add('Герои')
        keyboard_persi.add('Злодеи')
        keyboard_persi.add('Нейтральные персонажи')
        keyboard_persi.add('Назад')

        keyboard_neutral = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_neutral.add('Сверхзвуковой Соник')
        keyboard_neutral.add('Сойрю')
        keyboard_neutral.add('Назад')

        keyboard_villain = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_villain.add('Уровни угроз')
        keyboard_villain.add("Пиратская банда «Тёмная материя»")
        keyboard_villain.row('Храм/Палата эволюции', "Независимые")
        keyboard_villain.add('Ассоциация монстров')
        keyboard_villain.add('Назад')

        keyboard_threats = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_threats.row('Волчий', "Тигриный")
        keyboard_threats.row('Демонический', "Драконий")
        keyboard_threats.add('Божественный')
        keyboard_threats.add('Назад')

        keyboard_independent = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_independent.add('Братья Мозг и Мышцы')
        keyboard_independent.add('Гароу')
        keyboard_independent.add('Морской Капустень')
        keyboard_independent.add('Назад')

        keyboard_band = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_band.row("Глорибас", 'Мельзальгальд')
        keyboard_band.add("Генгальшп")
        keyboard_band.add('Борос')
        keyboard_band.add('Назад')

        keyboard_monsters = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_monsters.add('Псайкос')
        keyboard_monsters.add('Царь монстров Орочи')
        keyboard_monsters.add('Назад')

        keyboard_chamber = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_chamber.add('Доктор Генус')
        keyboard_chamber.row('Царь зверей', "Земляной дракон", "Бронированная горилла")
        keyboard_chamber.add('Асура Кабуто')
        keyboard_chamber.add('Назад')

        keyboard_heroes = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_heroes.add('Сайтама')
        keyboard_heroes.row('S-класс', "A-класс")
        keyboard_heroes.row('B-класс', "C-класс")
        keyboard_heroes.add('Генос')
        keyboard_heroes.add('Назад')

        keyboard_battles = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_battles.add('Сайтама VS Крабинатора')
        keyboard_battles.add('Сайтама VS Ботана и Качка')
        keyboard_battles.add('Сайтама VS Сверхзвукового Соника')
        keyboard_battles.add("Генос VS Сайтамы")
        keyboard_battles.add("Герои VS Морского Царя")
        keyboard_battles.add("Сайтама VS Бороса")
        keyboard_battles.add('Назад')

        keyboard_S_class = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_S_class.row("1-10 место", "11-17 место")
        keyboard_S_class.add("Назад")

        keyboard_S_class1_10 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_S_class1_10.add("Бласт")
        keyboard_S_class1_10.row("Тацумаки", "Бэнг", "Атомный Самурай")
        keyboard_S_class1_10.row("Ребёнок-Император", "Бофой", "Кинг")
        keyboard_S_class1_10.row("Зомбимен", "Технорыцарь", "Свинобог")
        keyboard_S_class1_10.add('Назад')

        keyboard_S_class11_17 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_S_class11_17.row("Сверхлитой Темноблеск", "Сторожевой Пёс")
        keyboard_S_class11_17.row("Световой Флэш", "Мастер в Майке")
        keyboard_S_class11_17.row("Стальная Бита", "Гомо-гомо Зек")
        keyboard_S_class11_17.add("Назад")

        keyboard_A_class = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_A_class.row("1-10 место", "11-39 место")
        keyboard_A_class.add("Назад")

        keyboard_B_class = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_B_class.add("Фубуки Адская Метель")
        keyboard_B_class.row("Реснички", 'Горная Обезьяна')
        keyboard_B_class.row("Очкарик", 'Реактивный Добряк')
        keyboard_B_class.row("Лили", 'Чёрная Дыра в Майке')
        keyboard_B_class.add("Назад")

        keyboard_C_class = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_C_class.add("Бесправный Ездок")
        keyboard_C_class.add("Тигр в Майке")
        keyboard_C_class.add("Жужжащий Человек")
        keyboard_C_class.add("Назад")

        keyboard_A_class11_39 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_A_class11_39.row("Два хвостика", "Великий Философ", "Молния Генджи")
        keyboard_A_class11_39.row("Макс-молния", "Золотой Шар", "Смайл")
        keyboard_A_class11_39.row("Пружинящий Ус", "Снек")
        keyboard_A_class11_39.add("Назад")

        keyboard_A_class1_10 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_A_class1_10.row("Милая маска", "Иайан", "Окамаитачи")
        keyboard_A_class1_10.row("Бусидрель", "Тяжелый танк Фундоши", "Синее пламя")
        keyboard_A_class1_10.row("Фокусник", "Гатлинг Смерти", "Вегетарианец в Майке")
        keyboard_A_class1_10.add("Стингер")
        keyboard_A_class1_10.add('Назад')

        keyboard_A_class1_10 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard_A_class1_10.row("Милая маска", "Иайан", "Окамаитачи ")
        keyboard_A_class1_10.row("Бусидрель", "Тяжелый танк Фундоши", "Синее пламя")
        keyboard_A_class1_10.row("Фокусник", "Гатлинг Смерти", "Вегетарианец в Майке")
        keyboard_A_class1_10.add("Стингер")
        keyboard_A_class1_10.add('Назад')

        keyboard11 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard11.row(emoji.emojize('Предложить идею :bulb:', use_aliases=True),
                       emoji.emojize('Помощь авторам :mailbox:', use_aliases=True))
        keyboard11.add(emoji.emojize('О последнем обновлении :computer:', use_aliases=True))
        keyboard11.add('Назaд')  # second_a_eng

        keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard2.add('OVA')
        keyboard2.row('1 сезон', '2 сезон')  # Rus
        keyboard2.add('Нaзад')  # a-eng

        keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard3.row("1-6 cерии", '7-12 cерии')  # c-eng
        keyboard3.add('Вeрнуться')  # e-eng

        keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard4.row("1 cерия", '2 cерия')  # c-eng
        keyboard4.row("3 cерия", '4 cерия')  # c-eng
        keyboard4.row("5 cерия", '6 cерия')  # c-eng
        keyboard4.add('Веpнуться')  # p-eng

        keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard5.row("7 cерия", '8 cерия')  # c-eng
        keyboard5.row("9 cерия", '10 cерия')  # c-eng
        keyboard5.row("11 cерия", '12 cерия')  # c-eng
        keyboard5.add('Веpнyться')  # yp-eng

        keyboard6 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard6.row("1 ceрия", '2 ceрия')  # ce-eng
        keyboard6.row("3 ceрия", '4 ceрия')  # ce-eng
        keyboard6.row("5 ceрия", '6 ceрия')  # ce-eng
        keyboard6.add('Вернyться')  # y-eng

        keyboard7 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard7.row("7 ceрия", '8 ceрия')  # ce-eng
        keyboard7.row("9 ceрия", '10 ceрия')  # ce-eng
        keyboard7.row("11 ceрия", '12 ceрия')  # ce-eng
        keyboard7.add('Вepнyться')  # eyp-eng

        keyboard8 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard8.row("1-6 ceрии", '7-12 ceрии')  # ce-eng
        keyboard8.add("Вepнуться")  # ep-eng

        keyboardOV = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboardOV.add('Что такое OVA?')
        keyboardOV.row("1 ceзон OVA", '2 ceзон OVA')  # ce-eng
        keyboardOV.add('Нaзaд')  # aa-eng

        keyboardOV2 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboardOV2.row("1 сeрия", '2 сeрия')  # e-eng
        keyboardOV2.row("3 сeрия", '4 сeрия')  # e-eng
        keyboardOV2.row("5 сeрия", '6 сeрия')  # e-eng
        keyboardOV2.add('Вeрнyться')  # ey-eng

        keyboardOV1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboardOV1.row("1 сepия", '2 сepия')  # ep-eng
        keyboardOV1.row("3 сepия", '4 сepия')  # ep-eng
        keyboardOV1.row("5 сepия", '6 сepия')  # ep-eng
        keyboardOV1.add('Веpнyтьcя')  # ypc-eng


        def print_all_users():
            bo = True
            for el in users:
                if bo:
                    print(el)
                else:
                    print(", " + el)
                bo = False


        def starti(message):
            bo = True
            for el in users:
                if message.from_user.id == el:
                    bo = False
                    return
            if bo:
                users[message.from_user.id] = "join"
            try:
                sql = """INSERT INTO users(usersl) VALUES(%s)"""
                recordTuple = (message.from_user.id)
                cursor.execute(sql, recordTuple)
                conn.commit()
            except Exception:
                return


        @bot.message_handler(commands=['start'])
        def start_message(message):
            bot.send_message(message.chat.id, 'Добро пожаловать, здесь у тебя полно возможностей, надеемся тебе понравится',
                             reply_markup=keyboard1)
            users[message.from_user.id] = "join"


        @bot.message_handler(content_types=['text'])
        def send_text(message):
            starti(message)
            if message.text == emoji.emojize('Найти серию по фразе :speech_balloon:', use_aliases=True):
                bot.send_message(message.chat.id, 'Выбирай', reply_markup=keyboard_phrases)
                users[message.from_user.id] = "phrases"
            elif message.text.lower() == 'как это работает?' and users[message.from_user.id] == "phrases":
                bot.send_message(message.chat.id, 'Так как это работает?\n\nВы вводите какую-то фразу, которая уже есть в '
                                                  'списке и вам выдаётся серия, в которой она была.\n\nВводить фразу можно '
                                                  'как, например, обычно: блин, я забыл купить бульон из комбу\nЛибо через '
                                                  'номер: 1)\n\nСтоит учесть, '
                                                  'что фразы не найдутся, если их нет в списке фраз.\n\nЕсли вы хотите, '
                                                  'чтобы ваша фраза там появилась, напишите это в разделе "Предложить идею" ('
                                                  'Меню->Другое->Предложить идею)', reply_markup=keyboard_phrases)
                users[message.from_user.id] = "phrases"
            elif message.text.lower() == 'all users':
                print_all_users()
                bot.send_message(message.chat.id, 'Выбери предпочтения', reply_markup=keyboard1)
            elif message.text.lower() == 'counter of users':
                sql = """SELECT COUNT(*) FROM users; """
                cursor.execute(sql)
                result = cursor.fetchall()
                bot.send_message(message.chat.id, result[0][0], reply_markup=keyboard1)
            elif message.text.lower() == "ввести фразу":
                users[message.from_user.id] = "phrase_vvod"
                bot.send_message(message.chat.id, "Введите фразу\nили её номер со скобкой\n\nP.s. смотри инструкцию",
                                 reply_markup=keyboard_phrases)
            elif message.text.lower() == "фразы сайтамы":
                users[message.from_user.id] = "phrases_list"
                bot.send_message(message.chat.id, "Фразы Сайтамы:\n\n1) Блин, я забыл купить бульон из комбу\n\n"
                                                  '4) Эээ, реябят. Присмотрите за павшими героями. Нехорошо будет, '
                                                  'если помрут. Кого мне тогда '
                                                  'использовать?\n\n7) О, неплохой дроп',
                                 reply_markup=keyboard_phrases_list)
            elif message.text.lower() == "фразы других персонажей":
                users[message.from_user.id] = "phrases_list"
                bot.send_message(message.chat.id, "Фразы других персонажей:\n\nРебёнок-Император:\n2) Мне на подготовительные "
                                                  "надо, можно идти уже?\n\nГенос:\n5) У меня уже есть фанклуб",
                                 reply_markup=keyboard_phrases_list)
            elif message.text.lower() == "диалоги":
                users[message.from_user.id] = "phrases_list"
                bot.send_message(message.chat.id, "Диалоги:\n\nСайтама и Кинг:\n3) —Ну у тебя окно было открыто.\n—Вообще-то "
                                                  "мы на 22 этаже.\n\nБорос и Сайтама:\n6) -Пророчество сбылось, битва на "
                                                  "равных была хороша.\n-Ага. И правда.\n-Лжёшь, у тебя было преимущество. У "
                                                  "меня не было ни шанса. Я даже боя дать тебе не смог.",
                                 reply_markup=keyboard_phrases_list)
            elif users[message.from_user.id] == "phrase_vvod":
                users[message.from_user.id] = "phrases"
                print("phrase:", message.text)
                if message.text.lower() == "1)" or message.text.lower() == "блин, я забыл купить бульон из комбу":
                    for_each("1 сезон 6 серия", message)
                    bot.send_message(message.chat.id,
                                     'Фраза "блин, я забыл купить бульон из комбу" в 18:50\n(18 минут 50 секунд)',
                                     reply_markup=keyboard1)
                elif message.text.lower() == "2)" or message.text.lower() == "мне на подготовительные надо, можно идти уже?":
                    for_each("1 сезон 10 серия", message)
                    bot.send_message(message.chat.id, 'Фраза "Мне на подготовительные '
                                                      'надо, можно идти уже?" в 12:40\n(12 минут 40 секунд)',
                                     reply_markup=keyboard1)
                elif message.text.lower() == "5)" or message.text.lower() == "у меня уже есть фанклуб":
                    for_each("2 сезон 2 серия", message)
                    bot.send_message(message.chat.id, 'Фраза '
                                                      '"У меня уже есть фанклуб" в 06:10\n(6 минут 10 секунд)',
                                     reply_markup=keyboard1)
                elif message.text.lower() == "7)" or message.text.lower() == "о, неплохой дроп":
                    for_each("2 сезон 2 серия", message)
                    bot.send_message(message.chat.id, 'Фраза '
                                                      '"О, неплохой дроп" в 06:20\n(6 минут 20 секунд)',
                                     reply_markup=keyboard1)
                elif message.text.lower() == "3)" or message.text.lower() == '—ну у тебя окно было открыто.\n—вообще-то мы на ' \
                                                                             '22 этаже.':
                    for_each("2 сезон 1 серия", message)
                    bot.send_message(message.chat.id, 'Этот диалог был в 08:00\n(8-ая минута)',
                                     reply_markup=keyboard1)
                elif message.text.lower() == "4)" or message.text.lower() == 'эээ, реябят. присмотрите за павшими героями. ' \
                                                                             'нехорошо будет, если помрут. кого мне тогда ' \
                                                                             'использовать?':
                    for_each("1 сезон 9 серия", message)
                    bot.send_message(message.chat.id, 'Фраза "Эээ, реябят. Присмотрите за павшими героями. Нехорошо будет, '
                                                      'если помрут. Кого мне тогда использовать?" в 15:08\n(15 минут 8 '
                                                      'секунд)',
                                     reply_markup=keyboard1)
                elif message.text.lower() == "6)" or message.text == '-Пророчество сбылось, битва на равных была ' \
                                                                     'хороша.\n-Ага. И правда.\n-Лжёшь, у тебя было ' \
                                                                     'преимущество. У меня не было ни шанса. Я даже боя дать ' \
                                                                     'тебе не смог.':
                    for_each("1 сезон 12 серия", message)
                    bot.send_message(message.chat.id, 'Этот диалог был в 11:58\n(11-ая минута 58-ая секунда)',
                                     reply_markup=keyboard1)
                else:
                    bot.send_message(message.chat.id,
                                     'Такой фразы ещё нет, но вы можете добваить её в\nМеню->Другое->"Предложить идею"',
                                     reply_markup=keyboard1)

            elif users[message.from_user.id] == "idea":
                print(message.from_user.id, " idea:", message.text)
                users[message.from_user.id] = "join"
                bot.send_message(message.chat.id, "Спасибо, постараемся в "
                                                  "кратчайшие сроки её реализовать", reply_markup=keyboard1)
            elif message.text.lower() == 'найти серию по фразе':
                users[message.from_user.id] = "find_seria"
                bot.send_message(message.chat.id, 'Напиши фразу одним сообщением, если по твоей фразе ничего не нашлось, '
                                                  'напиши об этом в "Предложить идею"')
            elif message.text == emoji.emojize('Найти серию по картинке :sunrise_over_mountains:', use_aliases=True):
                users[message.from_user.id] = "find_picture"
                bot.send_message(message.chat.id, 'Пришлите картинку и вам вернётся: максимально похожая найденная картинка,'
                                                  ' серия в которой она найдена, а также время в серии.\n\nПри просмотре, '
                                                  'чтобы быстро достичь найденного момента, просто нажмите на '
                                                  'подсвечивающееся время снизу.\n\nУбедитесь перед отправкой фотографии, '
                                                  'что она чётко взята/вырезана.\n\n (P.s. Найденные картинки могут быть '
                                                  'очень похожи, но не думайте, что эта та же картинка, что вы и прислали)')
            elif message.text == emoji.emojize('Предложить идею :bulb:', use_aliases=True):
                users[message.from_user.id] = "idea"
                bot.send_message(message.chat.id, 'Напиши одним сообщением какие изменения ты хотел бы видеть.\n\nЭто может '
                                                  'что угодно-от переставления кнопок в боте, до реализвации чего-нибудь '
                                                  'нового.\n\nТакже вы '
                                                  'можете написать как вас зовут, чтобы во вкладке "О последнем обновлении" '
                                                  'мы написали благодаря кому это обновление.')
            elif message.text == emoji.emojize('О последнем обновлении :computer:', use_aliases=True):
                users[message.from_user.id] = "join"
                bot.send_message(message.chat.id, 'Version 1.0.1\n\nДобавлен поиск серии по картинке.', reply_markup=keyboard1)
            elif message.text == emoji.emojize('Помощь авторам :mailbox:', use_aliases=True):
                users[message.from_user.id] = "join"
                bot.send_message(message.chat.id, 'Наш бот создан для истинных фанатов этого аниме. Единственную помощь '
                                                  'которую вы можете нам оказать-это распространять информацию если не о '
                                                  'нашем боте, то об этом аниме; а также предлагать идеи для улучшений.',
                                 reply_markup=keyboard1)
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "persi":
                users[message.from_user.id] = "join"
                bot.send_message(message.chat.id, "Вы в главном меню", reply_markup=keyboard1)
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "heroes":
                users[message.from_user.id] = "persi"
                bot.send_message(message.chat.id, "Вы в меню персонажей", reply_markup=keyboard_persi)
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "a-class":
                users[message.from_user.id] = "heroes"
                bot.send_message(message.chat.id, "Вы в меню героев", reply_markup=keyboard_heroes)
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "battles":
                users[message.from_user.id] = "join"
                bot.send_message(message.chat.id, "Вы в главном меню", reply_markup=keyboard1)
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "villains":
                users[message.from_user.id] = "persi"
                bot.send_message(message.chat.id, "Вернулись", reply_markup=keyboard_persi)
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "independent":
                users[message.from_user.id] = "villains"
                bot.send_message(message.chat.id, "Вернулись", reply_markup=keyboard_villain)
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "monsters":
                users[message.from_user.id] = "villains"
                bot.send_message(message.chat.id, "Вернулись", reply_markup=keyboard_villain)
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "band":
                users[message.from_user.id] = "villains"
                bot.send_message(message.chat.id, "Вернулись", reply_markup=keyboard_villain)
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "threats":
                users[message.from_user.id] = "villains"
                bot.send_message(message.chat.id, "Вернулись", reply_markup=keyboard_villain)
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "chamber":
                users[message.from_user.id] = "villains"
                bot.send_message(message.chat.id, "Вернулись", reply_markup=keyboard_villain)
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "phrases":
                users[message.from_user.id] = "join"
                bot.send_message(message.chat.id, "Вернулись", reply_markup=keyboard1)
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "phrases_list":
                users[message.from_user.id] = "phrases"
                bot.send_message(message.chat.id, "Вернулись", reply_markup=keyboard_phrases)

            elif message.text.lower() == 'посмотреть список фраз':
                users[message.from_user.id] = "phrases_list"
                bot.send_message(message.chat.id, "Выбирай:", reply_markup=keyboard_phrases_list)
            elif message.text == emoji.emojize('Найти серию по битве :boom:', use_aliases=True):
                bot.send_message(message.chat.id, 'Тут собраны не все битвы, если ты знаешь, что тут не хватает определённой '
                                                  'битвы, скажи это в "Предложить идею"', reply_markup=keyboard_battles)
                users[message.from_user.id] = "battles"
            elif message.text.lower() == 'сайтама vs бороса':
                for_each("1 сезон 11 серия", message)
                for_each("1 сезон 12 серия", message)
                bot.send_photo(message.chat.id, "AgACAgIAAxkBAAIIq1-DUs-"
                                                "S0u5GXtWBJOpjvHrPN5anAAL0sTEbDEkYSOigWnDnYoXF1rzRly4AAwEAAwIAA3kAAxJ2AQABGwQ",
                               "Битва продолжительностью в 2 серии.")
                bot.send_message(message.chat.id, 'Первый сезон задрал планку экшена на безумно высокий уровень, потому финал '
                                                  'должен был превзойти все увиденное. И это редкий случай, когда последняя '
                                                  'серия получилась без скидок прекрасной. В ней и зашкаливающий адреналин '
                                                  'совершенно вышел из-под контроля, а Сайтама впервые стал '
                                                  'серьезным.Злодей-пришелец Борос, словно прибывший из Dragon Ball Z, '
                                                  'оказался достойной угрозой Земле и чуть не уничтожил ее, а заодно и героя '
                                                  'в желтом плаще. Когда в японских произведениях от ударов персонажи '
                                                  'отлетают аж до Луны, будьте уверены — все предельно. Бой Сайтамы и Бороса '
                                                  '— это искрометное светошоу, способное по накалу страстей посоревноваться '
                                                  'со всеми сенэнами, вместе взятыми. Кажется, будто сама ткань мироздания '
                                                  'трещит от столкновения столь могущественных существ.А когда выясняется, '
                                                  'что даже тут Сайтама не дрался в полную силу, становится немного не по '
                                                  'себе.', reply_markup=keyboard_battles)
            elif message.text.lower() == 'генос vs сайтамы':
                for_each("1 сезон 5 серия", message)
                bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAII4l'
                                                '-DVhgmzcRdMkHHts23Ecp2bDQjAAL4sTEbDEkYSL6Iytd12zumTH7Xli4AAwEAAwI'
                                                'AA3kAAwRCAgABGwQ')
                bot.send_message(message.chat.id, 'Но самый лучший на сегодняшний день поединок в «Ванпанчмене» случился в '
                                                  'середине сезона. Любопытно, что он даже не был настоящий битвой — это '
                                                  'обычный спарринг между Гэносом и Сайтамой. Но то, как он обставлен, '
                                                  'сделало его великим.Такое чувство, что половину всего бюджета аниме '
                                                  'потратили именно на эти сцены. Даже несколько блеклое окружение становится '
                                                  'маловажным, ведь спецэффекты летят настолько обильно, что сами по себе '
                                                  'становятся прекрасным фоном для противостояния двух бесконечно сильных '
                                                  'сущностей, чья мощь не ограничивается простым Over 9000. Каждый кадр в нем '
                                                  '— демонстрация непоколебимости героев и их стремления прийти к своим '
                                                  'целям, несмотря ни на что. Даже если последние ограничиваются чем-то вроде '
                                                  'распродаж и видеоигр, если речь идет о Сайтаме.После окончания спарринга '
                                                  'Гэнос наконец-то узнал, на что на самом деле способен его учитель. А ведь '
                                                  'его даже ни разу не ударили! Впрочем, им предстоит еще многое пережить '
                                                  'вместе, что мы увидим совсем скоро во втором сезоне.',
                                 reply_markup=keyboard_battles)
            elif message.text.lower() == 'герои vs морского царя':
                for_each("1 сезон 8 серия", message)
                for_each("1 сезон 9 серия", message)
                bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAII7F'
                                                '-DVr5kw2iXBa87fD8Z5HNaaZ1lAAL5sTEbDEkYSAZ7bWAfM50iwLOUly4AAwEAAwIAA3kAAz'
                                                '-hAQABGwQ', "Битва продолжительностью в 2 серии.")
                bot.send_message(message.chat.id, 'Морской Царь оказался первой серьезной угрозой, появившейся в аниме. Также '
                                                  'при помощи него нам показали, что Сайтама не может быть везде и сразу. '
                                                  'Потому где-то не столь сильным героям обязательно придется отдуваться '
                                                  'за него, порой вступая в неравную битву только ради того, чтобы потянуть '
                                                  'время.Ливень, идущий во время сражения, подчеркивает общий драматизм. Даже '
                                                  'киборг Гэнос не смог справиться с Морским Царем и чуть не погиб от его '
                                                  'рук, что и говорить про обычного, но очень благородного человека '
                                                  'Безлицензионного Ездока. Впрочем, для Ванпанчмена даже столь опасный '
                                                  'противник не представляет особой угрозы. Классический один удар — и кризис '
                                                  'миновал.Гораздо важнее контекст, при котором состоялся поединок. '
                                                  'Во-первых, именно действия Сайтамы стали причиной вторжения Морского Царя '
                                                  'и последующего хаоса. Так что далеко не все поступки героя по уничтожению '
                                                  'злодеев приносят благо. Во-вторых, благодаря речи протагониста перед '
                                                  'толпой людей мы осознаем, что особой славы он не ищет, а также глубоко '
                                                  'уважает остальных героев. После такого не любить его становится '
                                                  'невозможно.',
                                 reply_markup=keyboard_battles)
            elif message.text.lower() == 'сайтама vs сверхзвукового соника':
                for_each("1 сезон 4 серия", message)
                bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAIJAV'
                                                '-DV5IRq_GcP5vMc9ORLDigW83WAAL7sTEb'
                                                'DEkYSM8kmnXXuo4g5vfVli4AAwEAAwIAA3kAAz5IAgABGwQ')
                bot.send_message(message.chat.id, "Соник в «Ванпанчмене» — сатирический комментарий по поводу всех "
                                                  "edgy-персонажей в духе Саскэ, Зоро, Бакугоу и прочих. Его скорость может "
                                                  "посоревноваться только с его гордостью, потому встреча с Сайтамой, "
                                                  "которому, в общем-то, все равно на многие вещи в этом мире становится для "
                                                  "ниндзя настоящим шоком. Не удивительно, что он начинает скакать вокруг "
                                                  "лысого героя, как ужаленный, и считает того своим персональным архиврагом. "
                                                  "В первой стычке с Сайтамой Соник больно расплачивается за свою наглость, "
                                                  "когда попадается гениталиями прямо на кулак врага. Учитывая, "
                                                  "что кулак все-таки принадлежит «человеку-один-удар», плачевные последствия "
                                                  "можно только представить.\nЗабавный факт: тюремный номер Cоника — 4188.",
                                 reply_markup=keyboard_battles)
            elif message.text.lower() == 'сайтама vs ботана и качка':
                for_each("1 сезон 1 серия", message)
                bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAIJBV'
                                                '-DWFHHXpbLi1zysH0IkAABb4HxKgAC_LExGwxJGEgX5ou'
                                                'GQF0evvCr65cuAAMBAAMCAAN5AAN3qQEAARsE')
                bot.send_message(message.chat.id, "Наглядный пример находчивости и необычного чувства юмора ONE. По своей "
                                                  "сути эта битва против двух максимально шаблонных злодеев создана всего "
                                                  "лишь ради одного панчлайна… или даже уан-панч-лайна! Причем в столь "
                                                  "небольшой сюжетной арке есть практически все — завязка о поиске могущества "
                                                  "и семейных узах, колоссальные разрушения, необдуманная ярость и "
                                                  "последующее раскаяние злодея. К счастью или к сожалению, Сайтаме нет дела "
                                                  "до подобных мелочей. Потому колосс-Качок так же, как и многие другие "
                                                  "суперзлодеи, пал (в буквальном смысле) от рук главного героя. А что "
                                                  "случилось с Ботаном? Это лучше увидеть самому, ведь с ним связана одна из "
                                                  "лучших шуток аниме.",
                                 reply_markup=keyboard_battles)
            elif message.text.lower() == 'сайтама vs крабинатора':
                for_each("1 сезон 1 серия", message)
                bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAIJEF'
                                                '-DWR8sfhtFZGGalhC67r9KxpOfAAL9sTEbDEkYSKFjHRmSCOwCS2gWmC4AAwEAAwIAA3kAA1'
                                                '-lAQABGwQ')
                bot.send_message(message.chat.id, "Важнейшая битва для создания максимально притягательного образа главного "
                                                  "героя. Во время нее у Сайтамы еще нет выдающихся способностей — он обычный "
                                                  "человек, которому с утра отказали в работе. Встреча с человеком-крабом "
                                                  "стала решающей для его желания стать героем.Злодей, как и полагается в "
                                                  "«Ванпанчмене», получился крайне несуразным. Он злой безо всяких причин, "
                                                  "а мутировал из-за того, что когда-то ел очень много крабов. А еще ему на "
                                                  "панцире нарисовали соски несмывающимся маркером, что лишь укрепило ярость "
                                                  "чудовища. Но встреча с апатичным Сайтамой, в котором наконец-то загорелась "
                                                  "искра справедливости, оказалась для Крабинатора роковой. Это, пожалуй, "
                                                  "чуть ли не единственный поединок Ванпанчмена, в котором его избивают "
                                                  "большую часть времени. Победил парень лишь благодаря несгибаемой воле к "
                                                  "жизни. И везению, естественно.",
                                 reply_markup=keyboard_battles)
            elif message.text.lower() == 'привет':
                bot.send_message(message.chat.id, 'Приветствую тебя у нас', reply_markup=keyboard1)
            elif message.text.lower() == 'пока':
                bot.send_message(message.chat.id, 'Возвращайся скорее', reply_markup=keyboard1)
            elif message.text == emoji.emojize('Смотреть серии :clapper:', use_aliases=True):
                bot.send_message(message.chat.id, 'Выбери предпочтения', reply_markup=keyboard2)
            elif message.text.lower() == 'что такое ova?':  # c-eng
                bot.send_message(message.chat.id, 'OVA-это спецвыпуски, которые созданы в качетсве дополненительных серий (не '
                                                  'относятся к основному сюжету аниме).',
                                 reply_markup=keyboard1)
            elif message.text.lower() == 'нaзад':  # a-eng
                bot.send_message(message.chat.id, 'Вернулись назад', reply_markup=keyboard1)
            elif message.text.lower() == 'нaзaд':  # aa-eng
                bot.send_message(message.chat.id, 'Вернулись назад', reply_markup=keyboard2)
            elif message.text.lower() == 'вeрнуться':  # e-eng
                bot.send_message(message.chat.id, 'Вернулись назад', reply_markup=keyboard2)
            elif message.text.lower() == 'вepнуться':  # ep-eng
                bot.send_message(message.chat.id, 'Вернулись назад', reply_markup=keyboard2)
            elif message.text == emoji.emojize('Другое :envelope:', use_aliases=True):
                bot.send_message(message.chat.id, 'Другое', reply_markup=keyboard11)
            elif message.text.lower() == 'назaд':  # second_a-eng
                bot.send_message(message.chat.id, 'Вернулись в главное меню', reply_markup=keyboard1)
            elif message.text.lower() == 'веpнуться':  # p-eng
                bot.send_message(message.chat.id, 'Вернулись в меню', reply_markup=keyboard3)
            elif message.text.lower() == 'веpнyться':  # yp-eng
                bot.send_message(message.chat.id, 'Вернулись в меню', reply_markup=keyboard3)
            elif message.text.lower() == 'вернyться':  # y-eng
                bot.send_message(message.chat.id, 'Вернулись в меню', reply_markup=keyboard8)
            elif message.text.lower() == 'вepнyться':  # eyp-eng
                bot.send_message(message.chat.id, 'Вернулись в меню', reply_markup=keyboard8)
            elif message.text.lower() == 'вeрнyться':  # ey-eng
                bot.send_message(message.chat.id, 'Вернулись в меню', reply_markup=keyboardOV)
            elif message.text.lower() == 'веpнyтьcя':  # ypc-eng
                bot.send_message(message.chat.id, 'Вернулись в меню', reply_markup=keyboardOV)

            elif message.text.lower() == '1 сезон':
                bot.send_message(message.chat.id, 'Смотри 1 сезон', reply_markup=keyboard3)
            elif message.text.lower() == '1-6 cерии':  # c-eng
                bot.send_message(message.chat.id, 'Смотри 1-6 серии', reply_markup=keyboard4)
            elif message.text.lower() == '7-12 cерии':  # c-eng
                bot.send_message(message.chat.id, 'Смотри 7-12 серии', reply_markup=keyboard5)
            elif message.text.lower() == '1 cерия':  # c-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIEUl99o5VkWx705sJHkytcizfsbxApAAIqBwACxgToS8IaYfdux8BTGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '2 cерия':  # c-eng
                bot.send_video(message.chat.id, 'BAACAgIAAxkBAAIEGF98soS6SwESAAGNKrwGa9D03rfNZwACXQkAAs8g4Uuwrs_p9fXKuRsE',
                               reply_markup=keyboard1)
            elif message.text.lower() == '3 cерия':  # c-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIEa199qbm-w1LGvCVdnz_tRRUNlV-LAAIwBwACxgToS90JonV1-xnqGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '4 cерия':  # c-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIEbF99qsMFaZZT-Jp2rK--L0G3v26rAAIyBwACxgToS7uyXb1gLh_BGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '5 cерия':  # c-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIQrV-NoDGgHCHmxhm7SMqUdCrgoHyyAAK3CAAC6HZpSEimdIfOZFkiGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '6 cерия':  # c-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIEbl99q9UFvSqrdhj-h-TeQ59aoIcoAAI0BwACxgToSxwJED5X_16JGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '7 cерия':  # c-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIFp19-FZwMBXVI_fLqrOvk1GjZZyahAAJ4CAACxgTwS0DaYL4-gficGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '8 cерия':  # c-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIFqF9-FfSQFrBBhlKdob5m8BcJWouEAAJ5CAACxgTwS3tOrWw_WP1bGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '9 cерия':  # c-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIFqV9-FksxOuH60DbX0IwhOROa2DQtAAJ6CAACxgTwS6Vqe6Xt-KkVGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '10 cерия':  # c-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIFql9-FsZsoUo8OevNIeFi8G2ZQGQdAAJ7CAACxgTwSz8utxELtvJDGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '11 cерия':  # c-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIFu19-F2cYB6svzdBKLRjqegg_luunAAJ9CAACxgTwS2jIRW5amKopGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '12 cерия':  # c-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIFvF9-F9Az-Jy5s07-QrdOV7kRVjpBAAJ-CAACxgTwSz_qlJRUhGdtGwQ',
                               reply_markup=keyboard1)

            elif message.text.lower() == '2 сезон':
                bot.send_message(message.chat.id, 'Смотри 2 сезон', reply_markup=keyboard8)
            elif message.text.lower() == '1-6 ceрии':  # ce-eng
                bot.send_message(message.chat.id, 'Смотри 1-6 серии', reply_markup=keyboard6)
            elif message.text.lower() == '7-12 ceрии':  # ce-eng
                bot.send_message(message.chat.id, 'Смотри 7-12 серии', reply_markup=keyboard7)
            elif message.text.lower() == '1 ceрия':  # ce-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGB19_YS_iinTESuN2o9y9weZxaFLeAAL0CwAChuT5S4gs3RSvnGaxGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '2 ceрия':  # ce-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGCF9_YmUgBkKt_JnKv6JTqw30BOHnAAL5CwAChuT5S1kqVv9Hm4j-GwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '3 ceрия':  # ce-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGCV9_Y32LSwPscfgUPyz_UlQ23w4dAAL9CwAChuT5S5InsS2AlB5UGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '4 ceрия':  # ce-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGCl9_ZJez_Y7qrXWZDv0KNwZFzctIAAMMAAKG5PlLmcUqWPpJB6obBA',
                               reply_markup=keyboard1)
            elif message.text.lower() == '5 ceрия':  # ce-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGC19_ZbY0Q8gtfYROkCb-yXV9JJZRAAICDAAChuT5SwWSFuFPQa98GwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '6 ceрия':  # ce-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGDF9_ZwxLhamesK3213HNK16hzrF4AAIEDAAChuT5S-WXmWgt40_-GwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '7 ceрия':  # ce-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGDV9_aDeJK4VUV7hmBe_34avAI8O1AAIFDAAChuT5Sxfc05eF7Q7tGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '8 ceрия':  # ce-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGDl9_aWxW74TGS-exH9b2Tlly5fLPAAIGDAAChuT5S8qG-2R8WhlMGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '9 ceрия':  # ce-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGD19_aoji6Ynm54EJo27v-kIrbTFKAAIHDAAChuT5S-aNG72j8TZkGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '10 ceрия':  # ce-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGEF9_a9NvyYT-lQwEAsfSwPuDvzUdAAIIDAAChuT5S70HaISkT7qAGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '11 ceрия':  # ce-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGEV9_bUC3yXBbwYC67Sadpn1INzIHAAIJDAAChuT5SzYPPlDbbNLvGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '12 ceрия':  # ce-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGEl9_bu_PddV5JrWm_0BRHndDMtxsAAIKDAAChuT5S5g5WU2Z6c-AGwQ',
                               reply_markup=keyboard1)

            elif message.text.lower() == 'ova':
                bot.send_message(message.chat.id, 'Смотри OVA', reply_markup=keyboardOV)
            elif message.text.lower() == '1 ceзон ova':  # ce-eng
                bot.send_message(message.chat.id, 'Смотри 1 сезон', reply_markup=keyboardOV1)
            elif message.text.lower() == '2 ceзон ova':  # ce-eng
                bot.send_message(message.chat.id, 'Смотри 2 сезон', reply_markup=keyboardOV2)
            elif message.text.lower() == '1 сepия':  # ep-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGNV-AL_wR1RibeRiesRiHOUxGRPmlAAIdCgAChuQBSBbKNxe0XC2UGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '2 сepия':  # ep-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGNl-AMHMAAVFZOA8e_qFQixTeEPHPJAACIQoAAobkAUiebsuhtk4f8RsE',
                               reply_markup=keyboard1)
            elif message.text.lower() == '3 сepия':  # ep-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIHMF-DBZ6DoL1eR18cj15h0MMIdbC4AAIsCQACDEkYSCl3sEwvd-rPGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '4 сepия':  # ep-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIHMV-DBiMjzKdhef5BPxIW0w7-Uf-oAAIuCQACDEkYSAvc1SFyBxPnGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '5 сepия':  # ep-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIHL1-DBUSd6b57iNRCQOxHMVDEY5CdAAIrCQACDEkYSFG4JWsK3Y3XGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '6 сepия':  # ep-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGOl-ANQ6leY6vvFvfI71iydlfj4U0AAIpCgAChuQBSIEqaOj3UHAXGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '1 сeрия':  # e-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIG-1-C-dMldamopZw-ZjgttahATRdWAALxBwACC-4ZSOYnywpKlI3UGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '2 сeрия':  # e-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIG_F-C-jzTVCQt_PSx4qFHdoOSblmmAALyBwACC-4ZSNFTXscju1LFGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '3 сeрия':  # e-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIHBF-DAiAVbo37LSHrLzgoAAGEqj_HlAACIAkAAgxJGEgWCospw0D--BsE',
                               reply_markup=keyboard1)
            elif message.text.lower() == '4 сeрия':  # e-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIHLl-DBEeKtYoMXWr88H2KT_b4mnPYAAInCQACDEkYSE90y8qdNflgGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '5 сeрия':  # e-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIHA1-DAAJ5xmmlZebWnLu0cLz45_bxAAIaCQACDEkYSD-nrBYmPkhXGwQ',
                               reply_markup=keyboard1)
            elif message.text.lower() == '6 сeрия':  # e-eng
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIHBV-DAn1JrZM-YW-bxJgdOddCkQABKQACIQkAAgxJGEhQdMdxoDm1fRsE',
                               reply_markup=keyboard1)

            elif message.text == emoji.emojize('О персонажах :globe_with_meridians:', use_aliases=True):
                bot.send_message(message.chat.id, 'Здесь вся найденная информация о персонажах\n\nХочется отметить: чтобы '
                                                  'найти определённого персонажа, стоит лишь написать его имя боту, '
                                                  'и он сразу появится.', reply_markup=keyboard_persi)
                users[message.from_user.id] = "persi"
            elif message.text.lower() == 'герои':
                bot.send_message(message.chat.id, 'Вы в меню героев', reply_markup=keyboard_heroes)
                users[message.from_user.id] = "heroes"
            elif message.text.lower() == 'злодеи':
                bot.send_message(message.chat.id, 'Вы в меню злодеев', reply_markup=keyboard_villain)
                users[message.from_user.id] = "villains"
            elif message.text.lower() == 'a-класс':
                bot.send_message(message.chat.id, 'A-класс', reply_markup=keyboard_A_class)
                users[message.from_user.id] = "a-class"
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "a-class1_10":
                bot.send_message(message.chat.id, 'Вернулись', reply_markup=keyboard_A_class)
                users[message.from_user.id] = "a-class"
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "b-class":
                bot.send_message(message.chat.id, 'Вернулись', reply_markup=keyboard_heroes)
                users[message.from_user.id] = "heroes"
            elif message.text.lower() == '1-10 место' and users[message.from_user.id] == "a-class":
                bot.send_message(message.chat.id, '1-10 место:', reply_markup=keyboard_A_class1_10)
                users[message.from_user.id] = "a-class1_10"
            elif message.text.lower() == 'b-класс':
                bot.send_message(message.chat.id, 'B класс:', reply_markup=keyboard_B_class)
                users[message.from_user.id] = "b-class"
            elif message.text.lower() == 's-класс':
                bot.send_message(message.chat.id, 'S класс:', reply_markup=keyboard_S_class)
                users[message.from_user.id] = "s-class"
            elif message.text.lower() == '1-10 место' and users[message.from_user.id] == "s-class":
                bot.send_message(message.chat.id, '1-10 место:', reply_markup=keyboard_S_class1_10)
                users[message.from_user.id] = "s-class1_10"
            elif message.text.lower() == '11-17 место' and users[message.from_user.id] == "s-class":
                bot.send_message(message.chat.id, '1-10 место:', reply_markup=keyboard_S_class11_17)
                users[message.from_user.id] = "s-class11_17"
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "s-class1_10":
                bot.send_message(message.chat.id, 'Вернулись', reply_markup=keyboard_S_class)
                users[message.from_user.id] = "s-class"
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "s-class11_17":
                bot.send_message(message.chat.id, 'Вернулись', reply_markup=keyboard_S_class)
                users[message.from_user.id] = "s-class"
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "s-class":
                bot.send_message(message.chat.id, 'Вернулись', reply_markup=keyboard_heroes)
                users[message.from_user.id] = "heroes"
            elif message.text.lower() == 'c-класс':
                bot.send_message(message.chat.id, 'C класс:', reply_markup=keyboard_C_class)
                users[message.from_user.id] = "c-class"
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "c-class":
                bot.send_message(message.chat.id, 'Вернулись', reply_markup=keyboard_heroes)
                users[message.from_user.id] = "heroes"
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "neutral":
                bot.send_message(message.chat.id, 'Вернулись', reply_markup=keyboard_persi)
                users[message.from_user.id] = "persi"
            elif message.text.lower() == 'уровни угроз':
                bot.send_message(message.chat.id,
                                 'Ассоциацией Героев было создано разделение монстров по уровням опасности.\n\n'
                                 'При разделении учитывались только интересы людей, разрушения, причиняемые окружающей среде, '
                                 'не учитывались, поэтому вполне возможно, что угроза божественного уровня может не равняться '
                                 'планетарному уровню. Также совсем не обязательно, что монстры одного уровня угрозы равны по '
                                 'силе. Еще одна интересная особенность — многие здешние монстры когда-то были людьми, '
                                 'одержимыми какой-нибудь негативной страстью. Также эпизодически появляется некая сущность, '
                                 'названная Богом, которая способствовала перерождению как минимум одного человека в монстра.',
                                 reply_markup=keyboard_threats)
                users[message.from_user.id] = "threats"
            elif message.text.lower() == 'волчий':
                bot.send_message(message.chat.id,
                                 'Волчий — угроза нескольким людям.',
                                 reply_markup=keyboard_threats)
                users[message.from_user.id] = "threats"
            elif message.text.lower() == 'драконий':
                bot.send_message(message.chat.id,
                                 'Драконий — угрозу нескольким городам.',
                                 reply_markup=keyboard_threats)
                users[message.from_user.id] = "threats"
            elif message.text.lower() == 'демонический':
                bot.send_message(message.chat.id,
                                 'Демонический/Дьявольский(в зависимости от перевода) — угроза целому городу.',
                                 reply_markup=keyboard_threats)
                users[message.from_user.id] = "threats"
            elif message.text.lower() == 'тигриный':
                bot.send_message(message.chat.id,
                                 'Тигриный — угроза большому количеству человек.',
                                 reply_markup=keyboard_threats)
                users[message.from_user.id] = "threats"
            elif message.text.lower() == 'божественный':
                bot.send_message(message.chat.id,
                                 'Божественный — угроза всему человечеству.',
                                 reply_markup=keyboard_threats)
                users[message.from_user.id] = "threats"
            elif message.text.lower() == 'пиратская банда «тёмная материя»':
                bot.send_message(message.chat.id,
                                 'Группа разнокалиберных пришельцев под предводительством рыцаря крови Бороса, прибывших на '
                                 'Землю в поисках хорошей драки. Персонажи другой манги того же автора, но более чем '
                                 'двадцатилетней давности, которая как раз и перестала выпускаться из-за раскачки '
                                 'нижеприведённых персон до унылой непобедимости.',
                                 reply_markup=keyboard_band)
                users[message.from_user.id] = "band"
            elif message.text.lower() == 'нейтральные персонажи':
                bot.send_message(message.chat.id,
                                 'Вроде бы и не злодеи, но в герои точно не набиваются. Если присмотреться хорошенько, '
                                 'таких персонажей в манге не мало.',
                                 reply_markup=keyboard_neutral)
                users[message.from_user.id] = "neutral"
            elif message.text.lower() == 'храм/палата эволюции':
                bot.send_message(message.chat.id,
                                 'Храм/Палата эволюции',
                                 reply_markup=keyboard_chamber)
                users[message.from_user.id] = "chamber"
            elif message.text.lower() == 'доктор генус':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIQ8l-N3MbDSAtRMnqPQyi'
                               '-gbzPLm2fAAKhsDEb6HZpSNf1sv9xDKQO2xNwly4AAwEAAwIAA3gAA2wLAgABGwQ',
                               'Доктор Генус: создатель данной конторки. Без дураков гениальный биолог, видавший этику в '
                               'гробу. Хотя фактически ему под сотню лет, благодаря своим разработкам Генус вернул себе '
                               'молодость (и предположительно обрёл биологическое бессмертие). Наштамповал армию клонов себя '
                               'любимого, чтобы успевать проводить все интересные исследования. Всю жизнь полагал, '
                               'что будущее человечества — в искусственной эволюции, и пытался вывести сверхсуществ на замену '
                               'людям. Однако, когда Сайтама одним ударом уничтожил его шедевр — Носорога Асуру — ученый '
                               'понял, как сильно ошибался насчет людей, после чего забросил свои исследования и открыл '
                               'ресторанчик. Размышлял над силой Сайтамы и пришел к выводу, что Сайтама сумел, '
                               'что называется, прыгнуть выше головы и тем самым обрёл безграничный потенциал. А тот факт, '
                               'что для этого Сайтаме понадобились не самые тяжелые тренировки, объясняется тем, '
                               'что в то время Сайтама был нулём без палочки, для которого даже такие тренировки были адскими '
                               'муками.',
                               reply_markup=keyboard_chamber)
                users[message.from_user.id] = "chamber"
            elif message.text.lower() == 'асура кабуто':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIQ81-N3WmmlIaukv'
                               '-c0jraZdUYpVjQAAKisDEb6HZpSEG_oOIKGKlciorali4AAwEAAwIAA3gAA_GXAgABGwQ',
                               'Асура Кабуто является чрезвычайно нестабильным мутантом. Он очень умен (это подтвердил и '
                               'доктор Генус), однако в нем есть ненасытная жажда крови и поэтому он все время находится в '
                               'заключении, а клоны Доктора Генуса опасаются одной только мысли о высвобождении Асуры, '
                               'сам он теряет над собой контроль только после полной трансформации от чего Кабуто крушит все '
                               'что видит в течении недели. Он считает, что намного превосходит людей, называя себя Новым '
                               'человеком, и как думал Доктор Генус, Асура Кабуто является именно тем образцом, которого он '
                               'так долго добивался, дабы увеличить эволюцию человека, однако Кабуто полагает что все '
                               'окружающие должны поклоняться его воле. Более того он очень саркастический. Несмотря на свой '
                               'угрожающий вид и личность он испугался одного  только взгляда Сайтамы осознав на мгновение '
                               'что Сайтама превышает все его характеристики, однако продолжил сражаться с ним демонстрируя '
                               'все свои способности.',
                               reply_markup=keyboard_chamber)
                users[message.from_user.id] = "chamber"
            elif message.text.lower() == 'царь зверей':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIQ9F'
                               '-N3ebNCjaRGRGouJGvVXmPwcczAAKjsDEb6HZpSIJJdN8K6quWFvjVli4AAwEAAwIAA3gAA_mbAgABGwQ',
                               'Царь зверей: здоровенный накачанный человек-лев с непомерным самомнением. Попытался нарезать '
                               'Сайтаму на ломтики своими когтями и был перемолот в фарш «шквалом обычных ударов».',
                               reply_markup=keyboard_chamber)
                users[message.from_user.id] = "chamber"
            elif message.text.lower() == 'земляной дракон':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIQ9V-N3jeJ2KtqM7lho9T7dj'
                               '-CraBOAAKksDEb6HZpSJoqHca9l4m4cAzHly4AAwEAAwIAA20AA77MAQABGwQ',
                               'Земляной дракон: слегка антропоморфный крот. Попытался прикопать Сайтаму…',
                               reply_markup=keyboard_chamber)
                users[message.from_user.id] = "chamber"
            elif message.text.lower() == 'бронированная горилла':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIQ9l'
                               '-N3qAbgVuVDhtYA3KaaaY0nmBlAAKlsDEb6HZpSHYs_kVaISaTpfsamC4AAwEAAwIAA20AA7_6AQABGwQ',
                               'Бронированная горилла: здоровенная горилла-киборг. Был побит Геносом, а увидев, что от Царя '
                               'зверей остался фарш, предпочел не выделываться и рассказал героям все о Храме Эволюции. Когда '
                               'же Генос и Сайтама отправились вершить справедливость, через встроенную спутниковую связь '
                               'предупредил своих о грядущих неприятностях. В манге и аниме работает вместе с Генусом в их '
                               'ресторанчике.',
                               reply_markup=keyboard_chamber)
                users[message.from_user.id] = "chamber"
            elif message.text.lower() == 'мельзальгальд':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIQ7l-N184M8f8XsBX_XXw8wQt_vrYdAAKTsDEb6HZpSNpsB4u7P'
                               '-AVSnYblS4AAwEAAwIAA20AA4SJBQABGwQ',
                               'Мельзальгальд: второй по силе (из тройки лучших бойцов Бороса) пришелец, обладатель пяти '
                               'голов и мощной регенерации — может '
                               'буквально собирать себя из пыли. Его слабое место — пять камушков, каждый из которых отвечает '
                               'за одну из голов. При разрушении камушка голова умирает. Мог разделяться на пять тел, '
                               'превращать свои руки в холодное оружие и вообще менять форму в широком диапазоне, '
                               'довольно долго сражался разом со Стальной Битой, Серебряным Клыком, Атомным Самураем и '
                               'Гомо-Гомо Зеком, и проиграл (а Сайтама в это время всю войну выиграл).',
                               reply_markup=keyboard_band)
                users[message.from_user.id] = "band"
            elif message.text.lower() == 'генгальшп':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIQ71'
                               '-N2JtKB7MEx9F_4QQD_9NIScDEAAKVsDEb6HZpSAo4lxJB1zH0lo2gli4AAwEAAwIAA3gAAyXWAgABGwQ',
                               'Генгальшп: первый по силе (среди тройки лучших Бороса), могущественный (по своим словам) '
                               'телекинетик. В манге не успел '
                               'показать себя, был убит Сайтамой броском камня. В аниме попытался раздавить его '
                               'гравитационным полем, надо ли говорить, что не получилось.',
                               reply_markup=keyboard_band)
                users[message.from_user.id] = "band"
            elif message.text.lower() == 'глорибас':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIQ8F'
                               '-N2b1fHp29o7Oj2jNXIsEf7xb8AAKXsDEb6HZpSP_SznWhoo4MvusXmC4AAwEAAwIAA3gAA1_5AQABGwQ',
                               'Глорибас, третий по силе (среди тройки лучших бойцов Бороса) проявил большую уверенность в '
                               'своем боевом мастерстве. Он кажется немного глуповатым, не в состоянии решить, какие движения '
                               'использовать в бою, направляясь к Сайтаме. Он любил медленно убивать своих врагов.',
                               reply_markup=keyboard_band)
                users[message.from_user.id] = "band"
            elif message.text.lower() == 'борос':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIQ8V'
                               '-N26NxYQt9f3PF9d5IfNu6bT4mAAKasDEb6HZpSP30LhgxVSpomJ9pli4AAwEAAwIAA3gAA1PaAgABGwQ',
                               reply_markup=keyboard_band)
                bot.send_message(message.chat.id,
                                 'Борос: главарь пришельцев, откровенная пародия на саяджинов, в частности на Сон Гоку ('
                                 'которого напоминает внешне). Страдая от унылой непобедимости, прочесал всю вселенную, '
                                 'достойного врага себе не нашел, но услышал от старого пророка, что на Земле есть некто, '
                                 'равный ему по силе. Борос использует внутреннюю энергию для усиления своего тела и '
                                 'энергетических атак — при этом, его тело напоминает скорее биомеханизм. Это объясняется '
                                 'суровым климатом мира, с которого происходит Борос. Достаточно долго сражался с Сайтамой, '
                                 'хотя Борос действовал в полную силу, а Сайтама — нет (собственно, он опять даже не '
                                 'напрягся). '
                                 'Под конец боя выжал из себя все 146 % и пинком зашвырнул Сайтаму на Луну. Тот перепрыгнул '
                                 'назад и разорвал Бороса на куски, но пришелец мгновенно собрал себя и обрушил на Сайтаму '
                                 'мощнейший энергетический удар, способный сжечь планетарную поверхность, на что Сайтама '
                                 'ответил «серьёзным ударом» (заметьте — просто серьёзным, а не каким-нибудь, в который вся '
                                 'дурь вкладывается), который рассеял эту атаку, смертельно ранил Бороса, и еще остаточная '
                                 'ударная волна тысячи километров пролетела. Умирая, Борос сказал, что они выложились на '
                                 'полную, но когда лысый согласился с этим, одернул его: «Хах! Лжец. Ты сдерживался. За весь '
                                 'бой ты так ни разу не оскалил свои клыки. Хе-хе… И всё же, не стоит верить пророчествам. Ты '
                                 'был слишком силён.», оставляя читателей гадать, на что же способен не сдерживающийся'
                                 'Сайтама.',
                                 reply_markup=keyboard_band)
                users[message.from_user.id] = "band"
            elif message.text.lower() == 'сверхзвуковой соник':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIRdF'
                               '-N4uXaINqPE1TW7uQxxxUtWSrzAAKpsDEb6HZpSP_ASDjxOQS7uAVtly4AAwEAAwIAA3kAA54OAgABGwQ',
                               reply_markup=keyboard_neutral)
                bot.send_message(message.chat.id,
                                 'Сверхзвуковой Соник, Соник-со-скоростью-звука: не совсем злодей, скорее просто двинутый '
                                 'ниндзя. '
                                 'Как '
                                 'следует из его погоняла, очень быстр. Для комплекта, Соник выглядит почти как трап — '
                                 'высокий, '
                                 'худой и при этом по женски изящный, физиономия тоже скорее женская. В истории дебютирует, '
                                 'как наемник богатея, посланный уничтожить «Райскую группу», с чем успешно справляется. Тут '
                                 'же '
                                 'встречает Сайтаму, бросается в драку и заканчивается всё тем, что Соник налетел яйцами на '
                                 'кулак (в манге на локоть) Сайтамы. Провопившись, ниндзя заявляет Сайтаме, что они еще '
                                 'встретятся и исчезает. Далее появляется аккурат в момент, когда Сайтама продолбал неделю в '
                                 'классе С без пользы, устраивает разгром, получает по башке и отправляется в тюрьму «Погань '
                                 'под '
                                 'крышкой», откуда сбегает вслед за Гомо-гомо Зеком. Наблюдал за боем Зека и Морского Царя, '
                                 'некоторое время сражался с последним, пока тот не усилился от дождя — на сем моменте '
                                 'благоразумно сбежал. Опять появился в момент, когда к Сайтаме приперлась Фубуки, напоролся '
                                 'на '
                                 'Геноса, завязалась драка, в итоге прервавшая махач Сайтамы с Фубуки. Далее Соник набросился '
                                 'на '
                                 'Сайтаму, использовав свой коронный фокус и создав десять остаточных изображений, '
                                 'на что Сайтама ответил «серьёзным упражнением по прыжкам в стороны» — запрыгал влево-вправо '
                                 'так быстро, что создал нечто вроде живой стены, после чего сделал шаг вперед, чем просто '
                                 'снес '
                                 'Соника. Через некоторое время встретился с двумя товарищами из родной деревни, '
                                 'которые передали ему клетку монстра, но Соник ухитрился не сообразить, что её надо есть '
                                 'сырой '
                                 'и целиком, и долго скакал на толчке.',
                                 reply_markup=keyboard_neutral)
                users[message.from_user.id] = "neutral"
            elif message.text.lower() == 'сойрю':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIRdV'
                               '-N42ZPp5W1IUG5x1PXeKacuZQDAAKqsDEb6HZpSDfVSDecNyzxwLVFmC4AAwEAAwIAA20AAxX2AQABGwQ',
                               reply_markup=keyboard_neutral)
                bot.send_message(message.chat.id,
                                 'Сойрю: мастер боевых искусств, участвовавший в региональном турнире. Практически, '
                                 'как и Сайтама, может приложить кого угодно (в большинстве случаев — другого человеческого '
                                 'противника) с одного удара, но его сверхчеловеческой силой всё же обделён, поэтому при '
                                 'встрече с более серьёзным противником выпускает весь свой арсенал приёмов местного кунг-фу. '
                                 'Дерётся в основном ногами — руки служат для блока и контратак, но если его как следует '
                                 'задеть, он внезапно демонстрирует умело замаскированную мускулатуру в совокупности с '
                                 'разрушительными ударами. Сей товарищ так же отличился тонким троллингом почти всех своих '
                                 'противников (только Сайтама и не поддался): философствует на тему, что стезя героя — лишь '
                                 'обуза для людей с суперсилами, когда они могли бы использовать их в своё удовольствие (и '
                                 'таким образом он всех подталкивает к мысли, что обществу герои не нужны). Впрочем, '
                                 'это не помешало и ему отхватить от главгероя... бедром (тот вовремя удержался, '
                                 'чтобы не вломить Сойрю кулаком, но когда тот попытался напасть со спины, лишь случайно '
                                 'задел его тазом — и впечатал в стену). Впоследствии был практически убит и раздавлен '
                                 'Бакузаном, из-за чего, вопреки своей гордости, молил о помощи у героев. Один из популярных '
                                 'персонажей фандома, ожидающего его скорейшее возвращение. У Вана уже вернулся (с сеструхой '
                                 'в придачу), подорвав позиции тех, кто писал, что Мурата придумал ненужного перса и зря '
                                 'забил главы филлерным турниром.',
                                 reply_markup=keyboard_neutral)
                users[message.from_user.id] = "neutral"
            elif message.text.lower() == 'гароу':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIQ6l-N08z0ZqJnS6WBr6auLNtGj9ttAAKAsDEb6HZpSEfiK3G8OeuR'
                               '-GgYlS4AAwEAAwIAA3gAAzx9BQABGwQ',
                               reply_markup=keyboard_independent)
                bot.send_message(message.chat.id,
                                 'Гароу: один из супербоссов манги. Преследует цель стать сильнейшим монстром и '
                                 'никому не проиграть. Получается хорошо, но не идеально, ибо по силе он примерно в топ-15 '
                                 'S-класса, держится наравне с Геносом или Сторожевым псом в одиночку, но сливает тем, '
                                 'кто выше. Впервые его упоминает Бэнг. Гароу был лучшим учеником Бэнга, но внезапно избил '
                                 'всех '
                                 'прочих учеников, за что словил люлей и надолго исчез. При этом он хоть и недолюбливает '
                                 'Бэнга и '
                                 'его додзе, в итоге все равно настолько похож на Бенга что его принимают за него со спины. '
                                 'Появляется в экстре, где побил банду каратистов, пытавшихся напасть на додзё Бэнга, '
                                 'но нарвавшихся там на Сайтаму и Геноса. Далее приходит в Ассоциацию Героев, которая как раз '
                                 'пыталась заключить союз с местными криминальными элементами и избивает на этих переговорах '
                                 'всех присутствующих, кроме председателя, при этом оторвав руку одному из охранявших '
                                 'председателя героев. Далее избивает героя по кличке «Вегетарианец в майке». Через некоторое '
                                 'время сталкивается с Бесправным Ездоком, но не успевает начать драку, ибо появляются '
                                 'герои-«маечники», во главе с предводителем — Мастером. Был сильно избит Мастером, '
                                 'но выдержал '
                                 'все, уложил Мастера со всей его бандой (Ездоку тоже прилетело), после чего красиво свинтил. '
                                 'По '
                                 'пути отметелил трех лохов из С-класса. Далее по списку были вынесены Золотой Шар и '
                                 'Пружинящий '
                                 'ус. А потом Гароу нарвался на Сайтаму (как водится, не зная, кто это), и попытался вбить '
                                 'его в землю, да только Сайтама ничего не заметил и одним ударом вырубил Гароу, '
                                 'который очухался только к утру на какой-то помойке. Узнал от случайного пацана о Сторожевом '
                                 'псе и пошел за ним, попутно отпинав Стальную Биту. На этом моменте его встретили два мутанта '
                                 'из Ассоциации Монстров и передали пригласительный билет — отказался. Огрёб от Сторожевого '
                                 'Пса '
                                 '(в процессе подозревая его в том, что он не человек, из-за его звериных движений) и чуть '
                                 'позже, после серии боёв с разными героями, и очередного пинка Сайтамы во время попытки '
                                 'нападения на Кинга, сцепился с толпой героев А-ранга, победил и их, но на последнем '
                                 'издыхании, '
                                 'после чего столкнулся с Геносом, Бэнгом и Бомбом. В драке с ними начал потихоньку '
                                 'перерождаться в монстра, и неизвестно, кто бы победил, но был спасён Человеком-фениксом и '
                                 'Древней многоножкой. Орочи, в качестве вступительного испытания, предложил Гароу принести '
                                 'ему '
                                 'голову любого героя на выбор, но Гароу в итоге отказался, за что был избит сопровождавшими '
                                 'его '
                                 'монстрами. Очухавшись, вернулся в гнездо, сразился с Орочи но проиграл с треском. По сути не '
                                 'столько злодей, сколько поехавший рыцарь крови, который хочет всех победить, но людей не '
                                 'убивает, и при этом несмотря на то что говорит что он монстр, к Ассоциации монстров '
                                 'присоединяться не хочет.',
                                 reply_markup=keyboard_independent)
                users[message.from_user.id] = "independent"
            elif message.text.lower() == 'морской капустень':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIQ61'
                               '-N1KA1gBz0bbO5cD8eKX84vc57AAKDsDEb6HZpSN3N9UBOQ1dDwxNwly4AAwEAAwIAA3gAAx4LAgABGwQ',
                               'Морской Капустень: чувак, больше всего похожий на стог водорослей, по факту — человек у '
                               'которого из башки растёт целая куча этой самой морской капусты. Забрёл в город Z, '
                               'пытаясь узнать, что же там творится, где и столкнулся с посланцами Геройской ассоциации — '
                               'Пружинящим Усом и Золотым Шаром, которых отправили за тем же самым. Капустень не шибко '
                               'напрягаясь вырубил обоих, но тут появился Сайтама, который как раз мечтал о средстве для '
                               'ращения волос из водорослей и ободрал беднягу-монстра до предпоследнего листка.',
                               reply_markup=keyboard_independent)
                users[message.from_user.id] = "independent"
            elif message.text.lower() == 'независимые':
                bot.send_message(message.chat.id,
                                 'Независимые злодеи',
                                 reply_markup=keyboard_independent)
                users[message.from_user.id] = "independent"
            elif message.text.lower() == 'братья мозг и мышцы':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIQ7F'
                               '-N1VGxeufoxIjAfEM2Nh6fcpMOAAKGsDEb6HZpSExqK5qTtT0n65AhlS4AAwEAAwIAA3kAA8mDBQABGwQ',
                               'Братья Мозг и Мышцы, они же Ботан и Качок: Качок всегда мечтал быть сильнейшим, '
                               'и Ботан исполнил его мечту, создав суперстероид, превративший Качка в многометрового титана. '
                               'Столкнувшись с вездесущим Сайтамой, Качок нечаянно прихлопнул Ботана, потом прибил (как он '
                               'думал) Сайтаму, и внезапно поймал себя на мысли, что у него ничего не осталось. Сайтамыч, '
                               'заметив, что обладать сверхсилой довольно скучно, убил Качка одним ударом в щи, '
                               'обрушив гиганта на город D. От которого остались одни руины.',
                               reply_markup=keyboard_independent)
                users[message.from_user.id] = "independent"
            elif message.text.lower() == 'ассоциация монстров':
                bot.send_message(message.chat.id,
                                 'Ассоциация',
                                 reply_markup=keyboard_monsters)
                users[message.from_user.id] = "monsters"
            elif message.text.lower() == 'царь монстров орочи':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIQ6F-N0Dk'
                               '-ilE2vZUHCQEgMw_P86QjAAJ9sDEb6HZpSDaUc0AstSJPIfsclS4AAwEAAwIAA20AA9SABQABGwQ',
                               reply_markup=keyboard_monsters)
                bot.send_message(message.chat.id,
                                 'Орочи был суровым и беспощадным существом, чья огромная сила была достаточной, чтобы держать '
                                 'под контролем сотни других монстров в Ассоциации монстров. Он мало говорил, так как его '
                                 'помощник Гёро-Гёро говорил всё за него. Хотя Орочи был лидером Ассоциации монстров, '
                                 'Гёро-Гёро был настоящим лидером Ассоциации. В основном Орочи действовал как исполнитель его '
                                 'правления. Гёро-Гёро долгие годы "промывал мозги" Орочи и получил почти полный контроль над '
                                 'ним.\n\nОрочи был гораздо умнее, чем казался. Его немногословная натура и звериная внешность '
                                 'заставили Гароу недооценить его интеллект, считая его глупым монстром, хотя он был описан '
                                 'Гёро-Гёро как «воинственный гений». Он также является одним из немногих персонажей, '
                                 'который признал огромную силу Сайтамы. После битвы с Сайтамой и знакомства с его '
                                 'способностями, Орочи быстро понял, что Сайтама победил Гокецу и Древнюю Многоножку, '
                                 'но и являлся «монстром города-призрака».\n\nОрочи мог контролировать своё желание убивать '
                                 'людей,в отличии от Гокецу. Он снова проявил снисходительность к Гароу, попросив новобранца '
                                 'убить одного героя, чтобы проявить себя как монстра.\n\nОрочи почти не терпел неудач от '
                                 'своих '
                                 'подчиненных. Так он съел Пробудившегося Таракана, когда он проиграл в битве с '
                                 'Геносом.\n\nПозже выясняется, что из-за «промывания мозгов» Гёро-Гёро, эмоции и чувства '
                                 'Орочи '
                                 'пропали, что очень похоже на проблему Сайтамы. Орочи был взволнован, увидев невероятную '
                                 'силу, '
                                 'которой обладал Сайтама. Он с нетерпением ждал, как сила человека пойдет против силы '
                                 'абсолютного монстра.\n\nВо времена своей прошлой жизни, как человека, Орочи был сломленным '
                                 'человеком, который уже терял свою человечность, когда встретился с Гёро-Гёро. Это делало его '
                                 'подходящим кандидатом на пост будущего Короля Монстров.',
                                 reply_markup=keyboard_monsters)
                users[message.from_user.id] = "monsters"
            elif message.text.lower() == 'псайкос':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIQ6V-N0q2VWQrNXyG-m3p9L9Gzmp5YAAJ'
                               '-sDEb6HZpSJjayFbS7YKWUn3Xli4AAwEAAwIAA3gAA4GeAgABGwQ',
                               'Псайкос: создательница и фактический лидер конторки, красотка-псионик, живущая в образе '
                               'монстра Гёро-гёро. Долгое время изучала монстров, пытаясь вывести сильнейшего, '
                               'и сумела открыть два метода монстрофикации. Первый — «клетки монстра», собираемые с Орочи: '
                               'съевший их мгновенно превращается в чудовище, чья сила, тем не менее, во многом зависит от '
                               'того, насколько силен он был до трансформации, и больше из него не выжать. Тем не менее, '
                               'этот метод быстр и надёжен. Второй же — вогнать в дерьмо по уши, протащить через ад, '
                               'дотащить до грани человеческого и заставить её преодолеть столько раз, сколько получится. '
                               'Метод долгий, нудный, требующий индивидуального подхода и не прощающий ошибок, но результат '
                               'оправдывает все затраты. Разглядев потенциал в Гароу, Псайкос попыталась перетянуть его на '
                               'свою сторону, но была послана. Сражалась с Тацумаки во время штурма гнезда, но проиграла и '
                               'была выдрана из монстрячьего тела… как оказалось нет. Это была кукла, а сама Псайкос сидела '
                               'глубоко под землёй.',
                               reply_markup=keyboard_monsters)
                users[message.from_user.id] = "monsters"
            elif message.text.lower() == 'милая маска':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIHeF-DNNdv-9_nNHMgbBtz8yazsHg3AAKrsTEbDEkYSIdHojXGyQs89PfVli4AAwEAAwIAA3gAAwo'
                               '-AgABGwQ', 'Милая маска/Прекрасно замаскированная Милая маска: 1 место. Маскот Ассоциации '
                                           'героев, свирепый и сильный боец с нарциссичной и садистской натурой. '
                                           'Подрабатывает идолом. Не пропускает в S-класс «недостойных» по его мнению героев, '
                                           'и ради этого остается в А-классе (из-за чего следующие трое персонажей в нём и '
                                           'застряли), хотя по силе давно превосходит остальных. Сражается голыми руками, '
                                           'может рубить ребром ладони, как мечом и мгновенно приращивать потерянные '
                                           'конечности. С рождения обладал безобразной внешностью, но все-равно мечтал стать '
                                           'настоящим героем. По сей причине вступил в Ассоциацию в наглухо-закрытой маске и '
                                           'по поддельным документам. В процессе чего становился сильнее, приобретал свой '
                                           'фан-клуб. Постепенно обнаружил, что приобрёл нечеловеческую силу, а в одном бою, '
                                           'когда маска была повреждена — ещё и потрясающую внешность. Однако осознал, что, '
                                           'по сути сам стал монстром (такая вот ирония судьбы)',
                               reply_markup=keyboard_A_class1_10)
                users[message.from_user.id] = "a-class1_10"
            elif message.text.lower() == 'иайан':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIIXF-DRg025t_MUbP'
                               '-C0WamX5_D1fhAALGsTEbDEkYSGSHyq_EkCykHqNMli4AAwEAAwIAA3kAA8TyAgABGwQ',
                               "Иайан: 2 место. Еще один самурай, ученик Атомного самурая. Имя происходит от его стиля боя "
                               "иайдо — искусства внезапного удара катаной. Специализируется на скоростных сериях ударов. "
                               "Также носит тяжелые на вид доспехи, похожие на рыцарские. Первым схватился с Мельзальгальдом, "
                               "потерял в этой схватке левую руку, но уцелел.",
                               reply_markup=keyboard_A_class1_10)
                users[message.from_user.id] = "a-class1_10"
            elif message.text.lower() == 'окамаитачи':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIIj1'
                               '-DSZgGj1ikF5km9BQqn_rQQH4TAALJsTEbDEkYSBAP2kwlo_sfw9X2lC4AAwEAAwIAA3gAAx2XBQABGwQ',
                               "Окамаитачи (Нарезающий Трансвестит): 3 место. Второй ученик Атомного Самурая. Действительно "
                               "трансвестит, да еще и гей впридачу. Впрочем, менее опасным это его не делает. "
                               "Специализируется на режущих воздушных волнах.",
                               reply_markup=keyboard_A_class1_10)
                users[message.from_user.id] = "a-class1_10"
            elif message.text.lower() == 'бусидрель':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIIll-DSydgK1IMSC48A-OZ6h0WofasAALnsTEbDEkYSHRbCPEO8K74YAgglS4AAwEAAwIAA3gAA'
                               '-MoBQABGwQ',
                               "Бусидрель: 4 место. Третий ученик Атомного Самурая. Использует катану и вакидзаши, "
                               "специализируется на колющих атаках.",
                               reply_markup=keyboard_A_class1_10)
                users[message.from_user.id] = "a-class1_10"
            elif message.text.lower() == 'тяжелый танк фундоши':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIIm1-DS79OOefCFmA9NDZ3sQ7LxcdAAALosTEbDEkYSAnY9v2cpnZkNKJpli4AAwEAAwIAA3gAAxh'
                               '-AgABGwQ',
                               "Тяжелый танк Фундоши: 5 место. Огромный качок в набедренной повязке (которая и называется "
                               "фундоши) и усищами, растущими прямо из носа. Кличку получил за свой сильнейший удар — "
                               "«танковый залп». Впервые появляется в роли телохранителя председателя Ассоциации на "
                               "переговорах с местными криминальными элементами. Попытался залепить своим залпом по Гароу, "
                               "но тот увернулся, Танк попал в пол и сломал руку. Далее Гароу вырубил его одним апперкотом.",
                               reply_markup=keyboard_A_class1_10)
                users[message.from_user.id] = "a-class1_10"
            elif message.text.lower() == 'синее пламя':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIInF'
                               '-DTDPxE70tZDlLZK7pehJWGDk8AALrsTEbDEkYSA8Gw0nY8VqJ1W_Uli4AAwEAAwIAA3gAA5hBAgABGwQ',
                               "Синее пламя: 6 место. Молодой парень, внешне похожий на Сайтаму с волосами. Отличают его "
                               "остекленевшие глаза — широко раскрытые и с очень маленькими радужками. Носит китайский наряд. "
                               "В качестве оружия использует небольшой но мощный огнемёт, который прячет в рукаве. Дебютирует "
                               "в истории с Морским Капустенем, но буквально мельком. Далее появляется в роли телохранителя "
                               "председателя Ассоциации на переговорах с местными криминальными элементами. В сражении с "
                               "Гароу потерял руки.",
                               reply_markup=keyboard_A_class1_10)
                users[message.from_user.id] = "a-class1_10"
            elif message.text.lower() == 'фокусник':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIJx1-ECf7Rfgt9zF0zK4CfiRjvbgl6AAKArzEbDEkgSMG2lLaa'
                               '-8yoIUoQmC4AAwEAAwIAA3gAA4SrAQABGwQ',
                               "Фокусник: 7 место. Молодчик в тройке, маске, плаще фокусника и цилиндре с намалёванным знаком "
                               "вопроса. Носит при себе «палочку», которой и орудует. Впервые появляется в роли телохранителя "
                               "председателя Ассоциации на переговорах с местными криминальными элементами. Показать ничего "
                               "не смог, Гароу уложил его за кадром.",
                               reply_markup=keyboard_A_class1_10)
                users[message.from_user.id] = "a-class1_10"
            elif message.text.lower() == 'стингер':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIJzF'
                               '-EEFjjurANumj05VYzyeu_2o8DAAKPrzEbDEkgSK3ZN3DcLrkklK9sli4AAwEAAwIAA20AA0yHAgABGwQ',
                               "Стингер: 10 место. Молодой парень с причесоном в стиле «взрыв на макаронной фабрике». В "
                               "качестве оружия использует бамбуковое копьё с бурообразным наконечником, которым может "
                               "прошивать по нескольку врагов за раз. В одиночку одолел десяток монстров тигриного уровня, "
                               "но из-за привычки рисоваться получил по морде от Морского Царя и надолго выбыл из строя. "
                               "Далее появляется, сражаясь вместе с Молнией Генджи с котоподобным монстром Куснякой.",
                               reply_markup=keyboard_A_class1_10)
                users[message.from_user.id] = "a-class1_10"
            elif message.text.lower() == 'два хвостика':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIJz1-EEU7SsG20cClrkD4LK3tRJ0LTAAKQrzEbDEkgSE_jZrDyDLv'
                               '-YI8hlS4AAwEAAwIAA20AA14oBQABGwQ',
                               "Два Хвостика (Двойные Хвостики): 11 место. Худощавая девушка с волосами, заплетенными в, "
                               "собственно, "
                               "два хвостика, носит костюм в цирковом стиле. Сражается большим количеством оружия, "
                               "замаскированным под реквизит жонглера, умеет метать кинжалы на манер бумерангов. По всей "
                               "видимости, слепа: глаза её скрыты повязкой, но обладает хорошим слухом и может отслеживать "
                               "противников по дыханию.",
                               reply_markup=keyboard_A_class11_39)
                users[message.from_user.id] = "a-class11_39"
            elif message.text.lower() == 'гатлинг смерти':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIJ4F'
                               '-EE17QLycc6ifcj2W8alCtkxj1AAKRrzEbDEkgSAPOMUJJ4UbGY2oYlS4AAwEAAwIAA3gAA2szBQABGwQ',
                               "Гатлинг Смерти: 8 место. Вместе с Бабочкой DX и Костью, Гатлинг Смерти сражается с Стоглазым "
                               "Осьминогом, но все три "
                               "героя быстро проигрывают.",
                               reply_markup=keyboard_A_class1_10)
                users[message.from_user.id] = "a-class1_10"
            elif message.text.lower() == 'вегетарианец в майке':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIJ4V'
                               '-EFCXIcQ7dMCL71Oawt7b2DVu2AAKSrzEbDEkgSPiiUoYyD3_2ba9sli4AAwEAAwIAA3gAA4qJAgABGwQ',
                               "Вегетарианец в Майке: 9 место. Вместе с Бабочкой DX и Костью, Гатлинг Смерти сражается с "
                               "Стоглазым "
                               "Осьминогом, но все три "
                               "героя быстро проигрывают.",
                               reply_markup=keyboard_A_class1_10)
                users[message.from_user.id] = "a-class1_10"
            elif message.text.lower() == '11-39 место' and users[message.from_user.id] == "a-class":
                bot.send_message(message.chat.id, "11-39 место",
                                 reply_markup=keyboard_A_class11_39)
                users[message.from_user.id] = "a-class11_39"
            elif message.text.lower() == 'назад' and users[message.from_user.id] == "a-class11_39":
                bot.send_message(message.chat.id, "Вернулись",
                                 reply_markup=keyboard_A_class)
                users[message.from_user.id] = "a-class"
            elif message.text.lower() == 'великий философ':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIKZl'
                               '-EKD_wgJC9EzhhvcHynlSM_OzOAAKwrzEbDEkgSFn30AEO3vc1YnHUli4AAwEAAwIAA20AA6NOAgABGwQ',
                               "Великий Философ: 13 место. Выглядит, как античные изображения Зевса (седовлас, густобород, "
                               "сложен как олимпийский чемпион), на голове носит лавровый венок, на теле — некое подобие "
                               "туники. При себе таскает монструозный талмуд по философии, который увлечённо штудирует. "
                               "Физически, естественно, силён и крепок (будет помощнее Стингера и Макса Молнии). Его коронный "
                               "приём — «Три тонны философии»: он закрывает свою книгу, после чего со всей дури лупасит врага "
                               "корешком. Вполне возможно, что как раз три тонны эта книженция и весит.",
                               reply_markup=keyboard_A_class11_39)
                users[message.from_user.id] = "a-class11_39"
            elif message.text.lower() == 'молния генджи':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIKb1-EKOGUV0drQMCHbHZI9dCdQ'
                               '-OeAAKyrzEbDEkgSGN4DXinV0gBC1kTmC4AAwEAAwIAA20AA5CrAQABGwQ',
                               "Молния Генджи: 17 место. Надсмотрщик города D. Носит броню (внешне похожую на "
                               "Механизированный Пластинчатый Доспех из Arcanum) с реактивными роликами, в качестве оружия "
                               "использует два шокера. Вместе со Стингером сражается с Куснякой и побеждает (рядом еще "
                               "одного, такого же, пинал Генос). А вот от более крупной версии кошака, благоразумно дает дёру "
                               "— со Стингером на горбу (переростка убил проходивший мимо Сайтама, как раз искавший кошку "
                               "одного богача). Генджи не особенно силён физически, и против неуязвимых к электричеству "
                               "врагов ему сражаться очень тяжело. Посему битву с Человеком-сомом и Мейко Плазмой он не "
                               "потянул.",
                               reply_markup=keyboard_A_class11_39)
                users[message.from_user.id] = "a-class11_39"
            elif message.text.lower() == 'макс-молния':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIKgF'
                               '-EKc_fwAFRle5TPSkqZJcHqgyKAAKzrzEbDEkgSKvhfAlB8gbEig_Hly4AAwEAAwIAA3gAA9V8AQABGwQ',
                               "Макс-молния: уже 19 место. В качестве оружия использует порох, который при ударе выпускает из "
                               "контейнеров на ботинках. Схватился с Морским Царем, продул вдребезги и едва не погиб под "
                               "небоскрёбом, но был спасен Гомо-Гомо Зеком. Далее появляется, участвуя в турнире по боевым "
                               "искусствам. Первый поединок — с «китаянкой» Лин-Лин — выиграл без особых проблем, "
                               "второй поединок с кунфуистом Суирю не осилил.",
                               reply_markup=keyboard_A_class11_39)
                users[message.from_user.id] = "a-class11_39"
            elif message.text.lower() == 'смайл':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIKgV'
                               '-EKloJifJrxvhVAAFng5t_5k6yBwACtK8xGwxJIEgZxSmXMxhwn4lFBZcuAAMBAAMCAANtAAM3mgEAARsE',
                               "Смайл (Смайлик): 27 место. Худощавый молодой человек в желто-оранжевом костюме и чёрной маске, "
                               "на груде красуется изображение смайлика. Сражается кендамой (игрушечным молоточком), "
                               "но громадных размеров и сделанным из прочных материалов. В обращении с этим оружием весьма "
                               "умел и изобретателен. К кендаме прикреплён шарик с нитью, за счёт чего может атаковать и на "
                               "дольних дистанциях. Несмотря на прозвище, никогда не улыбается и не воспринимает юмор. "
                               "Несколько раз мелькал в аниме, на заднем плане.",
                               reply_markup=keyboard_A_class11_39)
                users[message.from_user.id] = "a-class11_39"
            elif message.text.lower() == 'золотой шар':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIKgl'
                               '-EKqgaQVf4wun4qUUS93oOrLkLAAK1rzEbDEkgSKHsdkuNYckw_EoQmC4AAwEAAwIAA20AA4KmAQABGwQ',
                               "Золотой Шар: 26 место. Гоповатого вида парень, в качестве оружия использует рогатку с "
                               "лазерным прицелом. Из сей рогатки стреляет шарами из сплава с памятью формы — эти шары на "
                               "лету превращаются в дротики. Умеет запускать свои снаряды с хитрыми рикошетами. Был отправлен "
                               "в город Z для расследования обстановки вместе с Пружинящим Усом. Первым схватился с монстром "
                               "Морским Капустенем, но отвлекся на то, как легко Капустень отбил его дротик и потому "
                               "проиграл.",
                               reply_markup=keyboard_A_class11_39)
                users[message.from_user.id] = "a-class11_39"
            elif message.text.lower() == 'пружинящий ус':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIKk1'
                               '-ELS_iTjkhLdP8d9YSqXFSTsE5AAK7rzEbDEkgSNViRCwa3SvWMJpxly4AAwEAAwIAA20AAyS6AQABGwQ',
                               "Пружинящий Ус: 28 место. 47-летний мужчина в тройке, прозвище получил за свои аномально "
                               "гибкие и прочные усы. В качестве оружия использует рапиру, которая в нерабочее время "
                               "превращается в платочек. Очень умелый и сильный фехтовальщик, может рубить сталь и парировать "
                               "множественные атаки. Его рапира может удлиняться за сотню метров со сверхзвуковой скоростью, "
                               "пробивая всё на своём пути. Был отправлен в город Z для расследования обстановки вместе с "
                               "Золотым Шаром, сражался с Морским Капустенем, но продержался недолго (а потом Капустеня "
                               "ободрал Сайтама). Похоже, они с Золотым Шаром приятели — появляются обычно вместе.",
                               reply_markup=keyboard_A_class11_39)
                users[message.from_user.id] = "a-class11_39"
            elif message.text.lower() == 'снек':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIKlF'
                               '-ELUqCkvyXpPjgcIZMOTW0inuLAAK9rzEbDEkgSGNG3TnAJB8vkAgglS4AAwEAAwIAA20AA8AyBQABGwQ',
                               "Снек, жалящий змеиный кулак: 37 место."
                               "Гибкий парень, носящий что-то вроде смокинга из кожи змеи-монстра, который по прочности не "
                               "уступает хорошей броне. Читал свежеиспечённым супергероям лекцию на тему «теперь вы герои, "
                               "не опозорьте нас всех», проявил себя изрядным козлом. Его прозвище происходит от стиля боя — "
                               "«Кулака жалящей змеи», похожего на змеиный стиль кун-фу (фактически это он и есть). Попытался "
                               "наехать на Сайтаму и оказался вбит в землю. Вышел на Морского Царя, хотя понимал, что шансов "
                               "у него не шибко. Сумел уклониться от первого удара, но даже не успел толком порадоваться "
                               "этому — был впечатан в стену. Участвует в турнирах по боевым искусствам и довольно хорош в "
                               "этом деле.",
                               reply_markup=keyboard_A_class11_39)
                users[message.from_user.id] = "a-class11_39"
            elif message.text.lower() == 'чёрная дыра в майке':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIKuV-EMOPT3MgUKcQ_KxztDD3kMGQnAALArzEbDEkgSBi51tx'
                               '-tXU9KirNly4AAwEAAwIAA20AA719AQABGwQ',
                               "Чёрная Дыра в Майке: 81 место. Крупный мускулистый мужчина с короткими чёрными волосам. Он "
                               "носит чёрную "
                               "майку и простые "
                               "штаны.\nЧёрная Дыра В Майке очень уверенный и упрямый. Поэтому он отказывается верить, "
                               "что герой С-класса может уничтожить метеор. Он также довольно харизматичный человек, "
                               "что показано через его способность склонять толпу к своей вол",
                               reply_markup=keyboard_B_class)
                users[message.from_user.id] = "b-class"
            elif message.text.lower() == 'фубуки адская метель':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIK2F-ENyjVEm2p4_tNWmCuAthYJf7BAALErzEbDEkgSEfLvzGT'
                               '-2DVu5RJli4AAwEAAwIAA3gAAyr4AgABGwQ',
                               "Фубуки Адская Метель: 1 место. Младшая сестра Татцумаки, тоже псионик. Коплексует из-за "
                               "гиперопеки своей сестры, а так же — невозможности превзойти Милую Маску и учеников Атомного "
                               "Самурая, по силам а не рангу, навскидку была бы в топ-10 А-ранга. Обеспокоенная быстрым "
                               "продвижением Сайтамы по рангам, решила завербовать его. Получив отказ, напала на Сайтаму, "
                               "на что тот ответил лекцией на тему «что за фигня, герой?!». Осознав силу Сайтамы (а так же "
                               "его дружбу с героями S-класса) изменила свое отношение. Фубуки много сил и времени тратит на "
                               "свою группировку, которую набирает в основном из тех кто застрял в Б-ранге (например, "
                               "она обучает более-менее выдающихся последователей псионике), и она не раз втягивала Сайтаму и "
                               "его «группировку» в очередные соревнования.",
                               reply_markup=keyboard_B_class)
                users[message.from_user.id] = "b-class"
            elif message.text.lower() == 'реснички':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIK2V-EN1'
                               '-dyCKA9nxtbwOGwMRhUupQAALFrzEbDEkgSPAvXczfCir_13DUli4AAwEAAwIAA3gAAx9MAgABGwQ',
                               "Реснички: 2 место. Одетый в тройку парень с длинными ресницами, состоящий у Фубуки в "
                               "шестерках. Псионик, может изменять форму своего оружия — щипчиков для завивки ресниц.",
                               reply_markup=keyboard_B_class)
                users[message.from_user.id] = "b-class"
            elif message.text.lower() == 'горная обезьяна':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIK2l-EN-Tynp2VJaM4FoU3fCE_rWfmAALGrzEbDEkgSJDBq4aY'
                               '-gL3HLd3ly4AAwEAAwIAA20AA8yzAQABGwQ',
                               "Горная Обезьяна: 3 место. Громила в тройке, еще одна шестерка Фубуки. Укрепляет свое тело "
                               "псионической силой, так что смог пережить атаку Татцумаки.",
                               reply_markup=keyboard_B_class)
                users[message.from_user.id] = "b-class"
            elif message.text.lower() == 'очкарик':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIK3V'
                               '-EOPmw2zh9ISvjgWvA7hR6w9UwAALKrzEbDEkgSA9dGPOgest2afVBli4AAwEAAwIAA20AA2H1AgABGwQ',
                               "Очкарик: 20 место. Состоял в группировке Фубуки, но ушёл на вольные хлеба. Сражался с Гароу, "
                               "демонстрируя навыки боевых искусств, но всё же был им оттделан.",
                               reply_markup=keyboard_B_class)
                users[message.from_user.id] = "b-class"
            elif message.text.lower() == 'реактивный добряк':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIK3F-EONyPGi'
                               '-u6u1NiJWUtFAKomYyAALJrzEbDEkgSBUfZmN6zc0KZ4vali4AAwEAAwIAA20AA_1NAgABGwQ',
                               'Реактивный Добряк: 50 место. Киборг спортивно-бойцовской модели. Первым из слабых героев '
                               'вышел на Морского царя, но мгновенно был разорван пополам одним ударом когтистой ладони. '
                               'Возможно, выжил — киборг же. Выжил и получил апгрейд, участвовал в атаке на штаб Ассоциации '
                               'монстров. Теперь носит имя: "Возродившийся Реактивный Добряк". Один из немногих героев в '
                               'B-классе, кто не присоединился к Фубуки.',
                               reply_markup=keyboard_B_class)
                users[message.from_user.id] = "b-class"
            elif message.text.lower() == 'лили':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIK21-EOMLOXSSOXj'
                               '-mAAHwAXZgw5DF6QACyK8xGwxJIEhdINtJX5EiGOp3G5UuAAMBAAMCAANtAAO5OgUAARsE',
                               "Лили (возможно, прозвище-производное от слова Лилия): 74 место. Новичок в свите Фубуки - "
                               "временами косячит, но соратники в беде не бросят. Тоже владеет псионикой, н на весьма низком "
                               "уровне. В бою полагается на нунчаки.",
                               reply_markup=keyboard_B_class)
                users[message.from_user.id] = "b-class"
            elif message.text.lower() == 'бесправный ездок':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIK8l-EPOKRAcwxwq9RUxa0pMKGMH6OAALOrzEbDEkgSCYbgnBVBg15VWYWmC4AAwEAAwIAA20AA3'
                               '-nAQABGwQ',
                               'Бесправный ездок: 1 место. Мог бы и повыше подняться(навскидку по его силе он примерно в '
                               'середине B-класса), но не хочет. Постоянно огребает от разных монстров, но всегда отважно '
                               'кидается в бой, ибо такова его натура. Но еще чаще вывозит раненых героев с мест боев, '
                               'за что многие к нему хорошо относятся. Впервые засветился ещё в подростковом возрасте под '
                               'кликухой «Безымянный Велосипедист», пытаясь помочь жертве хулиганов. После разборок с Морским '
                               'царём и повышения Сайтамы проставился в знак уважения и благодарности. Персонаж - явная '
                               'отсылка к токусацу "Наездник в маске"',
                               reply_markup=keyboard_C_class)
                users[message.from_user.id] = "c-class"
            elif message.text.lower() == 'тигр в майке':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIK8V-EPKs0CcsKtZ6b-HvV8'
                               '-PkNQNRAALNrzEbDEkgSCXpBYyKxUkILe0XmC4AAwEAAwIAA20AA4enAQABGwQ',
                               "Тигр в Майке: 13 место. Крупный мускулистый мужчина с полосами тигра на его волосам и бровям. "
                               "Он носит майку в тигровую полоску.Мастер в Майке особенно громкий и неприятный. Он самоуверен "
                               "в своих способностях и смотрит свысока на новых героев, будучи довольно высокомерным и "
                               "враждебным.",
                               reply_markup=keyboard_C_class)
                users[message.from_user.id] = "c-class"
            elif message.text.lower() == 'жужжащий человек':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAIK8F-EO-arVuEBA9qU4xk8CMX33ZP0AALMrzEbDEkgSGekL3FbznK'
                               '-YmBQmC4AAwEAAwIAA20AA8GcAQABGwQ',
                               "Жужжащий человек : 331 место. Мускулистый молодой человек, носящий прическу в стиле «афро». "
                               "Носит белую сильно облегающую "
                               "футболку с иероглифом, обозначающий «Кулак» (яп. 拳), а также черные брюки и обувь для занятий "
                               "кунг-фу.Он показался себя достаточно храбрым, чтобы встать на защиту людей и бросить вызов "
                               "Морскому Царю, когда тот собирался убить всех людей находящихся в куполе, несмотря на свою "
                               "храбрость, выражение его лица ясно дало понять, что он был напуган.",
                               reply_markup=keyboard_C_class)
                users[message.from_user.id] = "c-class"
            elif message.text.lower() == 'бласт':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILEF-EW-dHKET04qi4ZI956f'
                               '-GPkX5AAIDsDEbDEkgSAbhmCcCuJdxT_LAly4AAwEAAwIAA3gAA_2FAQABGwQ',
                               'Бласт: 1 место. Во флешбеке Милой Маски Бласт представлен как мужчина на вид средних лет с '
                               'колючей причёской, бакенбардами и бровями необычной формы. Он изображён в профессионально '
                               'выглядящем костюме с надписью "Blast" внутри плашки на его плаще, который крепится к '
                               'массивным наплечникам. Текущий же вид Бласта неизвестен. Он считает, что лучше полагаться '
                               'только на себя и не ждать спасения от других. Ничего неизвестно о личности Бласта, '
                               'но судя по реакции ребёнка-императора, Бласт имеет привычку не появляться на заседаниях '
                               'Ассоциации героев. Подобно Сайтаме, он принимает работу супергероя в качестве хобби',
                               reply_markup=keyboard_S_class1_10)
                users[message.from_user.id] = "s-class1_10"
            elif message.text.lower() == 'тацумаки':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILEV-EW_cNo2gn4slprod1XSfnJvfdAAIEsDEbDEkgSFF'
                               '-JGFc8vXy8AJFli4AAwEAAwIAA3gAA_76AgABGwQ',
                               'Тацумаки Устрашающий вихрь: 2 место. Комплексует из-за своего детского вида, '
                               'посему отличается весьма стервозным характером. Низкие '
                               'физические показатели компенсируются мощными псионическими способностями (становящимися '
                               'нестабильными при малейших повреждениях мозга). Предпочитает летать. Способна усиливать тело '
                               'своей псионной мощью, отчасти управлять гравитацией и механизмами, также может разламывать '
                               'врагов псионическим вихрем. Смогла перехватить град гигантских снарядов с корабля Бороса и '
                               'отправить их обратно без заметных усилий, а потом запулить в этот корабль целый поток '
                               'обломков зданий, хотя сбить так и не смогла. В аниме чуть раньше этих событий уронила '
                               'здоровенный метеорит на древнего ящера-кайдзю, благополучно его убив.',
                               reply_markup=keyboard_S_class1_10)
                users[message.from_user.id] = "s-class1_10"
            elif message.text.lower() == 'бэнг':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILEl'
                               '-EW_zknsjzKMleP0vcGYxobOdtAAIFsDEbDEkgSHSeGEDHt1wHuxJwly4AAwEAAwIAA20AAzS8AQABGwQ', "Бэнг")
                bot.send_message(message.chat.id,
                                 'Бэнг Серебряный Клык: 3 место. Восьмидесятилетний дед, самый старый в '
                                 'ассоциации героев, '
                                 'внешне напоминает Солида Снейка. Впервые появляется в арке с метеоритом, '
                                 'там же видит Сайтаму '
                                 'в деле (метеорит, понятное дело, вдребезги). Держит собственное додзё, исповедует стиль боя '
                                 '«Кулак водного потока дробящего камни», благодаря которому он может '
                                 'разбивать осколки от '
                                 'метеорита и рвать на куски монстров драконьего уровня. Может отбивать и '
                                 'танковать очень '
                                 'мощные атаки — прямой удар Мельзальгальда не оставил на нем даже синяков. Благороден и '
                                 'честен, очень уважает Сайтаму. Некогда был наставником одного из суперзлодеев — Гароу, '
                                 'до того, как тот побил всех прочих учеников, получил пенделей от Бэнга и свалил за '
                                 'можай.\nБомб: старший брат Бэнга, в Ассоциации Героев не состоит. Исповедует стиль боя '
                                 '«Кулак '
                                 'вихря режущего железо». Вместе с Бэнгом отправляется на охоту за Гароу.\nЧаранка: студент '
                                 'школы боевых искусств, лучший ученик Бэнга №2: на замену выпнутому на мороз Гароу, '
                                 'хотя по мастерству и рядом с ним не стоял. Парень молодой и временами наивный, '
                                 'но слепо предан наставнику, как Генос — Сайтаме. Бэнг гоняет его в хвост и в гриву, '
                                 'но не только в качестве тренировок — лишь бы в его голове не оставалось места для крамольных '
                                 'мыслей, толкнувших его предшественника на скользкую дорожку. Как и Бомб, в Ассоциацию не '
                                 'входит.', reply_markup=keyboard_S_class1_10)
                users[message.from_user.id] = "s-class1_10"
            elif message.text.lower() == 'атомный самурай':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILE1'
                               '-EXAPscCD0UYgWQbAsdEh3VpScAAIGsDEbDEkgSPFDvFUuHg5u529Ali4AAwEAAwIAA3gAA4r7AgABGwQ',
                               'Атомный самурай: 4 место. Зовётся так за свой фирменный приём — «Разрез на атомы» — '
                               'сверхбыстрая шинковка противника на мелкие кусочки. Плюс он носит на плаще знак в виде атома '
                               'со множеством электронных орбиталей, а гарда его меча также стилизованна под этот атом. '
                               'Наставник Иайана и еще двоих героев А-класса, очень ими дорожит. Сражался с Мельзальгальдом '
                               'вместе с еще несколькими героями. Входит в некое сообщество крутых фехтовальщиков. Во время '
                               'штурма Ассоциации монстров без проблем кромсал всё, что шевелится, но столкнувшись с '
                               'Черноспермием — что выращивал свои копии из своих же кусочков — выгреб по полной.',
                               reply_markup=keyboard_S_class1_10)
                users[message.from_user.id] = "s-class1_10"
            elif message.text.lower() == 'ребёнок-император':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILFF-EXAmRTstNuA9tAilE3l2gE2k'
                               '-AAIHsDEbDEkgSEMbop7W29iuvMJImC4AAwEAAwIAA20AA7qoAQABGwQ',
                               'Ребёнок-Император: 5 место. Десятилетний шкет с соответствующими повадками, однако наделён '
                               'гениальным интеллектом, благодаря чему смог создать множество смертоносных гаджетов, '
                               'которые умещаются в рюкзачке, с которым малец никогда не расстаётся. Собственно, без него он '
                               'значительно слабее, хотя паренек довольно развит физически (сильнее Стингера) и также хороший '
                               'стратег. Образ вдохновлён мелким суперзлодеем Гизмо из мультсериала «Teen Titans».',
                               reply_markup=keyboard_S_class1_10)
                users[message.from_user.id] = "s-class1_10"
            elif message.text.lower() == 'бофой':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILFV-EXBF-9JHSGGaihYFEsZWyTPT8AAIIsDEbDEkgSDnvflu7cNQGVZ2jli4AAwEAAwIAA3gAA'
                               '-eIAgABGwQ',
                               'Бофой Стальной Рыцарь: 6 место. Неизвестный ученый-кибернетик. Никогда не сражается сам, '
                               'отправляя дистанционно управляемого летающего робота. Эгоистичен. Появляется в истории с '
                               'метеоритом, норовящим обрушится на город Z, исключительно затем, чтобы испытать новые ракеты. '
                               'Ракеты не помогли и Бофой убрался подальше. Перестроил штаб Ассоциации героев после вторжения '
                               'Бороса. Попытался напасть на Древнюю многоножку, но не смог её даже поцарапать, и та утащила '
                               'робота в логово Ассоциации монстров.',
                               reply_markup=keyboard_S_class1_10)
                users[message.from_user.id] = "s-class1_10"
            elif message.text.lower() == 'кинг':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILFl'
                               '-EXBpmGU0C9_ffj4MGq3x5N6TUAAIJsDEbDEkgSINZs6Sg6Gzixsjxly4AAwEAAwIAA3gAA5OaAQABGwQ',
                               'Кинг: 7 место. Тролль, лжец и, вероятно, девственник. В прошлом киберспортсмен. Сей персонаж '
                               'обладает феноменальными удачей и невезением одновременно. Кинг постоянно оказывался между '
                               'Сайтамой и какой-нибудь наковальней, и как-то так получалось, что слава за сраженных Сайтамой '
                               'монстров всегда падала на Кинга. В результате Кинга стали считать непобедимым героем и самым '
                               'сильным человеком на Земле, хотя единственное, что Кинг умеет — сохранять хорошую мину при '
                               'любой игре. Сайтама однажды узнал про это, но заморачиваться не стал и подружился с Кингом. В '
                               'одиночку сдерживал четверых монстров драконьего уровня одними словами. Возможно является '
                               'скрытым эспером, манипулирующим вероятностями.',
                               reply_markup=keyboard_S_class1_10)
                users[message.from_user.id] = "s-class1_10"
            elif message.text.lower() == 'зомбимен':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILF1-EXCJ8'
                               '-xMlp4Os_sKbxminzcG5AAIKsDEbDEkgSJi7VuMbZrTGq6NMli4AAwEAAwIAA3gAAw_zAgABGwQ',
                               'Образец № 66 Зомбимен: 8 место. Эксперимент Палаты эволюции, благодаря чему обладает очень '
                               'мощной регенерацией. И на этом его преимущества и заканчиваются — физически он не слишком '
                               'силён, боевыми навыками тоже не блещет, хотя владение огнестрелом у него вполне на уровне. По '
                               'словам ONE — слабейший в S классе. Во время штурма гнезда монстров сражался с '
                               'монстром-вампиром, и победил фактически измором.',
                               reply_markup=keyboard_S_class1_10)
                users[message.from_user.id] = "s-class1_10"
            elif message.text.lower() == 'технорыцарь':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILGF-EXCijsccrz7FSB2bslgRJwrIEAAILsDEbDEkgSChohhq'
                               '--1ycn9fXly4AAwEAAwIAA20AAw6BAQABGwQ',
                               'Технорыцарь: 9 место. Очередная темная лошадка. Представляет собой то ли разумного робота, '
                               'то ли киборга полной конверсии. Предпочитает сперва изучать врага, дабы побеждать с минимум '
                               'проблем (для чего не гнушается захватывать монстров в плен для живительного вскрытия, '
                               'облутывать покойничков, да и союзниками рискнуть может). В качестве оружия использует '
                               'многоцелевой механизм-трансформер, видимо состоящий из наночастиц. Показанные формы (названия '
                               'основаны на японских шахматах сёги): «Копьё» — мотоцикл с ракетными установками, '
                               '«Конь» — превращает Рыцаря в кентавра, «Ладья» — миниатюрный реактивный истребитель, '
                               '«Слон» — монструозная меха, «Серебро» — меч, и «Золото» — силовой доспех, способный '
                               'раскаляться до огромной температуры. В арке с пришельцами предупреждает Геноса остерегаться '
                               'Бофоя. Показал свою силу в арке Ассоциации монстров. Считает, что Бофой стремится захватить '
                               'мир и специально пожертвовал своим роботом, чтобы монстры смогли изучить его и через это '
                               'разделаться с героями.',
                               reply_markup=keyboard_S_class1_10)
                users[message.from_user.id] = "s-class1_10"
            elif message.text.lower() == 'свинобог':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILGV-EXCzMOshcZWfHf'
                               '-RDMhbBI0PwAAIMsDEbDEkgSMB_udsWKox7Ow3Hly4AAwEAAwIAA3gAAzWAAQABGwQ',
                               'Свинобог: 10 место. Этот товарищ специализируется на пожирании всего, что только можно. В том '
                               'числе и врагов. Еда помогает ему регенерировать. При этом он весьма силён и быстр (хотя по '
                               'нему не скажешь), а его жирок отлично защищает от ударов. Возможно, монстр, которому нравится '
                               'кушать монстров.',
                               reply_markup=keyboard_S_class1_10)
                users[message.from_user.id] = "s-class1_10"
            elif message.text.lower() == 'сверхлитой темноблеск':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILGl'
                               '-EXDCDSDXOYkaHrQVUzYgZoz68AAINsDEbDEkgSJsRPJFvxgoqyvLAly4AAwEAAwIAA3gAA89_AQABGwQ',
                               'Сверхлитой Темноблеск/Воронёный Суперсплав: 11 место. Огромный накачанный негр(?) в плавках. '
                               'Известно, что в детстве он был довольно слабым (и белым), но однажды ему подарили гантели и '
                               'будущий Суперсплав долгое время усердно занимался. В итоге он пришел к мастерству во всех '
                               'видах спорта. Обладает невероятно прочными кожей и мышцами а в грубой физухе превосходит всех '
                               'в S-классе, при этом быстр и ловок. Довольно долго держался против пробуждающегося Гароу ('
                               'который уже был способен снести Зека одним ударом), и лишь как следует раскочегарившись по '
                               'ходу боя, Гароу смог победить. Поражения так потрясло Суперсплава, что он оставил пост героя '
                               'и переквалифицировался в инструкторы для начинающих.',
                               reply_markup=keyboard_S_class11_17)
                users[message.from_user.id] = "s-class11_17"
            elif message.text.lower() == 'сторожевой пёс':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILG1'
                               '-EXDUiaIEk2fT3B5NHHXfmmFXaAAIOsDEbDEkgSCMV0NKhz9Y5Xxfnly4AAwEAAwIAA20AA4StAQABGwQ',
                               'Сторожевой Пес: 12 место. Назван так за то, что носит собачий костюм. Приставлен к городу Q, '
                               'считающимся «горячей точкой», с задачей по его защите (в одиночку) справляется на пять. Похож '
                               'на Сайтаму тем, что как и он проживает в неблагополучном и опасном городе (Q, как и Z таковым '
                               'являются), внешне всегда спокоен и даже пофигистичен, с виду невзрачен (не считая костюма) и '
                               'пробивался с самых низов C класса. Костюм до боли напоминает Хатико.',
                               reply_markup=keyboard_S_class11_17)
                users[message.from_user.id] = "s-class11_17"
            elif message.text.lower() == 'световой флэш':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILHF'
                               '-EXDpQnUUB_wp4iPIhY_iPgueXAAIPsDEbDEkgSKjfbcSp7HVEd7OUly4AAwEAAwIAA20AA3yrAQABGwQ',
                               'Световой Флэш: 13 место. Фактически, является героической версией Звукового Соника (о котором '
                               'ниже): воспитывался в деревне ниндзя (той же, что и Соник), невероятно ловкий и скоростной, '
                               'сражается катаной, обладает тонкой фигурой и женоподобным лицом. Быстр настолько, '
                               'что может носится по воде, стенам и потолку, даже по водопаду способен взбежать. Выносливость '
                               'соответствующая. В свободное время, по его словам, в промышленных масштабах выносит вперед '
                               'ногами различные бандформирования.',
                               reply_markup=keyboard_S_class11_17)
                users[message.from_user.id] = "s-class11_17"
            elif message.text.lower() == 'мастер в майке':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILHl-EXEVBei3OEM-QM7dTQIc09A'
                               '-lAAIRsDEbDEkgSM3qESuUsj_Rr2cWmC4AAwEAAwIAA20AA5yqAQABGwQ')
                bot.send_message(message.chat.id,
                                 'Мастер в майке: 15 место. Первый (во всех смыслах) «герой в майке» и неформальный лидер '
                                 'своих '
                                 'подражателей-героев — таких же «маечников» (которых навскидку около десятка). Высок, '
                                 'мускулист и весьма силен. Является последователем странной философии, согласно которой майка '
                                 'является источником силы, но по факту просто качок. Впервые появляется в арке с пришельцами, '
                                 'но ничего дельного не показывает. Далее со всей своей компанией натыкается на Гароу (еще не '
                                 'зная, кто это), которого специально искал с целью набить рожу за Вегетарианца. Одним ударом '
                                 'отшвырнул Гароу, сотряс землю ударом кулака, после чего бросился на таран. Гароу выдержал и '
                                 'это, и еще несколько затрещин. Мастер нюхом почуял, что Гароу нужно быстрее уделать, '
                                 'однако под его удар подставился Ездок, сказав Мастеру, что пора завязывать. Мастер было '
                                 'согласился, но Гароу опять напал, применив таки «Кулак горного потока дробящего камни» и '
                                 'буквально вбил Мастера в стену. В больнице Мастер кое-что рассказал Сайтаме, пришедшему '
                                 'проведать Ездока, о Гароу. По своим силам он фактически Сайтама-лайт: быстро бегает, '
                                 'очень сильно бьет, крепок сам по себе, но более никаких чудес.',
                                 reply_markup=keyboard_S_class11_17)
                users[message.from_user.id] = "s-class11_17"
            elif message.text.lower() == 'стальная бита':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILHV'
                               '-EXEAqcBYRfd4zTd1OAWWMNwXpAAIQsDEbDEkgSF625NbehySJnqDoly4AAwEAAwIAA3gAA4GsAQABGwQ',
                               'Стальная Бита: 16 место. Типичный японский гопник-фурёу во всем — от стиля одежды до манеры '
                               'говорить. И причесона Элвис-стайл. Помимо отличного владения, собственно, стальной битой, '
                               'обладает бойцовским духом — чем сильнее Бите досталось (неважно как — можно и самого себя по '
                               'башке приложить) — тем он сильнее, быстрее и устойчивее (в том числе к ядам). Согласно Слову '
                               'Божьему — вполне может затащить сухого Морского Царя. Первым (хоть и случайно) разгадал '
                               'слабость Мельзальгальда. Очень любит младшую сестру. После появления Гароу был назначен '
                               'телохранителем какой-то связанной с Ассоциацией шишки. Защищая эту самую шишку: без особых '
                               'проблем уделал пару монстров дьявольского уровня, но вот здоровенную многоножку драконьего — '
                               'не осилил, а потом сцепился с вездесущим Гароу. Продержался довольно долго, но, '
                               'понятное дело, не победил и наверняка бы склеился, если бы не его младшая сестра — Гароу '
                               'не трогает детей. Едва не рванул «добивать» многоножку, но сестренка своим подзатыльником '
                               'снесла гопнику последние ХП.',
                               reply_markup=keyboard_S_class11_17)
                users[message.from_user.id] = "s-class11_17"
            elif message.text.lower() == 'гомо-гомо зек':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILH1-EXEgdEBUmcYPKfXVd2KD0TJ9pAAISsDEbDEkgSPSIs4iTHbN6cE3zly4AAwEAAwIAA3gAA'
                               '-ucAQABGwQ')
                bot.send_message(message.chat.id,
                                 'Гомо-гомо Зек (изначальное имя «Pri-Pri-Prisoner» (ぷりぷりプリズナー Puripuri purizunā), '
                                 'что-то вроде '
                                 '«Нежно-ласковый узник»): 17 место. Эпический крутой и штатный гей Ассоциации Героев. Явная '
                                 'пародия на мангу One Piece. Большую часть времени сидит в тюрьме «Погань под крышкой», '
                                 'где содержатся самые опасные преступники (солидная часть из которых поймана им самим), '
                                 'которых простая тюряга не удержит. Надо сказать, надёжность обеспечивается не хитрющими '
                                 'системами контроля, а банальной толщиной стен и дверей. Разумеется, Зек в этой тюрьме '
                                 'главный '
                                 'пахан и все заключенные боятся его, как огня. Видя в новостях (у него есть телевизор) '
                                 'очередного плохого и симпатичного парня, Зек сбегает из тюрьмы, проламывая стену, '
                                 'ловит бедолагу и вместе с ним садится обратно за побег. Пришёл на помощь Стингеру и '
                                 'Максу-молнии (к которым неравнодушен) в битве с Морским царём и проиграл, хотя этих двоих '
                                 'спас. В аниме навестил их в больнице, и бедолаги оттуда чесанули так, что только пятки '
                                 'сверкали. Впоследствии сражался с Мельзальгальдом, где был серьёзнее и показал себя с лучшей '
                                 'стороны. Атакует преимущественно шквалами ударов, а всякий раз, когда он напрягает мышцы, '
                                 'те рвут его одежду в клочья. К арке Ассоциации монстров прокачался, стал еще сильнее, '
                                 'а во время штурма гнезда научился вибрировать всем телом так, что мог плавать в сплошном '
                                 'камне и рушить стены касанием пальца. Случайно нашел полудохлого Гароу (в лицо его Зек не '
                                 'знал) и решил освободить, но тот свалил Зека одним ударом.',
                                 reply_markup=keyboard_S_class11_17)
                users[message.from_user.id] = "s-class11_17"
            elif message.text.lower() == 'сайтама':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILIV-EXFDriBeWcqs6zie5J46gh_'
                               '-LAAIUsDEbDEkgSOxO7ND8ETQpQ0wQmC4AAwEAAwIAA20AA6CpAQABGwQ')
                bot.send_message(message.chat.id,
                                 'Сайтама: 7 место в B классе. Протагонист. Он же «Человек-Один-Удар» и «Лысый Плащ» ('
                                 'официальное прозвище в Ассоциации '
                                 'Героев). Спасая пацана от монстра, Сайтама возжелал стать супергероем, для чего начал '
                                 'усердно '
                                 'тренироваться каждый день, без всякой халтуры. Он занимался этим так усердно, что облысел ('
                                 'лысина — его больная мозоль), зато обрёл совершенно чудовищную физическую мощь (судя по '
                                 'всему, только её — владение какими-либо энергиями Сайтама не показал). Он не знает усталости '
                                 'в бою (но запыхается, если будет долго бегать на большой (для себя) скорости), не мёрзнет в '
                                 'космосе и не сгорает в атмосфере, его скорость близка к световой, прочность позволяет '
                                 'выдерживать атаки континентальных и выше мощностей без единой царапины, а его сила позволяет '
                                 'прыжком за несколько секунд преодолеть расстояние от Луны до Земли (правда… теоретически, '
                                 'способен задохнуться, ибо именно в этом и была причина его дискомфорта на Луне) и '
                                 'перемалывать врагов в фарш несильным ударом. Причем, в мгновение перед ударом противника '
                                 'сковывает ужас понимания того, насколько велика разница в уровнях, и он буквально видит себя '
                                 'очень маленьким по сравнению с огромным Человеком-Одним-Ударом. Согласно Слову Божьему (если '
                                 'это действительно оно — информация пока неподтвержденная) — сильнейший удар Сайтамы по мощи '
                                 'равен Большому Взрыву. При этом, Сайтама не владеет никакими боевыми искусствами, '
                                 'они ему без '
                                 'надобности.\n\nКазалось бы, готова Мэри Сью c унылой непобедимостью, но история построена '
                                 'так, '
                                 'что непобедимость Сайтамы ловкими и умелыми телодвижениями автора превращается в лихую и '
                                 'веселую. И он скорее пародия на Мэри Сью, чем сабж. Тут рушится битый тыщу раз штамп, '
                                 'в котором протагонисты сёнен-манги постоянно огребают и прочим героям приходится их выручать '
                                 '— тут «прочих» то и дело нагибают, а Сайтама вразвалочку приходит и флегматично поправляет '
                                 'всё. Ну и еще за Сайтамой не бегают поклонницы — романтические линии в манге отсутствуют '
                                 'напрочь, Сайтама не проявляет к этой стороне жизни никакого интереса.\n\nСам Сайтама '
                                 'несколько '
                                 'страдает от своей мощи, так как не может почувствовать ни радости победы, ни горечи '
                                 'поражения, ни напряжения во время боя или даже самого обыкновенного страха. То, '
                                 'что количество вражин не уменьшается, его абсолютно не волнует, так как Сайтама играет в '
                                 'героя исключительно ради самоудовлетворения. Также ему до лампочки мнение о его делах, '
                                 'хотя вот против известности Сайтама ничего не имеет, даже наоборот. Тем не менее, Сайтама не '
                                 'ставит геройство в приоритет, его больше волнует распродажи в ближайшем магазине. Живёт он в '
                                 'заброшенном районе города Z, нигде не работает, в свободное время штудирует мангу. Большую '
                                 'часть времени Сайтама находится в расслабленно-пофигистичном состоянии. Однако стоит '
                                 'отметить, что Сайтама совершенно не против кому-то помочь, ничего не требуя взамен ('
                                 'например, '
                                 'однажды он спасает самоубийцу и советует ему перед очередным прыжком с небоскрёба '
                                 'убеждаться, '
                                 'что он там обедает — юмора ситуации добавляет то, что этот самоубийца с небоскрёба уже не '
                                 'прыгнул, а сорвался — от осознанного самоубийства Сайтама даже не думал его '
                                 'останавливать).\n\nВ ассоциации героев Сайтама сперва очутился на последнем месте (едва сдал '
                                 'письменный тест на чувство справедливости, вероятно ответив на все вопросы «Убью на месте!», '
                                 'зато в физическом тесте побил все рекорды), но быстро помчался вверх. На данный момент он на '
                                 '39 месте в А-классе.\n\nЕще одна особенность Сайтамы — правда, не его личная — он нарисован '
                                 'в '
                                 'значительно более упрощенном стиле, чем всё остальное, и выглядит плоским. Трёхмерность же '
                                 'обретает только в моменты, когда выходит из своего пофигистичного состояния.',
                                 reply_markup=keyboard_heroes)
                users[message.from_user.id] = "heroes"
            elif message.text.lower() == 'генос':
                bot.send_photo(message.chat.id,
                               'AgACAgIAAxkBAAILIF-EXExJZEnoshbo9'
                               '-YmblwFxijNAAITsDEbDEkgSCKwCUuKC42tOaHoly4AAwEAAwIAA3gAAw2uAQABGwQ')
                bot.send_message(message.chat.id,
                                 'Генос Кибер-демон (фанская кличка — Гена-геноцид): 14 место. Крутой киборг, парень лет 19 от '
                                 'роду. В манге появляется, сражаясь с Комарихой, которая разорвала его на куски и уже '
                                 'собиралась прикончить, но Сайтама убил тварь одной затрещиной, немало впечатлив блондинчика, '
                                 'который тут же записался к лысому в ученики. Предыстория его в том, что на место обитания '
                                 'Геноса напал сумасшедший киборг, перебивший всё живое, но проходивший мимо ученый, '
                                 'как раз гонявшийся за этим киборгом, спас Геноса, превратив его в киборга, и с той поры '
                                 'паренёк сражается со злом везде, где может найти (причем, эта история изложена в манге '
                                 'просто '
                                 'стеной текста, в которой прямо слышится монотонный негромкий бубнёж — судя по реакции '
                                 'Сайтамы, которому пришлось эту канитель выслушивать, в аниме же монолог получился с '
                                 'эмоциями). Называет Сайтаму учителем (тот, хотя и заботится о Геносе по мере сил, '
                                 'себя его учителем отнюдь не считает), но никак не может поверить, что силы своей лысый '
                                 'добился лишь тренировками. Живёт на хате Сайтамы, где в свободное время наводит порядок, '
                                 'в качестве оружия использует встроенные в руки энергетические орудия. От живого тела в нём '
                                 'остался, от силы, кусок мозга. Собственно, Генос введён затем, чтобы демонстрировать '
                                 'типичную '
                                 'сёнёнскую крутизну, пафос и превозмогание, посему постоянно огребает люлей (в основном — '
                                 'из-за собственной самоуверенности), а потом приходит Сайтама и всё разруливает.',
                                 reply_markup=keyboard_heroes)
                users[message.from_user.id] = "heroes"
            else:
                diction1 = dict()
                diction1["а"] = False
                diction1["х"] = False
                diction2 = dict()
                diction2["a"] = False
                diction2["x"] = False
                for elements in message.text:
                    diction1[elements] = True
                    diction2[elements] = True
                if len(diction1) == 2:
                    if diction1["а"] & diction1["х"]:
                        bot.send_sticker(message.chat.id,
                                         'CAACAgIAAxkBAAICS194ydWLC4fWqJemCSDqKAyyc3YWAAJ-CAACeVziCWn3Vn6MWgfLGwQ',
                                         reply_markup=keyboard1)
                elif len(diction2) == 2:
                    if diction2["a"] & diction2["x"]:
                        bot.send_sticker(message.chat.id,
                                         'CAACAgIAAxkBAAICS194ydWLC4fWqJemCSDqKAyyc3YWAAJ-CAACeVziCWn3Vn6MWgfLGwQ',
                                         reply_markup=keyboard1)
                else:
                    bot.send_message(message.chat.id, 'Такой команды нет(', reply_markup=keyboard1)


        @bot.message_handler(content_types=['sticker'])
        def stic(message):
            print(message)
            bot.send_message(message.chat.id, 'Бот пока не умеет анализировать данные в таком формате', reply_markup=keyboard1)


        @bot.message_handler(content_types=['location'])
        def stic2(message):
            bot.send_message(message.chat.id, 'Бот пока не умеет анализировать данные в таком формате', reply_markup=keyboard1)


        @bot.message_handler(content_types=['document', 'audio', 'voice'])
        def stic4(message):
            bot.send_message(message.chat.id, 'Бот пока не умеет анализировать данные в таком формате', reply_markup=keyboard1)


        def for_each(mes, message):
            if mes == "1 сезон 1 серия":
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIEUl99o5VkWx705sJHkytcizfsbxApAAIqBwACxgToS8IaYfdux8BTGwQ',
                               caption="1 сезон 1 серия",
                               reply_markup=keyboard1)
            elif mes == "1 сезон 2 серия":
                bot.send_video(message.chat.id, 'BAACAgIAAxkBAAIEGF98soS6SwESAAGNKrwGa9D03rfNZwACXQkAAs8g4Uuwrs_p9fXKuRsE',
                               caption="1 сезон 2 серия",
                               reply_markup=keyboard1)
            elif mes == "1 сезон 3 серия":
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIEa199qbm-w1LGvCVdnz_tRRUNlV-LAAIwBwACxgToS90JonV1-xnqGwQ',
                               caption="1 сезон 3 серия",
                               reply_markup=keyboard1)
            elif mes == "1 сезон 4 серия":
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIEbF99qsMFaZZT-Jp2rK--L0G3v26rAAIyBwACxgToS7uyXb1gLh_BGwQ',
                               caption="1 сезон 4 серия",
                               reply_markup=keyboard1)
            elif mes == "1 сезон 5 серия":
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIQrV-NoDGgHCHmxhm7SMqUdCrgoHyyAAK3CAAC6HZpSEimdIfOZFkiGwQ',
                               caption="1 сезон 5 серия",
                               reply_markup=keyboard1)
            elif mes == "1 сезон 6 серия":
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIEbl99q9UFvSqrdhj-h-TeQ59aoIcoAAI0BwACxgToSxwJED5X_16JGwQ',
                               caption="1 сезон 6 серия",
                               reply_markup=keyboard1)
            elif mes == "1 сезон 7 серия":
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIFp19-FZwMBXVI_fLqrOvk1GjZZyahAAJ4CAACxgTwS0DaYL4-gficGwQ',
                               caption="1 сезон 7 серия",
                               reply_markup=keyboard1)
            elif mes == "1 сезон 8 серия":
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIFqF9-FfSQFrBBhlKdob5m8BcJWouEAAJ5CAACxgTwS3tOrWw_WP1bGwQ',
                               caption="1 сезон 8 серия",
                               reply_markup=keyboard1)
            elif mes == "1 сезон 9 серия":
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIFqV9-FksxOuH60DbX0IwhOROa2DQtAAJ6CAACxgTwS6Vqe6Xt-KkVGwQ',
                               caption="1 сезон 9 серия",
                               reply_markup=keyboard1)
            elif mes == "1 сезон 10 серия":
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIFql9-FsZsoUo8OevNIeFi8G2ZQGQdAAJ7CAACxgTwSz8utxELtvJDGwQ',
                               caption="1 сезон 10 серия",
                               reply_markup=keyboard1)
            elif mes == "1 сезон 11 серия":
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIFu19-F2cYB6svzdBKLRjqegg_luunAAJ9CAACxgTwS2jIRW5amKopGwQ',
                               caption="1 сезон 11 серия",
                               reply_markup=keyboard1)
            elif mes == "1 сезон 12 серия":
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIFvF9-F9Az-Jy5s07-QrdOV7kRVjpBAAJ-CAACxgTwSz_qlJRUhGdtGwQ',
                               caption="1 сезон 12 серия",
                               reply_markup=keyboard1)
            elif mes == '2 сезон 1 серия':
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGB19_YS_iinTESuN2o9y9weZxaFLeAAL0CwAChuT5S4gs3RSvnGaxGwQ',
                               caption="2 сезон 1 серия",
                               reply_markup=keyboard1)
            elif mes == '2 сезон 2 серия':
                bot.send_video(message.chat.id,
                               'BAACAgIAAxkBAAIGCF9_YmUgBkKt_JnKv6JTqw30BOHnAAL5CwAChuT5S1kqVv9Hm4j-GwQ',
                               caption="2 сезон 2 серия",
                               reply_markup=keyboard1)


        def picture2(message):
            file_user = bot.get_file_url(message.photo[-1].file_id)
            f = open('out_search.jpg', 'wb')
            f.write(urllib.request.urlopen(file_user).read())
            f.close()

            file = Image.open('out_search.jpg')

            our = imagehash.phash(file)

            it_end = int(str(our), 16)
            sql = f"""SELECT picturehashes.picturename, series.seriesname, series.fileid, BIT_COUNT(phash ^ '{it_end}'), 
            picturehashes.times
            FROM picturehashes,series
            WHERE picturehashes.sid=series.id and
            BIT_COUNT(phash ^ '{it_end}')=(SELECT MIN(BIT_COUNT(phash ^ '{it_end}'))
            FROM picturehashes) LIMIT 1;"""

            cursor.execute(sql)
            result = cursor.fetchall()
            if result[0][3] < 12:
                bot.send_photo(message.chat.id, open(result[0][0], 'rb'), caption="Максимально похожая картинка",
                               reply_markup=keyboard1)
                bot.send_video(message.chat.id, result[0][2],
                               caption="Картинка из " + result[0][1] + "\n\nМомент в серии: " + result[0][4],
                               reply_markup=keyboard1)
            else:
                bot.send_message(message.chat.id, "По вашему запросу ничего не найдено.\n", reply_markup=keyboard1)


        def trying():
            cap = cv2.VideoCapture('seas1_spec_ser6.mp4')

            i = 0

            while (True):
                i += 1
                ret, frame = cap.read()
                if not ret:
                    return

                if i % 7 == 0:
                    s = "OVA_seas1_ser6_" + str(i / 7) + ".jpg"
                    f = open(s, 'wb')
                    cv2.imwrite(s, frame)
                    file = Image.open(s)
                    our = imagehash.phash(file)

                    it_end = int(str(our), 16)
                    print(i / 7)
                    sql = """INSERT INTO picturehashes(phash, picturename, sid, times) VALUES(%s, %s, %s, %s)"""
                    recordTuple = (it_end, s, 36, time.strftime('%M:%S', time.gmtime(int(cap.get(0) / 1000))))
                    cursor.execute(sql, recordTuple)
                    conn.commit()


        # trying()


        @bot.message_handler(content_types=['photo'])
        def stic5(message):
            starti(message)
            if users[message.from_user.id] == "find_picture":
                picture2(message)
                users[message.from_user.id] = "join"
            else:
                print(message)


        @bot.message_handler(content_types=['video'])
        def stic6(message):
            print(message)
            bot.send_message(message.chat.id, 'Бот пока не умеет анализировать данные в таком формате', reply_markup=keyboard1)


        bot.polling(none_stop=True, timeout=1230)
        # bot.infinity_polling(20000)
        # if __name__ == '__main__':
        # main()
    except Exception:
        continue