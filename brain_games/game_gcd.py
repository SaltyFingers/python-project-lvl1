#!/usr/bin/env python
import random

import prompt
from brain_games.common_logic import *


def gcd_logic():
    name = welcome_user()
    i_num = 0
    i = 0
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)  
        print('Question: ' + str(number_1) + ' ' + str(number_2)) 
        answer = prompt.string('Your answer: ')
        if number_1 > number_2:
            number_more = number_1
            number_less = number_2
        elif number_1 < number_2:
            number_more = number_2
            number_less = number_1
        else:
            number_more = number_1
            number_less = number_more
            
        if number_more % number_less == 0:
            correct_answer = number_less
        #elif number_more % number_less != 0:
        else:
            i_num = number_less - 1
            while i_num >= 1:
                if number_more % number_less != 0:
                    i_num -= 1
                    number_less -= 1
                else:
                    correct_answer = number_less  
        print(correct_answer)
        #answer = prompt.string('Your answer: ')
        if int(answer) == correct_answer:
            print('Correct!')
            i_num += 1
        else:
            print("'" + str(answer) + "' is the wrong answer :c. Correct answer was '" + str(correct_answer) + "'" )
            return False
    print('Congratulations, ' + name + '!')
    


    
    



