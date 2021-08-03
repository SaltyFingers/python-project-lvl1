#!/usr/bin/env python
from random import randint

TASK = 'What number is missing in the progression?'
PROGRESSION_LENGHT = 10
MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_INDEX = 0
MAX_INDEX = PROGRESSION_LENGHT - 1
MIN_DIFFERENCE = 1
MAX_DIFFERENCE = 50


def build_progression(initial_term, difference):
    member, progression = initial_term, [initial_term]
    for i in range(PROGRESSION_LENGHT):
        member += difference
        progression.append(member)
    return progression


def get_string_from_progression(progression, hole_index):
    progression_string = []
    for index in range(0, PROGRESSION_LENGHT):
        progression_string.append(str(progression[index]))
    progression_string[hole_index] = '..'
    return " ".join(progression_string)


def get_round():
    initial_term = randint(MIN_NUMBER, MAX_NUMBER)
    difference = randint(MIN_DIFFERENCE, MAX_DIFFERENCE)
    hole_index = randint(MIN_INDEX, MAX_INDEX)
    progression = build_progression(initial_term, difference)
    return (get_string_from_progression(progression, hole_index),
            str(progression[hole_index]))
