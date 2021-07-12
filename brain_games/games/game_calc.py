#!/usr/bin/env python
import operator
from random import choice

from brain_games.scripts.common_logic import (
    count,
    engine,
    random_number,
    welcome,
    welcome_user,
)


def calc_logic():
    welcome()
    name = welcome_user()
    j = 0
    x = count()
    questions = []
    correct_answers = []
    operators = {
        '+': operator.add,
        '*': operator.mul,
        "-": operator.sub,
    }
    operators_list = list(operators.keys())
    print('What is the result of the expression?')
    for j in range(x):
        number_1 = random_number()
        number_2 = random_number()
        operator_key = choice(operators_list)
        current_operator = operators.get(operator_key)
        questions.append(str(number_1) + ' ' + operator_key + ' '
                                                  + str(number_2))
        correct_answers.append(current_operator(number_1, number_2))

    engine(name=name, questions=questions, correct_answers=correct_answers)
