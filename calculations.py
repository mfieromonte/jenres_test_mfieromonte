import logging

logger = logging.getLogger(__name__)


def add(a, b):
    logger.debug(f'Adding {a} and {b}')
    return a + b


def subtract(a, b):
    logger.debug(f'Subtracting {b} from {a}')
    return a - b


def multiply(a, b):
    logger.debug(f'Multiplying {a} and {b}')
    return a * b


def divide(a, b):
    logger.debug(f'Dividing {a} by {b}')
    if b == 0:
        logger.error("Cannot divide by zero.")
        raise ValueError("Cannot divide by zero.")
    return a / b
