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
        game_data = game.game_logic()
        question, correct_answer = game_data[0], game_data[1]
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print("'" + answer + "' is the wrong answer :c. \
Correct answer was '" + correct_answer + "'\
\nLet\'s try again, " + name + '!')
            break
    if current_round == 3:
        print('Congratulations, ' + name + '!')
