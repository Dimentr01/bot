# -*- coding: utf-8 -*-
import telebot
import for_bot_handler
import traceback
import all_text_func_bot

while True:
    try:

        bot = telebot.TeleBot('1215578709:AAExaTAxqks3rgp3HuRfVDRBacCso6F1llI')


        # telebot.apihelper.proxy = {'https':'socks5h://88.198.50.103:1080'}

        # code: join=begin, heroes=back to persi, idea=for idea, find_seria=find seria, a-class=back to heroes, persi=glav menu
        # a-class-row...=back to a-class, battles-return to glav

        @bot.message_handler(commands=['start'])
        def start_message(message):
            for_bot_handler.start(message)


        @bot.message_handler(content_types=['text'])
        def send_text(message):
            all_text_func_bot.for_user_text(message)




        @bot.message_handler(content_types=['document', 'audio', 'voice', 'location', 'sticker', 'video'])
        def all_other_handlers(message):
            for_bot_handler.other_handlers(message)


        @bot.message_handler(content_types=['photo'])
        def photo_from_user(message):
            for_bot_handler.for_photo(message)


        bot.polling(none_stop=True, timeout=1230)
        # bot.infinity_polling(20000)
        # if __name__ == '__main__':
        # main()
    except Exception:
        print(traceback.format_exc())
        continue
