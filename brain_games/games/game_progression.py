#!/usr/bin/env python
from random import randint

TASK = 'What number is missing in the progression?'


def game_logic():
    first_number = randint(1, 100)
    delta = randint(1, 50)
    random_index = randint(0, 9)
    element = first_number
    progression = [str(first_number)]
    for x in range(9):
        element = element + delta
        progression.append(str(element))
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    progression = " ".join(progression)
    return progression, correct_answer
