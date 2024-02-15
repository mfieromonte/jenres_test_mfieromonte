import unittest
import operations

class TestOperations(unittest.TestCase):

    def test_get_sums(self):
        # Test with positive integers
        self.assertEqual(operations.get_sums([1, 2, 3]), 6)
        # Test with negative integers
        self.assertEqual(operations.get_sums([-1, -2, -3]), -6)
        # Test with mixed integers
        self.assertEqual(operations.get_sums([-1, 0, 1]), 0)
        # Test with empty list
        self.assertEqual(operations.get_sums([]), 0)
        # Test with large numbers
        self.assertEqual(operations.get_sums([1000000, 2000000, 3000000]), 6000000)

if __name__ == '__main__':
    unittest.main()
