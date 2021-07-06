import prompt
import random

def engine():

    def welcome_user():
        print('Welcome to the Brain Games!')
        name = prompt.string('Hello there!\nMay I have your name, friend?\nMy name is ')
        print('Nice to meet you, ' + name + '!')
        return name

    
    def random_number():
        random_number = random.randint(1,100)
        return random_number


    def right_answer():
        print('Correct!\nLet\'s try this one!')


    def wrong_answer(answer, correct_answer, name):
        print("'" + str(answer) + "' is the wrong answer :c. Correct answer was '" + str(correct_answer) + "'" )
        try_again = prompt.string('Do you want to try again?\n1. yes\n2. no')
        if try_again == 1 or str(try_again) == 'yes':
            print('Let\'s try again, ' + name + '!')
        else:
            return False

    
    def count_answers():

if __name__ == "__main__":
    engine()



