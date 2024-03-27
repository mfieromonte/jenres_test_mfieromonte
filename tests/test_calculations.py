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

    # Additional tests can be added here if new functions are implemented in calculations.py

if __name__ == '__main__':
    unittest.main()
