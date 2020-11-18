import for_db
import cv2
import imagehash
from PIL import Image
import time
import keyboards
import for_bot_handler


def print_all_users():
    bo = True
    for el in for_bot_handler.users:
        if bo:
            print(el)
        else:
            print(", " + el)
        bo = False


def beginning(message):
    bo = True
    for el in for_bot_handler.users:
        if message.from_user.id == el:
            return
    if bo:
        for_bot_handler.users[message.from_user.id] = "join"
    try:
        sql = """INSERT INTO for_for_bot_handler.bot_handler.users(for_for_bot_handler.bot_handler.usersl) VALUES(%s)"""
        recordtuple = message.from_user.id
        for_db.cursor.execute(sql, recordtuple)
        for_db.conn.commit()
    except Exception:
        return


def photo_slicing():
    cap = cv2.VideoCapture('seas1_spec_ser6.mp4')

    i = 0

    while True:
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
            sql = """INSERT INTO picturehashes(phash, picturename, sid, times) VALUES(%s, %s, %s, %s);"""
            recordtuple = (it_end, s, 36, time.strftime('%M:%S', time.gmtime(int(cap.get(0) / 1000))))
            for_db.cursor.execute(sql, recordtuple)
            for_db.conn.commit()


def send_video(mes, message):
    if mes == "1 сезон 1 серия":
        for_bot_handler.bot.send_video(message.chat.id,
                                       'BAACAgIAAxkBAAIEUl99o5VkWx705sJHkytcizfsbxApAAIqBwACxgToS8IaYfdux8BTGwQ',
                                       caption="1 сезон 1 серия",
                                       reply_markup=keyboards.keyboard1)
    elif mes == "1 сезон 2 серия":
        for_bot_handler.bot.send_video(message.chat.id,
                                       'BAACAgIAAxkBAAIEGF98soS6SwESAAGNKrwGa9D03rfNZwACXQkAAs8g4Uuwrs_p9fXKuRsE',
                                       caption="1 сезон 2 серия",
                                       reply_markup=keyboards.keyboard1)
    elif mes == "1 сезон 3 серия":
        for_bot_handler.bot.send_video(message.chat.id,
                                       'BAACAgIAAxkBAAIEa199qbm-w1LGvCVdnz_tRRUNlV-LAAIwBwACxgToS90JonV1-xnqGwQ',
                                       caption="1 сезон 3 серия",
                                       reply_markup=keyboards.keyboard1)
    elif mes == "1 сезон 4 серия":
        for_bot_handler.bot.send_video(message.chat.id,
                                       'BAACAgIAAxkBAAIEbF99qsMFaZZT-Jp2rK--L0G3v26rAAIyBwACxgToS7uyXb1gLh_BGwQ',
                                       caption="1 сезон 4 серия",
                                       reply_markup=keyboards.keyboard1)
    elif mes == "1 сезон 5 серия":
        for_bot_handler.bot.send_video(message.chat.id,
                                       'BAACAgIAAxkBAAIQrV-NoDGgHCHmxhm7SMqUdCrgoHyyAAK3CAAC6HZpSEimdIfOZFkiGwQ',
                                       caption="1 сезон 5 серия",
                                       reply_markup=keyboards.keyboard1)
    elif mes == "1 сезон 6 серия":
        for_bot_handler.bot.send_video(message.chat.id,
                                       'BAACAgIAAxkBAAIEbl99q9UFvSqrdhj-h-TeQ59aoIcoAAI0BwACxgToSxwJED5X_16JGwQ',
                                       caption="1 сезон 6 серия",
                                       reply_markup=keyboards.keyboard1)
    elif mes == "1 сезон 7 серия":
        for_bot_handler.bot.send_video(message.chat.id,
                                       'BAACAgIAAxkBAAIFp19-FZwMBXVI_fLqrOvk1GjZZyahAAJ4CAACxgTwS0DaYL4-gficGwQ',
                                       caption="1 сезон 7 серия",
                                       reply_markup=keyboards.keyboard1)
    elif mes == "1 сезон 8 серия":
        for_bot_handler.bot.send_video(message.chat.id,
                                       'BAACAgIAAxkBAAIFqF9-FfSQFrBBhlKdob5m8BcJWouEAAJ5CAACxgTwS3tOrWw_WP1bGwQ',
                                       caption="1 сезон 8 серия",
                                       reply_markup=keyboards.keyboard1)
    elif mes == "1 сезон 9 серия":
        for_bot_handler.bot.send_video(message.chat.id,
                                       'BAACAgIAAxkBAAIFqV9-FksxOuH60DbX0IwhOROa2DQtAAJ6CAACxgTwS6Vqe6Xt-KkVGwQ',
                                       caption="1 сезон 9 серия",
                                       reply_markup=keyboards.keyboard1)
    elif mes == "1 сезон 10 серия":
        for_bot_handler.bot.send_video(message.chat.id,
                                       'BAACAgIAAxkBAAIFql9-FsZsoUo8OevNIeFi8G2ZQGQdAAJ7CAACxgTwSz8utxELtvJDGwQ',
                                       caption="1 сезон 10 серия",
                                       reply_markup=keyboards.keyboard1)
    elif mes == "1 сезон 11 серия":
        for_bot_handler.bot.send_video(message.chat.id,
                                       'BAACAgIAAxkBAAIFu19-F2cYB6svzdBKLRjqegg_luunAAJ9CAACxgTwS2jIRW5amKopGwQ',
                                       caption="1 сезон 11 серия",
                                       reply_markup=keyboards.keyboard1)
    elif mes == "1 сезон 12 серия":
        for_bot_handler.bot.send_video(message.chat.id,
                                       'BAACAgIAAxkBAAIFvF9-F9Az-Jy5s07-QrdOV7kRVjpBAAJ-CAACxgTwSz_qlJRUhGdtGwQ',
                                       caption="1 сезон 12 серия",
                                       reply_markup=keyboards.keyboard1)
    elif mes == '2 сезон 1 серия':
        for_bot_handler.bot.send_video(message.chat.id,
                                       'BAACAgIAAxkBAAIGB19_YS_iinTESuN2o9y9weZxaFLeAAL0CwAChuT5S4gs3RSvnGaxGwQ',
                                       caption="2 сезон 1 серия",
                                       reply_markup=keyboards.keyboard1)
    elif mes == '2 сезон 2 серия':
        for_bot_handler.bot.send_video(message.chat.id,
                                       'BAACAgIAAxkBAAIGCF9_YmUgBkKt_JnKv6JTqw30BOHnAAL5CwAChuT5S1kqVv9Hm4j-GwQ',
                                       caption="2 сезон 2 серия",
                                       reply_markup=keyboards.keyboard1)
