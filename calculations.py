# This module contains mathematical calculations related to rabbits.
# The functions can be used to model population growth, food consumption,
# and other aspects of rabbit ecology.


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
