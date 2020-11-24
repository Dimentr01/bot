import telebot
import emoji

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
