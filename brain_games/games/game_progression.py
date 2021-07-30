#!/usr/bin/env python
from random import randint

TASK = 'What number is missing in the progression?'
PROGRESSION_LENGHT = 10


def add_progression_member(initial_term, difference):
    member, progression = initial_term, [initial_term]
    for i in range(PROGRESSION_LENGHT):
        member += difference
        progression.append(member)
    return progression


def get_string_from_progression(progression, random_number):
    progression_string = []
    for member in range(0, PROGRESSION_LENGHT):
        progression_string.append(str(progression[member]))
    progression_string[random_number] = '..'
    return " ".join(progression_string)


def run_game():
    initial_term = randint(1, 100)
    difference = randint(1, 50)
    random_number = randint(0, PROGRESSION_LENGHT - 1)
    progression = add_progression_member(initial_term, difference)
    return (get_string_from_progression(progression, random_number),
            str(progression[random_number]))
