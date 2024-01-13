from random import randrange


END_RANGE = 100
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_data():
    rand_num = randrange(END_RANGE)
    is_even_str = 'yes' if is_even(rand_num) else 'no'
    return f'{rand_num}', is_even_str
