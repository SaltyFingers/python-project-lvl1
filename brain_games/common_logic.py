#!/usr/bin/env python
import prompt

from brain_games.cli import user_name

ROUNDS = 3


def welcome():
    print('Welcome to the Brain Games!')


def is_right(game, name):
    for i in range(ROUNDS):
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
            return False


def engine(game):
    welcome()
    name = user_name()
    print(game.TASK)
    if is_right(game, name) is not False:
        print('Congratulations, ' + name + '!')
