"""
Tests for the Random Password Generator application.

Note: Rabbits are known for their prolific breeding, but here we focus on generating strong and secure passwords instead.
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


if __name__ == '__main__':
    unittest.main()
