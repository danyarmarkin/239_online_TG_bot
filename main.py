import telebot
from telebot import types
bot = telebot.TeleBot('1450184958:AAFssh29dL78vhV5gEhKYZifBhWVKGjfPcU')




@bot.message_handler(commands=['start'])
def startText(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Загрузить работу')
    btn2 = types.KeyboardButton('Справка')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Привет!\nЭто 239 Online bot!",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def startText(message):
    print(message.from_user.first_name, message.from_user.last_name, "(" + str(message.from_user.id) + "):", message.text)
    m = message.text.lower()

    if m == "загрузить дз" or "/upload_hw":
        bot.send_message(message.chat.id, "Введите тэг работы")

    if m == "!math_17.02.2021":
        @bot.message_handler(content_types=['photo'])
        def getPhoto(message):
            try:

                file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = message.from_user.first_name + message.from_user.last_name+".png"
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)
                bot.reply_to(message, "Фото добавлено")

            except Exception as e:
                bot.reply_to(message, e)





bot.polling(none_stop=True)