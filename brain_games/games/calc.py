from random import choice, randrange


RANGE = 10
RULE = 'What is the result of the expression?'


def generate_data():
    result = ''
    a, b, exp = randrange(RANGE), randrange(RANGE), choice(['+', '-', '*'])

    match exp:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b

    return f'{a} {exp} {b}', str(result)
