import unittest
from main import methodsForBot


class Test(unittest.TestCase):
  def setUp(self):
    self.methods = methodsForBot()
  def test_add(self):
    self.assertEqual(self.methods.cooking_method(), "Сегодня можно потушить")


