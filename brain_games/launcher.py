import prompt
from brain_games.const_file import CHANCE


def start(game):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)

    for _ in range(CHANCE):

        question, corr_answer = game.generate_data()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == corr_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{corr_answer}'")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
