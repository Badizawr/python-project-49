from brain_games.const_file import MAX_NUM, RULE_PRIME
from random import randrange


RULE_PRIME


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_data():
    rand_num = randrange(MAX_NUM)
    return f'{rand_num}', 'yes' if is_prime(rand_num) else 'no'
