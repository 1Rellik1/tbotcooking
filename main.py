from random import random, randint
import telebot
class methodsForBot:
    def meat(self):
        x = randint(1, 5)
        if x == 1:
            return "Приготовь сегодня курицу"
        elif x == 2:
            return "Приготовь сегодня свинину"
        elif x == 3:
            return "Приготовь сегодня говядину"
        elif x == 4:
            return "Приготовь сегодня индейку"
        elif x == 5:
            return "Приготовь сегодня кролика"

    def cooking_method(self):
        x = randint(1, 5)
        return "Сегодня можно потушить"
        # if x == 1:
        #     return"Сегодня можно запечь"
        # elif x == 2:
        #     return"Сегодня можно зажарить"
        # elif x == 3:
        #     return"Сегодня можно сварить"
        # elif x == 4:
        #     return"Сегодня можно потушить"
        # elif x == 5:
        #     return"Сегодня можно приготовить на пару"

    def garnish(self):
        x = randint(1, 5)
        if x == 1:
            return "Сегодня можно приготовить макароны на гарнир"
        elif x == 2:
            return "Сегодня можно приготовить гречку на гарнир"
        elif x == 3:
            return "Сегодня можно приготовить рис на гарнир"
        elif x == 4:
            return "Сегодня можно приготовить булгур на гарнир"
        elif x == 5:
            return "Сегодня можно приготовить птитим на гарнир"


token = '1958566717:AAETD70Kg3akYv7TZ_Kwgr18FYw6papWLZI'
bot =telebot.TeleBot(token)
choosing= methodsForBot()
def menu():
    markup = telebot.types.InlineKeyboardMarkup()
    buttonA = telebot.types.InlineKeyboardButton('Основное блюдо', callback_data='meat')
    buttonB = telebot.types.InlineKeyboardButton('Гарнир', callback_data='garnish')
    buttonC = telebot.types.InlineKeyboardButton('Способ приготовления', callback_data='cooking_method')
    markup.row(buttonA, buttonB)
    markup.row(buttonC)
    return markup

@bot.message_handler(commands=['start'])
def on_start(message):
    bot.send_message(message.chat.id,"Привет, я бот, который поможет тебе решить, что сегодня приготовить",reply_markup=menu())



@bot.callback_query_handler(lambda meat_handler: meat_handler.data == "meat")
def meat_massage(call):
    bot.send_message(call.message.chat.id, choosing.meat(),reply_markup=menu())


@bot.callback_query_handler(lambda meat_handler: meat_handler.data == "garnish")
def garnish_massage(call):
    bot.send_message(call.message.chat.id,choosing.garnish(),reply_markup=menu())

@bot.callback_query_handler(lambda meat_handler: meat_handler.data == "cooking_method")
def cooking_method_massage(call):
    bot.send_message(call.message.chat.id,choosing.cooking_method(),reply_markup=menu())



bot.polling()

