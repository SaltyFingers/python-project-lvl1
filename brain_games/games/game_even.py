#!/usr/bin/env python
from random import randint


def even_logic():
    TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
    number = randint(1, 100)
    question = str(number)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    game = [TASK, question, correct_answer]
    # game = {
    #     'task': TASK,
    #     'question': question,
    #     'correct_answer': correct_answer,
    # }
    return game


if __name__ == '__main__':
    even_logic()
