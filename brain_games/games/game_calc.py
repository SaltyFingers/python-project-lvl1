#!/usr/bin/env python
import operator
from random import choice, randint

TASK = 'What is the result of the expression?'
operators = {
    '+': operator.add,
    '*': operator.mul,
    "-": operator.sub,
}
operators_list = list(operators.keys())


def game_logic():
    number_1, number_2 = randint(1, 100), randint(1, 100)
    operator_key = choice(operators_list)
    current_operator = operators.get(operator_key)
    question = '{} {} {}'.format(number_1, operator_key, number_2)
    return question, str(current_operator(number_1, number_2))
