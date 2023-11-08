import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Welcome to the Brain Games!\nMay I have your name? {name}\nHello, {name}!")
    print("------------------------------------------------")
    print("brain-even\nbrain-calc\nbrain-gcd\nbrain-progression\nbrain-prime")
    print("------------------------------------------------")
