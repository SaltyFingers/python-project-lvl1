#!/usr/bin/env python
from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
FIRST_PRIME_NUMBER = 2


def is_prime(number):
    x = 0
    for i in range(FIRST_PRIME_NUMBER, number // FIRST_PRIME_NUMBER + 1):
        if (number % i == 0):
            x += 1
    if x <= 0 and number > FIRST_PRIME_NUMBER:
        return True
    else:
        return False


def game_logic():
    number = randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return str(number), str(correct_answer)
