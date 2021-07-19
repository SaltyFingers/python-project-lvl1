 #!/usr/bin/env python
from random import randint

from brain_games.scripts.common_logic import engine

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def question():
    return randint(1, 100)
  

def answer():
    if question() % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer

