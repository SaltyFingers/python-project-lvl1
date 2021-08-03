#!/usr/bin/env python
from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(number):
    return True if number % 2 == 0 else False


def get_round():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(number) else 'no'
    return str(number), str(correct_answer)
