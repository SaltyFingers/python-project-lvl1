#!/usr/bin/env python
import random

import prompt


def welcome():
    name = prompt.string('Hello there!\nMay I have your name, friend?\nMy name is ')
    print('Nice to meet you, ' + name + '!')
    return name


def even_logic():
    name = welcome()
    i = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        number = random.randint(1, 100)
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        if number % 2 == 0 and answer == 'yes' or number % 2 != 0 and answer == 'no':
            print('Correct!')
            i = i +  1 
        else:
            print("'" + answer + "'" + ' is wrong answer :c. Correct answer was ' + "'" + correct_answer + "'" '\nLet\'s try again, ' + name + '!')
            i = 0
    print('Congratulations, ' + name + '!')
 

