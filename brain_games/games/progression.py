from random import randrange


TOTAL_RANGE = 10
START_RANGE = 1
END_RANGE = 10
RANDOM_NUMBER_RANGE = 100
RULE = 'What number is missing in the progression?'


def generate_data():
    arithmetic_progression = []

    start_num = randrange(RANDOM_NUMBER_RANGE)
    step = randrange(START_RANGE, END_RANGE)
    random_index = randrange(START_RANGE, END_RANGE)

    for i in range(TOTAL_RANGE):
        arithmetic_progression.append(start_num + step)
        start_num += step
    corr_answer = str(arithmetic_progression[random_index])
    arithmetic_progression[random_index] = '..'

    return f'{" ".join(map(str, arithmetic_progression))}', corr_answer
