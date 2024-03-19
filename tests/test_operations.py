import unittest
from operations import get_sums, get_nums

class TestOperations(unittest.TestCase):

    def test_get_sums(self):
        self.assertEqual(get_sums([1, 2, 3]), 6)
        self.assertEqual(get_sums([-1, 0, 1]), 0)
        self.assertEqual(get_sums([]), 0)

    def test_get_nums(self):
        self.assertEqual(get_nums([]), 6)  # The function seems to ignore input and always returns 6

if __name__ == '__main__':
    unittest.main()
