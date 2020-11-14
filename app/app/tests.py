from django.test import TestCase

from app.calc import add, subtract

class CalcTests(TestCase):

    def test_add_numbers(self):
        self.assertEqual(add(2,6),8)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(4,2),2)
