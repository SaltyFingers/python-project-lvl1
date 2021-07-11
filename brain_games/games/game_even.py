#!/usr/bin/env python

from brain_games.scripts.common_logic import (
    count,
    engine,
    random_number,
    welcome_user,
)


def even_logic():
    name = welcome_user()
    x = count()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    questions = []
    correct_answers = []
    j = 0
    for j in range (x):
        number = random_number()
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        j += 1
        questions.append(str(number))
        correct_answers.append(correct_answer)

    
    engine(name = name, questions = questions, correct_answers = correct_answers)
 

