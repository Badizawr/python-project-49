from random import randrange


TOTAL_RANGE = 10
STEP = randrange(1, 10)  # Step of progression
RANDOM_INDEX = randrange(1, 10)  # Random num to hide the field progression
END_RANGE = 100
RULE = 'What number is missing in the progression?'


def generate_data():
    arithmetic_progression = []
    start_num = randrange(END_RANGE)  # Start number of arithmetic progression
    for i in range(TOTAL_RANGE):
        arithmetic_progression.append(start_num + STEP)
        start_num += STEP
    corr_answer = str(arithmetic_progression[RANDOM_INDEX])
    arithmetic_progression[RANDOM_INDEX] = '..'

    return f'{" ".join(map(str, arithmetic_progression))}', corr_answer
