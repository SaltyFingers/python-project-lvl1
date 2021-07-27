#!/usr/bin/env python
import prompt

ROUNDS = 3


def greeting():
    print('Welcome to the Brain Games!')


def get_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}! ')
    return name


def run_engine(game):
    greeting()
    name = get_name()
    print(game.TASK)
    for i in range(ROUNDS):
        question, correct_answer = game.game_logic()
        print(f'Quesion: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is the wrong answer :c. Correct answer was '{correct_answer}'\n\
Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
