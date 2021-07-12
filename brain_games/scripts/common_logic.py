import random

import prompt
from brain_games.games import *

def welcome():
    print('Welcome to the Brain Games!')

def welcome_user():
        name = prompt.string('May I have your name? ')
        print('Hello, ' + name + '!')
        return name


def random_number():
    number = random.randint(1, 100)
    return number


def count():
    ROUNDS = 3
    return ROUNDS


def engine(name, questions, correct_answers):
    index = 0
    current_round = 0
    rounds = count()
    for current_round in range(rounds):
        print('Question: ' + str(questions[index]))
        answer = prompt.string('Your answer: ')
        if isinstance(correct_answers[index], int):
            answer = int(answer)
        if answer == correct_answers[index]:
            print('Correct!')
            index += 1
            current_round += 1
        else:
            print("'" + str(answer) + "' is the wrong answer :c. Correct answer was '" + str(correct_answers[index]) + "'" '\nLet\'s try again, ' + name + '!' )
            return False
    if current_round == 3:
        print('Congratulations, ' + name + '!')
 

if __name__ == "__main__":
    engine()
