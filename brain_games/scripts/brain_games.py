#!/usr/bin/env python3
import brain_games.cli
from brain_games.scripts.brain_even import brain_even
from brain_games.scripts.brain_calc import brain_calculator
from brain_games.scripts.brain_gcd import brain_gcd
from brain_games.scripts.brain_prime import brain_prime
from brain_games.scripts.brain_progression import brain_progression


def main():
    brain_games.cli.welcome_user()


if __name__ == '__main__':
    main()
