import random

import prompt
from brain_games.scripts.common_logic import welcome_user 


def prime_logic():
    name = welcome_user()
    i = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while i < 3:
        number = random.randint(1, 100)
        def is_prime(number):
            d = 0    
            for j in range(2, number // 2 + 1):
                if (number % j == 0):
                    d += 1
            if d <= 0:
                correct_answer = 'yes'
            else:
                correct_answer = 'no'
            return correct_answer
        correct_answer = is_prime(number)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        if str(answer) == str(correct_answer):
            print('Correct!')
            i += 1
        else:
            print("'" + str(answer) + "' is the wrong answer :c. Correct answer was '" + str(correct_answer) + "'" '\nLet\'s try again, ' + name + '!' )
            i = 0      
    
    print('Congratulations, ' + name + '!')