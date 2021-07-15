#!/usr/bin/env python
import operator
from random import choice, randint


def calc_logic():
    operators = {
        ' + ': operator.add,
        ' * ': operator.mul,
        " - ": operator.sub,
    }
    operators_list = list(operators.keys())
    task = 'What is the result of the expression?'
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operator_key = choice(operators_list)
    current_operator = operators.get(operator_key)
    question = str(number_1) + operator_key + str(number_2)
    correct_answer = current_operator(number_1, number_2)
    game = {
        'task': task,
        'question': question,
        'correct_answer': correct_answer,
    }
    return game


if __name__ == '__main__':
    game_logic()
