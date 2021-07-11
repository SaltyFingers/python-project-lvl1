
import random

import prompt
from brain_games.scripts.common_logic import welcome_user 


def progression_logic():
    name = welcome_user()
    i = 0
    print('What number is missing in the progression?')
    while i < 3:
        first_number = random.randint(0, 50)
        delta = random.randint(1, 20)
        random_index = random.randint(0,9)
        element = first_number
        progression = [str(first_number)]
        for x in range(9):
            element = element + delta
            progression.append(str(element))
        correct_answer = progression[random_index]
        progression[random_index] = '..'
        progression = " ".join(progression)
        question = str(progression)
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if int(answer) == int(correct_answer):
            print('Correct!')
            i += 1
        else:
            print("'" + str(answer) + "' is the wrong answer :c. Correct answer was '" + str(correct_answer) + "'" '\nLet\'s try again, ' + name + '!' )
            i = 0      
    if i == 3:
        print('Congratulations, ' + name + '!')