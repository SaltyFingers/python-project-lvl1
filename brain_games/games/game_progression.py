#!/usr/bin/env python
from random import randint

TASK = 'What number is missing in the progression?'
    

def question_generation():
    first_number = randint(1, 100)
    delta = randint(1, 50)
    random_index = randint(0, 9)
    element = first_number
    progression = [str(first_number)]
    for x in range(9):
        element = element + delta
        progression.append(str(element))
    answer = progression[random_index]
    return [progression, random_index, answer]


def question(question):    
    question[0][question[1]] = '..'
    question[0] = " ".join(question[0])
    return str(question[0])  


def answer(question):
    return question[2]
