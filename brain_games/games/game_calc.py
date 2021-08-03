#!/usr/bin/env python
import operator
from random import choice, randint

TASK = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
operators = {
    '+': operator.add,
    '*': operator.mul,
    "-": operator.sub,
}
operator_symbols = list(operators.keys())


def get_round():
    number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = randint(MIN_NUMBER, MAX_NUMBER)
    operator_symbol = choice(operator_symbols)
    current_operator = operators.get(operator_symbol)
    question = f'{number_1} {operator_symbol} {number_2}'
    return question, str(current_operator(number_1, number_2))
