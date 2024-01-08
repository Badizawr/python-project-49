### Hexlet tests and linter status:
[![Actions Status](https://github.com/Badizawr/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/Badizawr/python-project-49/actions)

<a href="https://codeclimate.com/github/DarkWolf1990/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/dd977484c3b5d792291a/maintainability" /></a>
<a href="https://codeclimate.com/github/DarkWolf1990/python-project-49/test_coverage"><img src="https://api.codeclimate.com/v1/badges/dd977484c3b5d792291a/test_coverage" /></a>
Project description:

The project consists of several console mini-games in the Python programming language. You are given 3 attempts to win.
You can't make a mistake, you'll have to start the game again. List of games:

    brain-calc - "calculate the result of the operation, there is no division operation"
    brain-even - "Is the number shown even?"
    brain-gcd - "Determine the greatest common divisor between two numbers"
    brain-progression - "Missing element in an arithmetic progression. How quickly can you guess what number you need to enter?"
    brain-prime - "Prime numbers and that's it!"

Minimum requirements:

You will need a UNIX-like operating system

    Python 3.10.12 and higher
    Dependency management and package building tool Poetry
    Package make

Installation and startup instructions:

    Clone git to your computer

git clone git@github.com:Badizawr/python-project-49.git

    Go to the project directory.

cd python-project-49

    Install the required dependencies.

poetry install
make install
make build
make package-install

At your choice, run, for example, brain-calc. You can call the desired game using the following commands:

    brain-calc
    brain-even
    brain-gcd
    brain-progression
    brain-prime

Demonstration of work
[![asciicast](https://asciinema.org/a/3hfHKrDx3sielQAiQq2Ri0PoC.svg)](https://asciinema.org/a/3hfHKrDx3sielQAiQq2Ri0PoC)
