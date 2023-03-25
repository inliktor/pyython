import telebot
from telebot import *
from telebot import types
token='5567467526:AAHZViw5XZUrrlzau1QsYpm5bq_sLR4Up7o'
bot=telebot.TeleBot(token)
try:
    def authL():
        Logins=input()
        return(Logins)
    def authP():
        Passwords=input()
        return(Passwords)

    #||||||||||||||||| ||||||||||||||||||| ||||||||||||||||||| ||||||||||||||| |||||||||||||||| 

    #Хелп по комманд для комрадов 
        @bot.message_handler(commands=['button'])
        def button_message(message):
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("Дневник")
            markup.add(item1)																								
            bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
# если что сносить 
    #Перехват сообщения ака ответ на него или же комманда для ботика ✌️
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id,"Привет ✌️ ")

    #кнопка тип клава тг чтоб ваши пальчики не ебались с комманд
    @bot.message_handler(commands=['button'])
    def button_message(message):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Дневник")
        markup.add(item1)																								
        bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
    #Дневничок, Эта лупа залупа делает парсинг и жестко трахает мне мозги 
    @bot.message_handler(content_types='text')
    def message_reply(message):
        from dnevnikselenium import score,raspiss1,raspiss2,raspiss,raspiss3,raspiss4,raspiss5,Login,Password
        if message.text=="Дневник":
            bot.send_message(message.chat.id,authL)
            bot.send_message(message.chat.id,authP)
            bot.send_message(message.chat.id, score)
            bot.send_message(message.chat.id, raspiss)
            bot.send_message(message.chat.id, raspiss1)
            bot.send_message(message.chat.id, raspiss2)
            bot.send_message(message.chat.id, raspiss3)
            bot.send_message(message.chat.id, raspiss4)
            bot.send_message(message.chat.id, raspiss5)
    bot.infinity_polling()
    
except: 
    pass