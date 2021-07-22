#!/usr/bin/env python
from random import randint

TASK = 'Find the greatest common divisor of given numbers.'


def game_logic():
    number_1, number_2 = randint(1, 100), randint(1, 100)
    question = '{} {}'.format(number_1, number_2)
    while number_1 != number_2:
        if number_1 > number_2:
            number_1 = number_1 - number_2
        else:
            number_2 = number_2 - number_1
    return str(question), str(number_1)
