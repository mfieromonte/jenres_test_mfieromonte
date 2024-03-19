import string
import random

def generate_password(length=8, use_digits=True, use_special_chars=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password
