#!/usr/bin/env python
import operator
from random import choice

import prompt
from brain_games.scripts.common_logic import (
    count,
    engine,
    random_number,
    welcome_user,
)


def calc_logic():
    name = welcome_user()
    j = 0
    x = count()
    questions = []
    correct_answers = []
    op_list = {
        '+': operator.add ,
        '*': operator.mul ,
        "-": operator.sub 
        }
    print('What is the result of the expression?')
    for j in range(x):
        number_1 = random_number()
        number_2 = random_number()
        op = choice(op_list) 
        questions.append(str(number_1) + op + str(number_2))
        correct_answers.append(op(number_1, number_2))

    engine(name = name, questions = questions, correct_answers = correct_answers)