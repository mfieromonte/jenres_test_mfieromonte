import unittest
import calculations

class TestCalculations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculations.add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(calculations.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calculations.multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(calculations.divide(8, 2), 4)
        with self.assertRaises(ValueError):
            calculations.divide(8, 0)

    def test_divide_by_one(self):
        self.assertEqual(calculations.divide_by_one(8, 0), 8)

    def test_divide_by_two(self):
        self.assertEqual(calculations.divide_by_two(8, 0), 4)

if __name__ == '__main__':
    unittest.main()
