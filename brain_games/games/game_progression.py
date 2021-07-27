#!/usr/bin/env python
from random import randint

TASK = 'What number is missing in the progression?'
PROGRESSION_LENGHT = 9


def progression_fill(first_number, difference):
    member = first_number
    progression = [str(first_number)]
    for i in range(PROGRESSION_LENGHT):
        member = member + difference
        progression.append(str(member))
    return progression


def get_progression_string(progression, random_index):
    progression[random_index] = '..'
    return " ".join(progression)


def game_logic():
    first_number = randint(1, 100)
    difference = randint(1, 50)
    random_index = randint(0, PROGRESSION_LENGHT)
    progression = get_progression_string(first_number, difference)
    correct_answer = progression[random_index]
    return get_progression_string(progression, random_index), correct_answer
