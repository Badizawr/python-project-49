from random import randrange


TOTAL_RANGE = 10
START_RANGE = 1
END_RANGE = 100
RULE = 'What number is missing in the progression?'
TOTAL_RANGE = 10
END_RANGE = 100
STEP = randrange(1, 10)
RANDOM_INDEX = randrange(1, 10)


def generate_data():
    arithmetic_progression = []
    start_num = randrange(END_RANGE)  # Start number of arithmetic progression
    step = randrange(START_RANGE, TOTAL_RANGE)
    for i in range(TOTAL_RANGE):
        arithmetic_progression.append(start_num + step)
        start_num += step
    corr_answer = str(arithmetic_progression[randrange(START_RANGE, TOTAL_RANGE)])
    arithmetic_progression[randrange(START_RANGE, TOTAL_RANGE)] = '..'

    return f'{" ".join(map(str, arithmetic_progression))}', corr_answer
