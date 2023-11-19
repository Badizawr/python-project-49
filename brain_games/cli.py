import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    greeting = f"Welcome to the Brain Games!\nMay I have your name? {name}\nHello, {name}!"
    separator = "-" * 50
    games = ["brain-even", "brain-calc", "brain-gcd", "brain-progression", "brain-prime"]
    game_list = "\n".join(games)
    print(f"{greeting}\n{separator}\n{game_list}\n{separator}")

