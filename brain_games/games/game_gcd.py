#!/usr/bin/env python
from random import randint

def gcd_logic():
    task = 'Find the greatest common divisor of given numbers.'
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = str(number_1) + ' ' + str(number_2)
    while number_1 != number_2:
        if number_1 > number_2:
            number_1 = number_1 - number_2
        else:
            number_2 = number_2 - number_1
    correct_answer = number_1
    game = {
        'task': task,
        'question': question,
        'correct_answer': correct_answer,
    }
    return game


if __name__ == '__main__':
    game_logic()