#!/usr/bin/env python
from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_generation():
    return randint(1, 100)


def question(question):
    return str(question)


def answer(question):
    x = 0
    for j in range(2, question // 2 + 1):
        if (question % j == 0):
            x += 1
    if x <= 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
