from math import gcd
from random import randrange


START_RANGE = 1
END_RANGE = 100
RULE = 'Find the greatest common divisor of given numbers.'
START_RANGE = 1
END_RANGE = 100


def generate_data():
    a, b = randrange(START_RANGE, END_RANGE), randrange(START_RANGE, END_RANGE)
    return f'{a} {b}', str(gcd(a, b))
