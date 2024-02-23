import logging
from demo import hello_world, hello_mars
from unittest.mock import patch
import unittest


class TestLogging(unittest.TestCase):

    @patch('demo.logger')
    def test_hello_world_logs_info(self, mock_logger):
        hello_world()
        mock_logger.info.assert_called_with("Hello World function is called")

    @patch('demo.logger')
    def test_hello_mars_logs_info(self, mock_logger):
        hello_mars()
        mock_logger.info.assert_called_with("Hello Mars function is called")


if __name__ == '__main__':
    unittest.main()
