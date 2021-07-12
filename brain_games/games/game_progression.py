
import random

from brain_games.scripts.common_logic import (
    count,
    engine,
    random_number,
    welcome_user,
)


def progression_logic():
    name = welcome_user()
    j = 0
    x = count()
    questions = []
    correct_answers = []
    print('What number is missing in the progression?')
    for j in range(x):
        first_number = random_number()
        delta = random.randint(1, 20)
        random_index = random.randint(0,9)
        element = first_number
        progression = [str(first_number)]
        for x in range(9):
            element = element + delta
            progression.append(str(element))
        correct_answers.append(progression[random_index])
        progression[random_index] = '..'
        progression = " ".join(progression)
        questions.append(str(progression))
    engine(name = name, questions = questions, correct_answers = correct_answers)
