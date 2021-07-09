import prompt
import random
#from brain_games import game_even, game_calc, game_gcd, brain_progression, brain_prime
#from brain_games.scripts import brain_even, brain_calc, brain_gcd, brain_progression, brain_prime

def welcome_user():
        print('Welcome to the Brain Games!')
        name = prompt.string('Hello there!\nMay I have your name, friend?\nMy name is ')
        print('Nice to meet you, ' + name + '!')
        return name


# def choose_the_game():
#     name = welcome_user()
#     print('Which game do you want to begin?:\
#     \n1. Even \n2. Calc \n3. GCD \n4. Progression \n5. Prime\
#     \nEnter, for example, 1 or Even or 1. Even')
#     def games():
#         game = prompt.string('Time to choose: ')
#         if game == 1 or str(game) == 'Even' or str(game) == '1. Even':
#             brain_even()
#         elif game == 2 or str(game) == 'Calc' or str(game) == '2. Calc':
#             brain_calc()
#         elif game == 3 or game == 'GCD' or game == '3. GCD':
#             brain_gcd()
#         elif game == 4 or game == 'Progression' or game == '4. Progression':
#             brain_progression()
#         elif game == 5 or game == 'Prime' or game == '5. Prime':
#             brain_prime()
#         else:
#             print('Please, ' + name + ', enter the correct name' )
#         games()


def engine(question, correct_answer, name):
    index = 0
    for index in range(3):
                
        print(question)
        
        answer = prompt.string('Your answer: ')

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
    print('Congratulations, ' + name)
 
    # def random_number():
    #     random_number = random.randint(1,100)
    #     return random_number


if __name__ == "__main__":
    engine()
