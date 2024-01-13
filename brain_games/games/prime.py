from random import randrange

MAX_NUM = 100

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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
