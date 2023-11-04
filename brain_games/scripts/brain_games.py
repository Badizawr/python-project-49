#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import brain_even
from brain_games.scripts.brain_calc import brain_calculator
from brain_games.scripts.brain_gcd import brain_gcd


def text_for_string():
    print(f"poetry run python -m brain_games.scripts.brain_games Welcome to the Brain Games!")


def main():
    text_for_string()
    welcome_user()
    brain_even()
    brain_calculator()
    brain_gcd()


if __name__ == '__main__':
    main()
