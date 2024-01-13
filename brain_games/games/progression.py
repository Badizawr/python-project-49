from brain_games.const_file import TOTAL_RANGE, STEP, RANDOM_INDEX, MAX_NUM_
from random import randrange


RULE = 'What number is missing in the progression?'


def generate_data(START_NUM = randrange(MAX_NUM_)):
    arithmetic_progression = []
    for i in range(TOTAL_RANGE):
        arithmetic_progression.append(START_NUM + STEP)
        START_NUM += STEP
    corr_answer = str(arithmetic_progression[RANDOM_INDEX])
    arithmetic_progression[RANDOM_INDEX] = '..'

    return f'{" ".join(map(str, arithmetic_progression))}', corr_answer
