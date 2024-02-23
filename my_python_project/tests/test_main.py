import unittest
import logging
from unittest.mock import patch
from demo_housekeeping import hello_world, hello_mars


class TestLogging(unittest.TestCase):
    @patch('demo_housekeeping.logger')
    def test_hello_world_logging(self, mock_logger):
        hello_world()
        mock_logger.info.assert_called_with("Executing hello_world function")
        mock_logger.debug.assert_called_with("Unused variable set to 13")

    @patch('demo_housekeeping.logger')
    def test_hello_mars_logging(self, mock_logger):
        hello_mars()
        mock_logger.info.assert_called_with("Executing hello_mars function")


if __name__ == '__main__':
    unittest.main()
