#!/usr/bin/env python
from random import randint

from brain_games.scripts.common_logic import random_number

questions = []
correct_answers = []

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


number = random_number()

def question_func():
    question = str(number)
    return question
    


def answer_func():

    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
# return task_funk, question_func, answer_func



# if __name__ == '__main__':
#     rand_num()
#     task_func()
#     question_func()
#     answer_func()
