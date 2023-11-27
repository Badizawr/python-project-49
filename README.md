### Hexlet tests and linter status:
[![Actions Status](https://github.com/Badizawr/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/Badizawr/python-project-49/actions)

<a href="https://codeclimate.com/github/DarkWolf1990/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/dd977484c3b5d792291a/maintainability" /></a>
<a href="https://codeclimate.com/github/DarkWolf1990/python-project-49/test_coverage"><img src="https://api.codeclimate.com/v1/badges/dd977484c3b5d792291a/test_coverage" /></a>
Описание проекта:

Проект представляет собой несколько консольных миниигр на языке программирования Python. Вам предлагается 3 попытки до победы. Нельзя совершать ошибку, игру придется начинать заново. Список игр:

    brain-calc - посчитайте результат операции, отсуствует операция деления
    brain-even - является ли показанное число чётным?
    brain-gcd - определяем наибольший общий делитель между двумя числами
    brain-progression - пропущенный элемент в арифметической прогрессии. Как быстро вы сможете догадаться какое число нужно ввести?
    brain-prime - простые числа и этим всё сказано!

Минимальные требования:

Вам понадобится UNIX-подобная операционная система

    Python 3.10.12 и выше
    Инструмент для управления зависимостями и сборки пакетов Poetry
    Пакет make

Инструкция по установке и запуску:

    Клонируйте гит к себе на компьютер

git clone git@github.com:Badizawr/python-project-49.git

    Перейдите в директорию проекта.

cd python-project-49

    Установите необходимые зависимости.

poetry install
make install
make build
make package-install

На ваш выбор запускаете, к примеру, brain-calc. Вызвать нужную игру можно следующими командами:

    brain-calc
    brain-even
    brain-gcd
    brain-progression
    brain-prime

Демонстрация работы
[![asciicast](https://asciinema.org/a/3hfHKrDx3sielQAiQq2Ri0PoC.svg)](https://asciinema.org/a/3hfHKrDx3sielQAiQq2Ri0PoC)
