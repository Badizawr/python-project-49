from random import randint


def brain_progression():
    print('What number is missing in the progression?')
    count = 0
    while count < 3:
        start, step = randint(1, 50), randint(1, 10)
        progression = [start + i * step for i in range(10)]
        hidden_index: int = randint(1, len(progression) - 2)
        hidden_number = progression[hidden_index]
        progression[hidden_index] = '..'
        print(' '.join(map(str, progression)))
        answer = input('Your answer: ')
        if answer == str(hidden_number):
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{hidden_number}'.")
            break
    else:
        print('Congratulations, you won!')



