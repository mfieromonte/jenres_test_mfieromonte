import unittest
import random_user_api


class TestRandomUserAPI(unittest.TestCase):

    def test_get_random_user(self):
        # Test fetching a single random user
        result = random_user_api.get_random_user()
        self.assertIn('results', result)
        self.assertEqual(len(result['results']), 1)

    def test_get_multiple_users(self):
        # Test fetching multiple random users
        result = random_user_api.get_random_user(results=5)
        self.assertIn('results', result)
        self.assertEqual(len(result['results']), 5)

    def test_get_user_with_gender(self):
        # Test fetching a user with a specific gender
        result = random_user_api.get_random_user(gender='female')
        self.assertIn('results', result)
        self.assertEqual(result['results'][0]['gender'], 'female')


if __name__ == '__main__':
    unittest.main()
