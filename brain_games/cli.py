import prompt
# from brain_games.scripts.brain_even import brain_even
# from brain_games.scripts.brain_calc import brain_calculator
# from brain_games.scripts.brain_gcd import brain_gcd
# from brain_games.scripts.brain_prime import brain_prime
# from brain_games.scripts.brain_progression import brain_progression


def welcome_user():
    name = prompt.string('May I have your name? ')
    greeting = f"Welcome to the Brain Games!\nMay I have your name? {name}\nHello, {name}!"
    separator = "-" * 50
    games = ["brain-even", "brain-calc", "brain-gcd", "brain-progression", "brain-prime"]
    game_list = "\n".join(games)
    print(f"{greeting}\n{separator}\n{game_list}\n{separator}")

    # temp = input("enter the game name: ")
    # match temp:
    #     case "brain-even":
    #         return brain_even()
    #     case "brain-calc":
    #         return brain_calculator()
    #     case "brain-gcd":
    #         return brain_gcd()
    #     case "brain-progression":
    #         return brain_progression()
    #     case "brain-prime":
    #         return brain_prime()
    # return f"Your input {temp}"
