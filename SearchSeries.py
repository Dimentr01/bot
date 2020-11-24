import BotHandlers
import imagehash
import urllib
import db
from PIL import Image
import keyboards


def search_similar_photo(message):
    file_user = BotHandlers.bot.get_file_url(message.photo[-1].file_id)
    f = open('out_search.jpg', 'wb')
    f.write(urllib.request.urlopen(file_user).read())
    f.close()

    file = Image.open('out_search.jpg')

    our = imagehash.phash(file)
    it_end = int(str(our), 16)

    result = db.part_of_search_similar_photo(it_end)

    if result[0][3] < 12:
        # insert your pathway
        BotHandlers.bot.send_photo(message.chat.id,
                                   open("/home/dimentrx/pythonML/" + result[0][0], 'rb'),
                                   caption="Максимально похожая картинка",
                                   reply_markup=keyboards.keyboard1)
        BotHandlers.bot.send_video(message.chat.id, result[0][2],
                                   caption="Картинка из " + result[0][1] + "\n\nМомент в серии: " + result[0][4],
                                   reply_markup=keyboards.keyboard1)
    else:
        BotHandlers.bot.send_message(message.chat.id, "По вашему запросу ничего не найдено.\n",
                                     reply_markup=keyboards.keyboard1)
