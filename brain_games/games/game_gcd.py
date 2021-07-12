#!/usr/bin/env python
from brain_games.scripts.common_logic import (
    count,
    engine,
    random_number,
    welcome,
    welcome_user,
)


def gcd_logic():
    welcome()
    name = welcome_user()
    j = 0
    x = count()
    questions = []
    correct_answers = []
    print('Find the greatest common divisor of given numbers.')
    for j in range(x):
        number_1 = random_number()
        number_2 = random_number()
        questions.append(str(number_1) + ' ' + str(number_2))
        while number_1 != number_2:
            if number_1 > number_2:
                number_1 = number_1 - number_2
            else:
                number_2 = number_2 - number_1
        correct_answer = number_1
        correct_answers.append(correct_answer)

    engine(name=name, questions=questions, correct_answers=correct_answers)
