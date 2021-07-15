#!/usr/bin/env python
from random import randint


def progression_logic():
    task = 'What number is missing in the progression?'
    first_number = randint(1, 100)
    delta = randint(1, 20)
    random_index = randint(0, 9)
    element = first_number
    progression = [str(first_number)]
    for x in range(9):
        element = element + delta
        progression.append(str(element))
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    progression = " ".join(progression)
    question = str(progression)
    game = {
        'task': task,
        'question': question,
        'correct_answer': correct_answer,
    }
    return game


if __name__ == '__main':
    progression_logic()
   
