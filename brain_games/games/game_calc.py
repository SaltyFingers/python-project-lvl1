#!/usr/bin/env python
import operator
from random import choice, randint

TASK = 'What is the result of the expression?'
operators = {
    '+': operator.add,
    '*': operator.mul,
    "-": operator.sub,
}
operator_symbols_list = list(operators.keys())


def run_game():
    number_1, number_2 = randint(1, 100), randint(1, 100)
    operator_symbol = choice(operator_symbols_list)
    current_operator = operators.get(operator_symbol)
    question = f'{number_1} {operator_symbol} {number_2}'
    return question, str(current_operator(number_1, number_2))
