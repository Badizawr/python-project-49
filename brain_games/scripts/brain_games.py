#!/usr/bin/env python3
from cli import welcome_user



def text_for_string():
    print(f"poetry run python -m brain_games.scripts.brain_games Welcome to the Brain Games!")


def main():
    text_for_string()
    welcome_user()



if __name__ == '__main__':
    main()