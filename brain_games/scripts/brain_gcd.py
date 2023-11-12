from random import randint
from math import gcd


def brain_gcd():
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        x, y = randint(1, 100), randint(1, 100)
        print(f'{x} {y}')
        answer = input('Your answer: ')
        if answer == str(gcd(x, y)):
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{gcd(x, y)}'.")
            break
    else:
        print('Congratulations, you won!')


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
