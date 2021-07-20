#!/usr/bin/env python
import prompt

ROUNDS = 3


def welcome():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def engine(game):
    welcome()
    name = welcome_user()
    print(game.TASK)
    for current_round in range(ROUNDS):
        question_generation = game.question_generation()
        question = game.question(question_generation)
        correct_answer = game.answer(question_generation)
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if isinstance(correct_answer, int):
            answer = int(answer)
        else:
            answer = str(answer)
        if answer == correct_answer:
            print('Correct!')
            current_round += 1
        else:
            print("'" + str(answer) + "' is the wrong answer :c. \
Correct answer was '" + str(correct_answer) + "'\
\nLet\'s try again, " + name + '!')
            return False
    if current_round == 3:
        print('Congratulations, ' + name + '!')
