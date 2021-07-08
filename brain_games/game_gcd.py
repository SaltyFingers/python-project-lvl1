#!/usr/bin/env python
import random

import prompt
from brain_games.scripts.common_logic import welcome_user 


def gcd_logic():
    name = welcome_user()
    i = 0
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)  
        print('Question: ' + str(number_1) + ' ' + str(number_2))
        while number_1 != number_2: 
            if number_1 > number_2:
                number_1 = number_1 - number_2
            else:
                number_2 = number_2 - number_1
        correct_answer = number_1
        answer = prompt.string('Your answer: ')
        if int(answer) == correct_answer:
            print('Correct!')
            i += 1
        else:
            print("'" + str(answer) + "' is the wrong answer :c. Correct answer was '" + str(correct_answer) + "'" )
            return False
    print('Congratulations, ' + name + '!')
    


    
    



