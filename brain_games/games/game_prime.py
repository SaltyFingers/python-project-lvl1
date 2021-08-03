#!/usr/bin/env python
from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
FIRST_PRIME_NUMBER = 2
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number < FIRST_PRIME_NUMBER:
        return False
    for i in range(FIRST_PRIME_NUMBER, number // 2 + 1):
        return False if (number % i == 0) else True


def get_round():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return str(number), str(correct_answer)
