import telebot
import random
import os
from telebot import types
import requests
from bs4 import BeautifulSoup as BS

token = '1946264092:AAGTXrii9xH6qoeSGVw34G1OSE3Hri92sNc'
bot = telebot.TeleBot(token)

# @bot.message_handler(content_types=['text'])

# def menu(message):
#     if message.text == "Новости":
#         bot.send_message(message.from_user.id, "Привет!")
#         keys_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         k1 = types.KeyboardButton('/news1')
#         k2 = types.KeyboardButton('/news2')
#         k3 = types.KeyboardButton('/news3')
#         k4 = types.KeyboardButton('/news4')
#         keys_2.add(k1,k2,k3,k4)
#         bot.send_message(message.from_user.id, "Menu Was Generated", reply_markup=keys_2)
#
# @bot.message_handler(commands=['/news1','/news2','/news3','/news4'])
#
# def News(message):
#     urlst = 'https://stopgame.ru'
#     urlig = 'https://www.igromania.ru'
#     if message.text == '/news1':
#         bot.send_message(message.from_user.id, "ВОТ!")
#         i = 0
#         r = requests.get('https://stopgame.ru/news')
#         html = BS(r.content, 'html.parser')
#         for el in html.select('.caption-bold'):
#             if i < 5:
#                 url_more1 = el.select_one('a').get('href')
#                 bot.send_message(message.from_user.id, url_more1)
#             i += 1
#
#     elif message.text == '/news2':
#         bot.send_message(message.from_user.id, "ВОТ!")
#         i = 0
#         r = requests.get('https://www.igromania.ru/news/game/')
#         html = BS(r.content, 'html.parser')
#         for el in html.select('.aubl_item'):
#             if i < 5:
#                 url_more2 = el.select_one('a').get('href')
#                 urlig += url_more2
#                 bot.send_message(message.from_user.id, urlig)
#                 urlig = 'https//www.igromania.ru'
#             i += 1
#
#     elif message.text == '/news3':
#         bot.send_message(message.from_user.id, "ВОТ!")
#         i = 0
#         r = requests.get('https://vqtimes.ru/news/')
#         html = BS(r.content, 'html.parser')
#         for el in html.select('.item-name'):
#             if i < 5:
#                 url_more3 = el.select_one('a').get('href')
#                 urlst += url_more3
#                 bot.send_message(message.from_user.id, urlst)
#                 urlst = 'https//vqtimes.ru'
#             i += 1
#
#     elif message.text == '/news4':
#         bot.send_message(message.from_user.id, "ВОТ!")
#         i = 0
#         r = requests.get('https://ru.wix.com/')
#         html = BS(r.content, 'html.parser')
#         for el in html.select('.post-title'):
#             if i < 5:
#                 url_more4 = el.select_one('a').get('href')
#                 bot.send_message(message.from_user.id, url_more4)
#             i += 1

@bot.message_handler(content_types=['text'])

def text_message(message):
    if message.text == "Привет":
        keys = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keys1 = types.KeyboardButton('Информация')
        keys2 = types.KeyboardButton('Картинки')
        keys3 = types.KeyboardButton('Аудио')
        keys4 = types.KeyboardButton('Комбо')
        keys.add(keys1, keys2, keys3, keys4)
        bot.send_message(message.from_user.id, "Как вам второе меню?", reply_markup=keys)

    elif message.text == "Информация":
        bot.send_message(message.from_user.id, "Привет, выбери что ты хочешь посмотреть и я покажу тебе...")

    elif message.text == "Картинки":
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Щенок 1', callback_data='animals1')
        keyboard.add(key1)
        key2 = types.InlineKeyboardButton(text='Щенок 2', callback_data='animals2')
        keyboard.add(key2)
        key3 = types.InlineKeyboardButton(text='Щенок 3', callback_data='animals3')
        keyboard.add(key3)
        bot.send_message(message.from_user.id, text='Выберите животное', reply_markup=keyboard)

    elif message.text == 'Аудио':
        # a = open('C:\\Users\\Никита\\OneDrive\\Рабочий стол\\Bendy and The inc Machine.mp3', 'rb')
        # bot.send_audio(message.from_user.id,a)
        b = open('C:\\Users\\Никита\\OneDrive\\Рабочий стол\\Cake by the Ocean.mp3', 'rb')
        bot.send_audio(message.from_user.id, b)

    elif message.text == "Новости":
        bot.send_message(message.from_user.id, "Привет!")
        keys_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        k1 = types.KeyboardButton('/news1')
        k2 = types.KeyboardButton('/news2')
        k3 = types.KeyboardButton('/news3')
        keys_2.add(k1,k2,k3)
        bot.send_message(message.from_user.id, "Menu Was Generated", reply_markup=keys_2)


    # @bot.message_handler(commands=['/news1', '/news2', '/news3', '/news4'])
    @bot.message_handler(content_types=['text'])

    def News(message):

        urlst = 'https://www.netangels.ru'
        urlig = 'https://www.igromania.ru'

        if message.text == '/news1':
            bot.send_message(message.from_user.id, "ВОТ!")
            i = 0
            r = requests.get('https://stopgame.ru/news/')
            html = BS(r.content, 'html.parser')
            for el in html.select('.caption-bold'):
                if i < 5:
                    url_more1 = el.select_one('a').get('href')
                    bot.send_message(message.from_user.id, url_more1)
                i += 1

        elif message.text == '/news2':
            bot.send_message(message.from_user.id, "ВОТ!")
            i = 0
            r = requests.get('https://www.igromania.ru/news/game/')
            html = BS(r.content, 'html.parser')
            for el in html.select('.aubl_item'):
                if i < 5:
                    url_more2 = el.select_one('a').get('href')
                    urlig += url_more2
                    bot.send_message(message.from_user.id, urlig)
                    urlig = 'https//www.igromania.ru'
                i += 1

        elif message.text == '/news3':
            bot.send_message(message.from_user.id, "ВОТ!")
            i = 0
            r = requests.get('https://www.netangels.ru/')
            html = BS(r.content, 'html.parser')
            for el in html.select('.item-name'):
                if i < 1:
                    url_more3 = el.select_one('a').get('href')
                    urlst += url_more3
                    bot.send_message(message.from_user.id, urlst)
                    urlst = 'https//www.netangels.ru'
                i += 1

    News(message)

@bot.callback_query_handler(func=lambda call:True)

def callback_worker(call):
    if call.data == 'animals1':
        a = open('C:\\Users\\Никита\\OneDrive\\Рабочий стол\\1.jpg', 'rb')
        bot.send_photo(call.from_user.id, a)
    elif call.data == 'animals2':
        b = open('C:\\Users\\Никита\\OneDrive\\Рабочий стол\\2.jpeg', 'rb')
        bot.send_photo(call.from_user.id, b)
    elif call.data == 'animals3':
        c = open('C:\\Users\\Никита\\OneDrive\\Рабочий стол\\3f.jpg', 'rb')
        bot.send_photo(call.from_user.id, c)

bot.polling(none_stop = True, interval = 0)


