from brain_games.const_file import MAX_NUM_, RULE
from random import choice
from random import randrange

RULE


def generate_data():

    result = ''
    a, b, exp = randrange(MAX_NUM_), randrange(MAX_NUM_), choice(['+', '-', '*'])

    match exp:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b

    return f'{a} {exp} {b}', str(result)
