#!/usr/bin/env python
from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
DEVIDER = 2


def is_even(number):
    return True if number % DEVIDER == 0 else False


def run_game():
    number = randint(1, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    return str(number), str(correct_answer)
