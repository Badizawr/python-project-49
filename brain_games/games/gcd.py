from brain_games.const_file import START_RANGE, END_RANGE 
from math import gcd
from random import randrange


RULE = 'Find the greatest common divisor of given numbers.'


def generate_data():
    a, b = randrange(START_RANGE, END_RANGE), randrange(START_RANGE, END_RANGE)
    return f'{a} {b}', str(gcd(a, b))
