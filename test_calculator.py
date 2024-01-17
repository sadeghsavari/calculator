# test_calculator.py
import unittest
from calculator import add, subtract, multiply, divide, calculate

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_calculate(self):
        self.assertEqual(calculate("2 + 3"), 5)
        self.assertEqual(calculate("4 * 5"), 20)
        self.assertEqual(calculate("7 / 2"), 3.5)
        self.assertEqual(calculate("1 / 0"), "division by zero")
        self.assertEqual(calculate("invalid_expression"), "invalid syntax")

if __name__ == "__main__":
    unittest.main()
