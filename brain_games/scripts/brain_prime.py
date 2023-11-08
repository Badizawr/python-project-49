from random import randint


def brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = randint(1, 100)
        print(number)
        answer = input('Your answer: ')
        if (answer == 'yes' and number % 2 == 0) or (answer == 'no' and number % 2 != 0):
            print('Correct!')
            count += 1
        else:
            right_answer = 'yes' if number % 2 == 0 else 'no'
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            break
    else:
        print('Congratulations, you won!')


