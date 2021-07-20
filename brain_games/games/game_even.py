#!/usr/bin/env python
from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_generation():
    return randint(1, 100)


def question(question):
    return str(question)


def answer(question):
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
