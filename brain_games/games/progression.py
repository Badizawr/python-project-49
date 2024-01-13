from random import randrange


RULE = 'What number is missing in the progression?'
TOTAL_RANGE = 10
END_RANGE = 100
STEP = randrange(1, 10)
RANDOM_INDEX = randrange(1, 10)


def generate_data():
    arithmetic_progression = []
    start_num = randrange(END_RANGE)
    for i in range(TOTAL_RANGE):
        arithmetic_progression.append(START_NUM + STEP)
        START_NUM += STEP
    corr_answer = str(arithmetic_progression[RANDOM_INDEX])
    arithmetic_progression[RANDOM_INDEX] = '..'

    return f'{" ".join(map(str, arithmetic_progression))}', corr_answer
