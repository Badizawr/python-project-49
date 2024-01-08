from random import randrange


RULE = 'What number is missing in the progression?'


def generate_data():
    arithmetic_progression = []
    TOTAL_RANGE = 10
    START_NUM = randrange(100)  # Start number of arithmetic progression
    STEP = randrange(1, 10)  # Step of progression
    RANDOM_INDEX = randrange(1, 10)  # Random num to hide the field progression

    for i in range(TOTAL_RANGE):
        arithmetic_progression.append(START_NUM + STEP)
        START_NUM += STEP
    corr_answer = str(arithmetic_progression[RANDOM_INDEX])
    arithmetic_progression[RANDOM_INDEX] = '..'

    return f'{" ".join(map(str, arithmetic_progression))}', corr_answer
