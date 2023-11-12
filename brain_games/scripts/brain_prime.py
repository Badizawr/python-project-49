from random import randint


def brain_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        number = randint(1, 100)
        print(number)
        answer = input('Your answer: ')
        if (answer == 'yes' and is_prime(number)) or (answer == 'no' and not is_prime(number)):
            print('Correct!')
            count += 1
        else:
            right_answer = 'yes' if is_prime(number) else 'no'
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            break
    else:
        print('Congratulations, you won!')


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    brain_prime()


if __name__ == '__main__':
    main()
