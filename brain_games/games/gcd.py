from math import gcd
from random import randrange


RULE = 'Find the greatest common divisor of given numbers.'


def generate_data():
    start_range = 1
    end_range = 100
    a, b = randrange(start_range, end_range), randrange(start_range, end_range)
    return f'{a} {b}', str(gcd(a, b))
