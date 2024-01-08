from math import gcd
from random import randrange


RULE = 'Find the greatest common divisor of given numbers.'


def generate_data():
    START_RANGE = 1
    END_RANGE = 100
    a, b = randrange(START_RANGE, END_RANGE), randrange(START_RANGE, END_RANGE)
    return f'{a} {b}', str(gcd(a, b))
