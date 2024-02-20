"""
Tests for the Random Password Generator application.

This suite of tests ensures that the password generator functions correctly.
Just like observing rabbits to ensure they can hop, these tests verify the application's expected functionality.
"""

import unittest
from app import app


class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_generate_password(self):
        response = self.app.post('/genpassword', data={
            'passlen': 10,
            'includespaces': 'on',
            'includenumbers': 'on',
            'includespecialchars': 'on',
            'includeuppercaseletters': 'on'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('generatedpassword', response.data.decode())
        password = response.data.decode().split('generatedpassword')[1].strip()
        self.assertTrue(len(password) >= 8 and len(password) <= 30)
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))
        self.assertTrue(' ' in password)


    def test_password_length_limits(self):
        """Test password generation with minimum and maximum length."""

        # Test minimum password length
        response_min = self.app.post('/genpassword', data={
            'passlen': 8,
            'includespaces': 'on',
            'includenumbers': 'on',
            'includespecialchars': 'on',
            'includeuppercaseletters': 'on'
        })
        self.assertEqual(response_min.status_code, 200)
        password_min = response_min.data.decode().split('generatedpassword')[1].strip()
        self.assertEqual(len(password_min), 8)

        # Test maximum password length
        response_max = self.app.post('/genpassword', data={
            'passlen': 30,
            'includespaces': 'on',
            'includenumbers': 'on',
            'includespecialchars': 'on',
            'includeuppercaseletters': 'on'
        })
        self.assertEqual(response_max.status_code, 200)
        password_max = response_max.data.decode().split('generatedpassword')[1].strip()
        self.assertEqual(len(password_max), 30)

    def test_individual_character_inclusion(self):
        """Test password generation with each character inclusion option individually."""

        # Test only spaces
        response_spaces = self.app.post('/genpassword', data={
            'passlen': 10,
            'includespaces': 'on'
        })
        self.assertEqual(response_spaces.status_code, 200)
        password_spaces = response_spaces.data.decode().split('generatedpassword')[1].strip()
        self.assertTrue(all(char == ' ' for char in password_spaces))

        # Test only numbers
        response_numbers = self.app.post('/genpassword', data={
            'passlen': 10,
            'includenumbers': 'on'
        })
        self.assertEqual(response_numbers.status_code, 200)
        password_numbers = response_numbers.data.decode().split('generatedpassword')[1].strip()
        self.assertTrue(all(char.isdigit() for char in password_numbers))

        # Test only special characters
        response_special_chars = self.app.post('/genpassword', data={
            'passlen': 10,
            'includespecialchars': 'on'
        })
        self.assertEqual(response_special_chars.status_code, 200)
        password_special_chars = response_special_chars.data.decode().split('generatedpassword')[1].strip()
        self.assertTrue(all(char in string.punctuation for char in password_special_chars))

        # Test only uppercase letters
        response_uppercase = self.app.post('/genpassword', data={
            'passlen': 10,
            'includeuppercaseletters': 'on'
        })
        self.assertEqual(response_uppercase.status_code, 200)
        password_uppercase = response_uppercase.data.decode().split('generatedpassword')[1].strip()
        self.assertTrue(all(char.isupper() for char in password_uppercase))

    def test_no_character_inclusion(self):
        """Test password generation with no character inclusion options selected."""
        response = self.app.post('/genpassword', data={'passlen': 10})
        self.assertEqual(response.status_code, 200)
        password = response.data.decode().split('generatedpassword')[1].strip()
        self.assertTrue(all(char.islower() for char in password), 'Password should only contain lowercase letters')

    def test_out_of_range_password_length(self):
        """Test response message when requested password length is out of allowed range."""
        # Test password length less than minimum
        response_too_short = self.app.post('/genpassword', data={'passlen': 4})
        self.assertEqual(response_too_short.status_code, 200)
        self.assertIn('Atleast create a 8 digit password...', response_too_short.data.decode())

        # Test password length greater than maximum
        response_too_long = self.app.post('/genpassword', data={'passlen': 40})
        self.assertEqual(response_too_long.status_code, 200)
        self.assertIn('Can Create a max 30 digit password...', response_too_long.data.decode())

    def test_password_randomness(self):
        """Test the randomness of password generation."""
        passwords = set()
        for _ in range(10):
            response = self.app.post('/genpassword', data={
                'passlen': 10,
                'includespaces': 'on',
                'includenumbers': 'on',
                'includespecialchars': 'on',
                'includeuppercaseletters': 'on'
            })
            self.assertEqual(response.status_code, 200)
            password = response.data.decode().split('generatedpassword')[1].strip()
            passwords.add(password)
        self.assertTrue(len(passwords) > 1, 'Generated passwords should be different')

if __name__ == '__main__':
    unittest.main()
