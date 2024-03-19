import unittest
from password_gen import generate_password
import string

class TestPasswordGenerator(unittest.TestCase):

    def test_length(self):
        password = generate_password(length=10)
        self.assertEqual(len(password), 10)

    def test_no_digits(self):
        password = generate_password(use_digits=False)
        self.assertFalse(any(char.isdigit() for char in password))

    def test_no_special_chars(self):
        password = generate_password(use_special_chars=False)
        self.assertFalse(any(char in string.punctuation for char in password))

if __name__ == '__main__':
    unittest.main()
