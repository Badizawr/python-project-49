from random import choice
from random import randrange


RULE = 'What is the result of the expression?'


def generate_data():
    range = 10
    result = ''
    a, b, exp = randrange(range), randrange(range), choice(['+', '-', '*'])

    match exp:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b

    return f'{a} {exp} {b}', str(result)
