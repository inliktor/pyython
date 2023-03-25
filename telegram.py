import telebot
from telebot import *
from telebot import types
token='5567467526:AAHZViw5XZUrrlzau1QsYpm5bq_sLR4Up7o'
bot=telebot.TeleBot(token)

try:
    #Временно не доступно
        def authL():
            Logins=input()
            return(Logins)
        def authP():
            Passwords=input()
            return(Passwords)
    #Временно не доступно

    #||||||||||||||||| ||||||||||||||||||| ||||||||||||||||||| ||||||||||||||| |||||||||||||||| 

    #Хелп по комманд для комрадов 

  #Перехват сообщения ака ответ на него или же комманда для ботика ✌️
        @bot.message_handler(commands=['start'])
        def start_message(message):
            bot.send_message(message.chat.id,"Привет ✌️ ")

        @bot.message_handler(commands=['help'])
        def Help_message(message):
            bot.send_message(message.chat.id,"Доступные комманды на данный момент: Start,Help,button,Дневник.(Писать через /)при вводе /button у вас будет выбор функций")

        @bot.message_handler(commands=['future'])
        def future_message(message):
            bot.send_message(message.chat.id,"Будущие бота туманно, если есть идеи по развитию бота прошу в лс @inliktor")

    #кнопка тип клава тг чтоб ваши пальчики комманд
        @bot.message_handler(commands=['button'])
        def button_message(message):
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("Дневник")
            item2=types.KeyboardButton("/start")
            item3=types.KeyboardButton('/help')            
            markup.add(item1,item2,item3)																								
            bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
        @bot.message_handler(content_types='text')
        def message_Dnevnik(message):           
            from dnevnikselenium import score,raspiss1,raspiss2,raspiss,raspiss3,raspiss4,raspiss5
            if message.text=="Дневник":
                bot.send_message(message.chat.id, raspiss)
                bot.send_message(message.chat.id, raspiss1)
                bot.send_message(message.chat.id, raspiss2)
                bot.send_message(message.chat.id, raspiss3)
                bot.send_message(message.chat.id, raspiss4)
                bot.send_message(message.chat.id, raspiss5)             
    #Дневничок, Эта лупа залупа делает парсинг
        @bot.message_handler(content_types='text')
        def message_reply(message):
            if message.text == "/start":
                bot.send_message(message.chat.id,start_message)
            if message.text == "/button":
                bot.send_message(message.chat.id,button_message)
            if message.text == "/help":
                bot.send_message(message.chat.id,Help_message)           
            #Вот эта штучка делает магию 
        bot.infinity_polling()

    
except: 
    pass

