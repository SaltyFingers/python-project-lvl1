#!/usr/bin/env python
from random import randint

TASK = 'What number is missing in the progression?'
PROGRESSION_LENGHT = 9


def progression_fill(member, difference):
    progression = [str(member)]
    for i in range(PROGRESSION_LENGHT):
        member += difference
        progression.append(str(member))
    return progression


def get_progression_string(progression, random_index):
    progression[random_index] = '..'
    return " ".join(progression)


def game_logic():
    member = randint(1, 100)
    difference = randint(1, 50)
    random_index = randint(0, PROGRESSION_LENGHT)
    progression = progression_fill(member, difference)
    correct_answer = progression[random_index]
    return get_progression_string(progression, random_index), correct_answer
