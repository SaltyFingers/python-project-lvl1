#!/usr/bin/env python
from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
FIRST_PRIME_NUMBER = 2
DEVIDER = 2
ONE = 1


def is_prime(number):
    x = 0
    if number < FIRST_PRIME_NUMBER:
        return False
    for i in range(FIRST_PRIME_NUMBER, number // DEVIDER + ONE):
        if (number % i == 0):
            x += 1
    return True if x <= 0 else False


def run_game():
    number = randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return str(number), str(correct_answer)
