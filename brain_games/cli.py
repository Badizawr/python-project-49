import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Welcome to the Brain Games!\nMay I have your name? {name}\nHello, {name}!")
