import telebot
from telebot import types
import requests
import json

photos = {
    'LiquidName': 'AgACAgIAAxkBAAID6WQgrbvxNRvm5gZ2M7cwIvGu2buDAAJPzjEbvcoISWsZ3UWHq21gAQADAgADeAADLwQ',
    'PodName': 'AgACAgIAAxkBAAID6WQgrbvxNRvm5gZ2M7cwIvGu2buDAAJPzjEbvcoISWsZ3UWHq21gAQADAgADeAADLwQ',
    'SnusName': 'AgACAgIAAxkBAAID6WQgrbvxNRvm5gZ2M7cwIvGu2buDAAJPzjEbvcoISWsZ3UWHq21gAQADAgADeAADLwQ',
    'SingleUseName': 'AgACAgIAAxkBAAID6WQgrbvxNRvm5gZ2M7cwIvGu2buDAAJPzjEbvcoISWsZ3UWHq21gAQADAgADeAADLwQ',
    'ConsName': 'AgACAgIAAxkBAAID6WQgrbvxNRvm5gZ2M7cwIvGu2buDAAJPzjEbvcoISWsZ3UWHq21gAQADAgADeAADLwQ',
}




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
        markup.add(vlad)
        msg = '<b>Курьеры:</b>'
        bot.send_message(message.chat.id, msg, parse_mode='html', reply_markup=markup)
        return 0

    elif message.text == 'Ассортимент':
        msg = '<b>Выберите нужные товары</b>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        liquids = types.KeyboardButton('Жидкости')
        pods = types.KeyboardButton('Поды')
        consumables = types.KeyboardButton('Разходники')
        snus = types.KeyboardButton('Снюс')
        single_use = types.KeyboardButton('Одноразки')
        back = types.KeyboardButton('Назад')
        markup.add(liquids, pods, consumables, snus, single_use, back)
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
        
        response = requests.get("http://127.0.0.1:8000/api/liquids").json()
        response_brand = requests.get("http://127.0.0.1:8000/api/liquid-brands").json()
        for brand in response_brand:
            # отправка названия бренда
            bot.send_message(message.chat.id, f"Жидкости бренда {brand['name']}:", parse_mode='html')
            # отправка фото
            photo_url = brand['image']
            photo_response = requests.get(photo_url)
            photo = photo_response.content
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'Есть в наличии:', parse_mode='html')
            is_there = 0
            for liquid in response:
                if liquid['brand']['name'] == brand['name']:
                    if liquid['amount'] > 0:
                        is_there += 1
                        msg = f'{liquid["name"]}\nЦена: {liquid["price"]} ₽'


                        bot.send_message(message.chat.id, msg, parse_mode='html')
            if is_there == 0:
                bot.send_message(message.chat.id, 'На данный момент в наличии экземпляров нет', parse_mode='html')

        return 0
    elif message.text == 'Поды':
        response = requests.get("http://127.0.0.1:8000/api/pods/").json()
        response_brand = requests.get("http://127.0.0.1:8000/api/pod-brands/").json()
        for brand in response_brand:
            # отправка названия бренда
            bot.send_message(message.chat.id, f"Поды бренда {brand['name']}:", parse_mode='html')
            # отправка фото
            photo_url = brand['image']
            photo_response = requests.get(photo_url)
            photo = photo_response.content
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'Есть в наличии:', parse_mode='html')
            is_there = 0
            for pod in response:
                if pod['brand']['name'] == brand['name']:
                    if pod['amount'] > 0:
                        is_there += 1
                        msg = f'{pod["name"]}\nЦена: {pod["price"]} ₽'

                        bot.send_message(message.chat.id, msg, parse_mode='html')
            if is_there == 0:
                bot.send_message(message.chat.id, 'На данный момент в наличии экземпляров нет', parse_mode='html')
        return 0
    elif message.text == 'Снюс':
        response = requests.get("http://127.0.0.1:8000/api/snuses/").json()
        response_brand = requests.get("http://127.0.0.1:8000/api/snus-brands/").json()
        for brand in response_brand:
            # отправка названия бренда
            bot.send_message(message.chat.id, f"Снюс бренда {brand['name']}:", parse_mode='html')
            # отправка фото
            photo_url = brand['image']
            photo_response = requests.get(photo_url)
            photo = photo_response.content
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'Есть в наличии:', parse_mode='html')
            is_there = 0
            for snus in response:
                if snus['brand']['name'] == brand['name']:
                    if snus['amount'] > 0:
                        is_there += 1
                        msg = f'{snus["name"]}\nЦена: {snus["price"]} ₽'

                        bot.send_message(message.chat.id, msg, parse_mode='html')
            if is_there == 0:
                bot.send_message(message.chat.id, 'На данный момент в наличии экземпляров нет', parse_mode='html')
        return 0
    elif message.text == 'Одноразки':
        response = requests.get("http://127.0.0.1:8000/api/singles/").json()
        response_brand = requests.get("http://127.0.0.1:8000/api/single-brands/").json()
        for brand in response_brand:
            # отправка названия бренда
            bot.send_message(message.chat.id, f"Одноразки бренда {brand['name']}:", parse_mode='html')
            # отправка фото
            photo_url = brand['image']
            photo_response = requests.get(photo_url)
            photo = photo_response.content
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'Есть в наличии:', parse_mode='html')
            is_there = 0
            for single in response:
                if single['brand']['name'] == brand['name']:
                    if single['amount'] > 0:
                        is_there += 1
                        msg = f'{single["name"]}\nЦена: {single["price"]} ₽'

                        bot.send_message(message.chat.id, msg, parse_mode='html')
            if is_there == 0:
                bot.send_message(message.chat.id, 'На данный момент в наличии экземпляров нет', parse_mode='html')
        return 0
    
    elif message.text == 'Разходники':
        response = requests.get("http://127.0.0.1:8000/api/consumables/").json()
        response_brand = requests.get("http://127.0.0.1:8000/api/consumables-brands/").json()
        for brand in response_brand:
            # отправка названия бренда
            bot.send_message(message.chat.id, f"Расходники бренда {brand['name']}:", parse_mode='html')
            # отправка фото
            photo_url = brand['image']
            photo_response = requests.get(photo_url)
            photo = photo_response.content
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'Есть в наличии:', parse_mode='html')
            is_there = 0
            for consumable in response:
                if consumable['brand']['name'] == brand['name']:
                    if consumable['amount'] > 0:
                        is_there += 1
                        msg = f'{consumable["name"]}\nЦена: {consumable["price"]} ₽'

                        bot.send_message(message.chat.id, msg, parse_mode='html')
            if is_there == 0:
                bot.send_message(message.chat.id, 'На данный момент в наличии экземпляров нет', parse_mode='html')
        return 0
    

    elif msg_text in greetings:
        msg = '👋'

    else:
        for i in swears:
            if i in msg_text:
                msg = 'не матюкайся у меня мама телефон проверяет'
    bot.send_message(message.chat.id, msg, parse_mode='html')


bot.polling(none_stop=True)
