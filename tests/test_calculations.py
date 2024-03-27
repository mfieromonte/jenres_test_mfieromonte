import unittest
from calculations import add, subtract, multiply, divide, divide_by_0

class TestCalculations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        with self.assertRaises(ValueError):
            divide(8, 0)

    def test_divide_by_0(self):
        self.assertEqual(divide_by_0(8, 0), 8)


if __name__ == '__main__':
    unittest.main()
