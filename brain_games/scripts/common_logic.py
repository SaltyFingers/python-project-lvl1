import prompt
import random
from brain_games.games import *

def welcome_user():
        print('Welcome to the Brain Games!')
        name = prompt.string('Hello there!\nMay I have your name, friend?\nMy name is ')
        print('Nice to meet you, ' + name + '!')
        return name


def choose_the_game():
    game = prompt.string('Which game do you want to begin?\
    \n1. Even \n2. Calc \n3. GCD \n4. \n5.')        


def engine(question, correct_answer, answer, name):
    index = 0
    for index in range(3):
        
        
        print(question)
        
        if int(answer) == correct_answer:
            print('Correct!\nLet\'s try this one!')
            index += 1
        else:
            print("'" + str(answer) + "' is the wrong answer :c. Correct answer was '" + str(correct_answer) + "'" )
            try_again = prompt.string('Do you want to try again?\n1. yes\n2. no')
            if try_again == 1 or str(try_again) == 'yes':
                print('Let\'s try again, ' + name + '!')
                index = 0
            else:
                return False
        

    
    
    
    
    # def random_number():
    #     random_number = random.randint(1,100)
    #     return random_number


if __name__ == "__main__":
    engine()



