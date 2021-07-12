#!/usr/bin/env python
from brain_games.scripts.common_logic import (
    count,
    engine,
    random_number,
    welcome,
    welcome_user,
)


def prime_logic():
    welcome()
    name = welcome_user()
    j = 0
    x = count()
    questions = []
    correct_answers = []
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for j in range(x):
        number = random_number()
        questions.append(str(number))

        def is_prime(number):
            d = 0
            for j in range(2, number // 2 + 1):
                if (number % j == 0):
                    d += 1
            if d <= 0:
                correct_answer = 'yes'
            else:
                correct_answer = 'no'
            return correct_answer
        correct_answers.append(is_prime(number))
    engine(name=name, questions=questions, correct_answers=correct_answers)
