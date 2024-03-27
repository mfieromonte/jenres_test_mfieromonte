import logging

logger = logging.getLogger(__name__)


def add(a, b):
    logger.debug(f"Adding {a} + {b}")
    return a + b


def subtract(a, b):
    logger.debug(f"Subtracting {a} - {b}")
    return a - b


def multiply(a, b):
    logger.debug(f"Multiplying {a} * {b}")
    return a * b


def divide(a, b):
    logger.debug(f"Dividing {a} / {b}")
    if b == 0:
        logger.error("Cannot divide by zero.")
        raise ValueError("Cannot divide by zero.")
    return a / b
