import unittest
import random
import datetime
from simple_calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(random.randint(-1000, 1000))

    @classmethod
    def setUpClass(cls):
        print("Start:", datetime.datetime.today().strftime("%H:%M:%S.%f"))

    @classmethod
    def tearDownClass(cls):
        print("Stop: ", datetime.datetime.today().strftime("%H:%M:%S.%f"))

    def test_add(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(1, 2, 3).value, calc_value + 6)

    def test_multiply(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.multiply(5, 2, 90).value, calc_value * 900)

    def test_divide(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.divide(2, 3).value, calc_value / 6)

    def test_subtract(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.subtract(100, 5).value, calc_value - 105)

    def test_power(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(4).value, calc_value ** 4)

    def test_root(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(2).value, calc_value ** (1/2))


if __name__ == '__main__':
    unittest.main()
