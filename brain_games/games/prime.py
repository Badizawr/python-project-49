from random import randrange


RANGE = 100
ROOT_MATHEMATICS = 0.5
RULE_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** ROOT_MATHEMATICS) + 1):
        if number % i == 0:
            return False
    return True


def generate_data():
    rand_num = randrange(RANGE)
    return f'{rand_num}', 'yes' if is_prime(rand_num) else 'no'
