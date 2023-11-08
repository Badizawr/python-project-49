#!/usr/bin/env python3

import brain_games.cli
from brain_games.scripts.brain_even import brain_even
from brain_games.scripts.brain_calc import brain_calculator
from brain_games.scripts.brain_gcd import brain_gcd
from brain_games.scripts.brain_prime import brain_prime
from brain_games.scripts.brain_progression import brain_progression


def text_for_string():
    print(f"poetry run python -m brain_games.scripts.brain_games Welcome to the Brain Games!")


def main():
    text_for_string()
    brain_games.cli.welcome_user()
    temp = input("enter the game name: ")
    match temp:
        case "brain-even":
            return brain_even()
        case "brain-calc":
            return brain_calculator()
        case "brain-gcd":
            return brain_gcd()
        case "brain-progression":
            return brain_progression()
        case "brain-prime":
            return brain_prime()
    return f"Your input {temp}"


if __name__ == '__main__':
    main()
