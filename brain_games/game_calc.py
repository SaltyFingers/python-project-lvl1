#!/usr/bin/env python
import operator
from random import randint, choice

import prompt


def welcome():
    name = prompt.string('Hello there!\nMay I have your name, friend?\nMy name is ')
    print('Nice to meet you, ' + name + '!')
    return name


def calc_logic():
    name = welcome()
    i = 0
    ops_list = (operator.add, operator.mul, operator.sub)
    print('What is the result of the expression?')
    for i in range(3):
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        op = choice(ops_list)
        if op == operator.add:
            question = (str(number_1) + ' + ' + str(number_2) + ' =')
            correct_answer = number_1 + number_2
        elif op == operator.mul:
            question = (str(number_1) + ' * ' + str(number_2) + ' =')
            correct_answer = number_1 * number_2
        else:
            question = (str(number_1) + ' - ' + str(number_2) + ' =')
            correct_answer = number_1 - number_2
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if int(answer) == correct_answer:
            print('Correct!')
            i += 1
        else:
            print("'" + str(answer) + "' is the wrong answer :c. Correct answer was '" + str(correct_answer) + "'" )
            return False
    print('Congratulations, ' + name + '!')

        