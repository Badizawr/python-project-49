from random import randint, choice


def brain_calculator():
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        x, y = randint(1, 100), randint(1, 100)
        op = choice(['+', '-', '*'])

        print(f'{x} {op} {y}')
        answer = input('Your answer: ')
        if answer == str(eval(f'{x}{op}{y}')):
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{eval(f'{x}{op}{y}')}'.")
            break
    else:
        print('Congratulations, you won!')


def main():
    brain_calculator()


if __name__ == '__main__':
    main()
