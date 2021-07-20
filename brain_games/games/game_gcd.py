#!/usr/bin/env python
from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def question_generation():
    number_1 = randint(1, 100)
    number_2 = randint(1, 101)
    return [number_1, number_2]


def answer(question):
    while question[0] != question[1]:
        if question[0] > question[1]:
            question[0] = question[0] - question[1]
        else:
            question[1] = question[1] - question[0]
    return question[0]


def question(question):
    return '{} {}'.format(question[0], question[1])
