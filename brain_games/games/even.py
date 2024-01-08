from random import randrange


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_data():
    MAX_NUM = 100
    rand_num = randrange(MAX_NUM)
    is_even_str = 'yes' if is_even(rand_num) else 'no'
    return f'{rand_num}', is_even_str
