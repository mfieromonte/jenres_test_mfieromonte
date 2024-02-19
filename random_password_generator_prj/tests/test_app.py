import unittest
from app import app


class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Random Password Generator', response.data.decode())

    def test_password_generation(self):
        response = self.app.post('/genpassword', data={
            'passlen': 10,
            'includespaces': 'on',
            'includenumbers': 'on',
            'includespecialchars': 'on',
            'includeuppercaseletters': 'on'
        })
        self.assertEqual(response.status_code, 200)
        password = response.data.decode()
        self.assertTrue(any(char.islower() for char in password), 'Password must contain a lowercase letter.')
        self.assertTrue(any(char.isupper() for char in password), 'Password must contain an uppercase letter.')
        self.assertTrue(any(char.isdigit() for char in password), 'Password must contain a digit.')
        self.assertTrue(any(char in string.punctuation for char in password), 'Password must contain a special character.')
        self.assertTrue(' ' in password, 'Password must contain a space.')
        self.assertEqual(len(password), 10, 'Password must be 10 characters long.')


if __name__ == '__main__':
    unittest.main()