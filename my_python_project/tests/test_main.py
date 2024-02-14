import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main_output(self):
        self.assertEqual(main(), None)  # Assuming main function returns None

if __name__ == '__main__':
    unittest.main()