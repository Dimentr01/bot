# -*- coding: utf-8 -*-

import traceback
import telebot
import BotHandlers
import BotSendText

while True:
    try:
        @bot.message_handler(commands=['start'])
        def start_message(message):
            BotHandlers.start(message)

        @bot.message_handler(content_types=['text'])
        def send_text(message):
            BotSendText.for_user_text(message)

        @bot.message_handler(content_types=['document', 'audio', 'voice', 'location', 'sticker', 'video'])
        def all_other_handlers(message):
            BotHandlers.other_handlers(message)

        @bot.message_handler(content_types=['photo'])
        def photo_from_user(message):
            BotHandlers.for_photo(message)

        bot.polling(none_stop=True, timeout=1230)
    except Exception:
        print(traceback.format_exc())
        continue
