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


def question_generation():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operator_key = choice(operators_list)
    question = number_1, operator_key, number_2
    return question


def question(question):
    question = '{} {} {}'.format(question[0], question[1], question[2])
    return question


def answer(question):
    current_operator = operators.get(question[1])
    correct_answer = current_operator(question[0], question[2])
    return correct_answer
