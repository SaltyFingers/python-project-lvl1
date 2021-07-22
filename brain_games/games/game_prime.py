#!/usr/bin/env python
from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    x = 0
    for j in range(2, number // 2 + 1):
        if (number % j == 0):
            x += 1
    if x <= 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def game_logic():
    number = randint(1, 100)
    return str(number), str(is_prime(number))
