#!/usr/bin/env python
from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def game_logic():
    number = randint(1, 100)
    return str(number), str(is_even(number))
