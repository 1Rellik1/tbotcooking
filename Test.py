import Bot
import unittest
import telebot

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.methods = Bot.methodsForBot()

    def test_meat(self):
        variants = ["Приготовь сегодня курицу", "Приготовь сегодня свинину", "Приготовь сегодня говядину",
                    "Приготовь сегодня индейку", "Приготовь сегодня кролика"]
        x = False
        ourmeat = self.methods.meat()
        for i in variants:
            if ourmeat == i:
                x = True
        self.assertEqual(True, x)

    def test_cooking_methods(self):
        variants = ["Сегодня можно запечь", "Сегодня можно зажарить", "Сегодня можно сварить",
                    "Сегодня можно потушить", "Сегодня можно приготовить на пару"]
        x = False
        our_cooking_method = self.methods.cooking_method()
        for i in variants:
            if  our_cooking_method == i:
                x = True
        self.assertEqual(True, x)

    def test_garnish(self):
        variants = ["Сегодня можно приготовить макароны на гарнир", "Сегодня можно приготовить гречку на гарнир", "Сегодня можно приготовить рис на гарнир",
                    "Сегодня можно приготовить булгур на гарнир", "Сегодня можно приготовить птитим на гарнир"]
        x = False
        our_garnish = self.methods.garnish()
        for i in variants:
            if our_garnish == i:
                x = True
        self.assertEqual(True, x)

    def test_menu(self):
        markup = telebot.types.InlineKeyboardMarkup()
        buttonA = telebot.types.InlineKeyboardButton('Основное блюдо', callback_data='meat')
        buttonB = telebot.types.InlineKeyboardButton('Гарнир', callback_data='garnish')
        buttonC = telebot.types.InlineKeyboardButton('Способ приготовления', callback_data='cooking_method')
        markup.row(buttonA, buttonB)
        markup.row(buttonC)
        self.assertEqual(markup.to_dict(), self.methods.menu().to_dict())


if __name__ == '__main__':
    unittest.main()
