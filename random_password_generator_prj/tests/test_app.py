import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_genpassword_status_code(self):
        response = self.app.post('/genpassword', data={'passlen': '10'})
        self.assertEqual(response.status_code, 200)

    def test_genpassword_min_length(self):
        response = self.app.post('/genpassword', data={'passlen': '5'})
        self.assertIn('Atleast create a 8 digit password...', response.data.decode())

    def test_genpassword_max_length(self):
        response = self.app.post('/genpassword', data={'passlen': '35'})
        self.assertIn('Can Create a max 30 digit password...', response.data.decode())

if __name__ == '__main__':
    unittest.main()
