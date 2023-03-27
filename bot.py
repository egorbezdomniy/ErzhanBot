import telebot
from telebot import types
import requests

photos = {
    'egorbezdomniy': 'AgACAgIAAxkBAAID6WQgrbvxNRvm5gZ2M7cwIvGu2buDAAJPzjEbvcoISWsZ3UWHq21gAQADAgADeAADLwQ',
}

response = requests.get("http://127.0.0.1:8000/api/liquids").json()


greetings = ['hello', 'hi', 'привет', 'здравствуй', 'здравствуйте']

swears = ['хуй', 'блять', 'бля', 'залупа', 'пизд']

token = '6139391767:AAHgSOWxdNako0LSrUImOp5Z2P210jHhDQs'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    msg = f'<b> Привет, {message.from_user.first_name}.</b>\n' \
          f'Команды должны появиться у вас над клавиатурой\n' \
          f'/help - список всех команд'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    assortment = types.KeyboardButton('Ассортимент')
    links = types.KeyboardButton('Ссылки')
    courier = types.KeyboardButton('Курьеры')

    markup.add(assortment, links, courier)
    bot.send_message(message.chat.id, msg, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=["photo"])

def handle_photo(message):

    photo_id=message.photo[2].file_id

    file_info = bot.get_file(photo_id)
    bot.send_message(message.chat.id, photo_id)


@bot.message_handler(commands=['help'])
def start(message):
    msg = '/start - начало работы бота\n' \
          'Жидкости'
    bot.send_message(message.chat.id, msg, parse_mode='html')


@bot.message_handler(content_types=['sticker'])
def get_user_sticker(message):
    msg = 'Норм стикер'
    bot.send_message(message.chat.id, msg)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    msg_text = message.text.lower()
    msg = 'Я вас не понял\n' \
          'Для появления списка команд напишите /help'

    if message.text == 'Ссылки':
        markup = types.InlineKeyboardMarkup()
        chanel = types.InlineKeyboardButton('Канал с новостями', url='https://t.me/erzhanshop')
        reviews = types.InlineKeyboardButton('Отзывы', url='https://t.me/+J54VuPy-YcI2ZDA6')
        markup.add(chanel, reviews)
        msg = '<b>Ccылки:</b>'
        bot.send_message(message.chat.id, msg, parse_mode='html', reply_markup=markup)
        return 0

    elif message.text == 'Курьеры':
        markup = types.InlineKeyboardMarkup()
        vlad = types.InlineKeyboardButton('Основной курьер', url='https://t.me/stupinoo')
        kochan = types.InlineKeyboardButton('Запасной курьер', url='https://t.me/+79857114336')
        markup.add(vlad, kochan)
        msg = '<b>Курьеры:</b>'
        bot.send_message(message.chat.id, msg, parse_mode='html', reply_markup=markup)
        return 0

    elif message.text == 'Ассортимент':
        msg = '<b>Выберите нужные товары</b>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        liquids = types.KeyboardButton('Жидкости')
        pods = types.KeyboardButton('Поды')
        consumables = types.KeyboardButton('Разходники/Одноразки')
        snus = types.KeyboardButton('Снюс')
        used = types.KeyboardButton('б/у')
        back = types.KeyboardButton('Назад')
        markup.add(liquids, pods, consumables, snus, used, back)
        bot.send_message(message.chat.id, msg, parse_mode='html', reply_markup=markup)
        return 0

    elif message.text == 'Назад':
        msg = f'/help - список всех команд'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        assortment = types.KeyboardButton('Ассортимент')
        links = types.KeyboardButton('Ссылки')
        courier = types.KeyboardButton('Курьеры')

        markup.add(assortment, links, courier)
        bot.send_message(message.chat.id, msg, parse_mode='html', reply_markup=markup)
        return 0

    elif message.text == 'Жидкости':

        for i in response:

            if i['ammount'] > 0:
                bot.send_photo(message.chat.id, photo=photos[i["name"]])
                msg = f'Бренд: {i["brand"]}\nИмя: {i["name"]}\nЦена: {i["price"]}'


                bot.send_message(message.chat.id, msg, parse_mode='html')
        return 0



    elif msg_text in greetings:
        msg = '👋'

    else:
        for i in swears:
            if i in msg_text:
                msg = 'не матюкайся у меня мама телефон проверяет'
    bot.send_message(message.chat.id, msg, parse_mode='html')


bot.polling(none_stop=True)
