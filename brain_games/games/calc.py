from random import choice
from random import randrange


RULE = 'What is the result of the expression?'


def generate_data():
    band = 10
    result = ''
    a, b, exp = randrange(band), randrange(band), choice(['+', '-', '*'])

    match exp:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b

    return f'{a} {exp} {b}', str(result)
