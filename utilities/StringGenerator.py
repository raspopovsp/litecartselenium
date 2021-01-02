import random
import string


class StringGenerator:

    @staticmethod
    def string_generator(size=8, whitespaces=0):
        symbols = string.ascii_lowercase + ' ' * whitespaces
        return ''.join(random.choice(symbols) for _ in range(size))

    @staticmethod
    def digits_generator(size=8, whitespaces=0):
        symbols = string.digits + ' ' * whitespaces
        return ''.join(random.choice(symbols) for _ in range(size))

    @staticmethod
    def string_with_digits_generator(size=8, whitespaces=0):
        symbols = string.ascii_lowercase + string.digits + ' ' * whitespaces
        return ''.join(random.choice(symbols) for _ in range(size))

    @staticmethod
    def string_with_digits_and_punctuation_generator(size=8, whitespaces=0):
        symbols = string.ascii_lowercase + string.digits + string.punctuation + ' ' * whitespaces
        return ''.join(random.choice(symbols) for _ in range(size))

