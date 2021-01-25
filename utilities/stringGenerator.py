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


    """ Параметризованный метод. Менее информативен, но в тесте выглядит красивее """
    @staticmethod
    def random_string(size=8, whitespaces=0, letters=False, digits=False, punctuation=False):
        if letters and digits and punctuation:
            symbols = string.ascii_lowercase + string.digits + string.punctuation + ' ' * whitespaces
            return ''.join(random.choice(symbols) for _ in range(size))
        elif letters and digits:
            symbols = string.ascii_lowercase + string.digits + ' ' * whitespaces
            return ''.join(random.choice(symbols) for _ in range(size))
        elif letters and punctuation:
            symbols = string.ascii_lowercase + string.punctuation + ' ' * whitespaces
            return ''.join(random.choice(symbols) for _ in range(size))
        elif digits:
            symbols = string.digits + ' ' * whitespaces
            return ''.join(random.choice(symbols) for _ in range(size))
        elif letters:
            symbols = string.ascii_lowercase + ' ' * whitespaces
            return ''.join(random.choice(symbols) for _ in range(size))