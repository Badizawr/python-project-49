from random import choice
from random import randrange


RULE = 'What is the result of the expression?'


def generate_data():
    MAX_NUM = 10
    result = ''
    a, b, exp = randrange(MAX_NUM), randrange(MAX_NUM), choice(['+', '-', '*'])

    match exp:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b

    return f'{a} {exp} {b}', str(result)
