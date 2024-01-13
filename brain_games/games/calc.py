
from random import choice
from random import randrange

RULE


def generate_data():

    result = ''
    a, b, exp = randrange(END_RANGE), randrange(END_RANGE), choice(['+', '-', '*'])

    match exp:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b

    return f'{a} {exp} {b}', str(result)
