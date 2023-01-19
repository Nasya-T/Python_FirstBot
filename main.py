import telebot
import sqlite3
from datetime import datetime
from telebot import types
bot = telebot.TeleBot('5855979787:AAFY-hh1-Nr1uEztR639Xf20mepoiT7c0bw')

#----------------------------  START  --------------------------------------
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🎉 Текущее событие')
    item2 = types.KeyboardButton('⚔ Данжи')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id, '——————————————————————\n                                   🔸Paimon_bot🔸\n——————————————————————\n \nПривет! Я твой бот - помощник. \n| Могу  рассказать про текущие события  \n| в Тейвате, какие данжи сегодня открыты,\n| и просто весело провести с тобой время!\n——————————————————————'.format(message.from_user), reply_markup=markup)

#-----------------------------  SQL  ----------------------------------------
# Я добавила базу данных и она работа, но из-за того, что она начала конфликтовать с другими кусками кода, пришлось его депортиорвать :(

#----------------------------  MAIN  ---------------------------------------
@bot.message_handler(content_types=['text'])
def get_message(message):

    if message.text == '🎉 Текущее событие':
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_ban = types.InlineKeyboardButton(text='🔸 Баннеры', callback_data='Ban')
        keyboard.add(key_ban)  # добавляем кнопку в клавиатуру
        key_event = types.InlineKeyboardButton(text='🔸 Ивенты', callback_data='Event')
        keyboard.add(key_event) # добавляем кнопку в клавиатуру
        question = 'Выбери что тебе нужно'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
        bot.send_message(message.from_user.id, '-----------------------------------')

    if message.text == '⚔ Данжи':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('🔸 Сегодня')
        item2 = types.KeyboardButton('🔸 Завтра')
        item3 = types.KeyboardButton('⬅ Назад')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, '⚔ Данжи', reply_markup=markup)

    if message.text == '⬅ Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('🎉 Текущее событие')
        item2 = types.KeyboardButton('⚔ Данжи')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, '⬅ Назад', reply_markup=markup)

    if message.text == '🔸 Сегодня':
        now = datetime.now()
        day_now = datetime.isoweekday(now)
        if day_now == 1 or day_now == 4:
            bot.send_photo(message.from_user.id,open('img\image_1_4.png', "rb"))
            bot.send_message(message.from_user.id, '-----------------------------------')
        if day_now == 2 or day_now == 5:
            bot.send_photo(message.from_user.id,open('img\image_2_5.png', "rb"))
            bot.send_message(message.from_user.id, '-----------------------------------')
        if day_now == 3 or day_now == 6:
            bot.send_photo(message.from_user.id, open('img\image_3_6.png', "rb"))
            bot.send_message(message.from_user.id, '-----------------------------------')
        if day_now == 7:
            bot.send_message(message.chat.id, '---- Сегодня доступны все данжи ✨ ----')
    if message.text == '🔸 Завтра':
        now = datetime.now()
        day_now = datetime.isoweekday(now) + 1
        if day_now == 1 or day_now == 4:
            bot.send_photo(message.from_user.id,open('img\image_1_4.png', "rb"))
            bot.send_message(message.from_user.id, '-----------------------------------')
        if day_now == 2 or day_now == 5:
            bot.send_photo(message.from_user.id,open('img\image_2_5.png', "rb"))
            bot.send_message(message.from_user.id, '-----------------------------------')
        if day_now == 3 or day_now == 6:
            bot.send_photo(message.from_user.id, open('img\image_3_6.png', "rb"))
            bot.send_message(message.from_user.id, '-----------------------------------')
        if day_now == 7:
            bot.send_message(message.chat.id, '---- Сегодня доступны все данжи ✨ ----')

#----------------------------  DEF  ---------------------------------------
# Кнопки в чате для банеров
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Ban":
        bot.send_photo(call.message.chat.id, open('img\Banner_1.jpg', "rb"))
        bot.send_message(call.message.chat.id, '-----------------------------------')
    elif call.data == "Event":
        bot.send_photo(call.message.chat.id, open('img\event.jpg', "rb"))
        bot.send_message(call.message.chat.id, 'Главный праздник текущей версии — Морские Фонари.\nБудет паркур, катеры и многое другое. Так же по окончанию можно будет выбрать любого персонажа из Ли Юэ по выбору ✨')
        bot.send_message(call.message.chat.id, '-----------------------------------')

#----------------------------  ---  ---------------------------------------

bot.polling(none_stop=True, interval=0)