import random

import prompt
# from brain_games.games.game_even import game_logic
# from brain_games.games.game_calc import game_logic
# from brain_games.games.game_gcd import game_logic



# def welcome():
#     print('Welcome to the Brain Games!')


# def welcome_user():
#     name = prompt.string('May I have your name? ')
#     print('Hello, ' + name + '!')
#     return name


# def random_number():
#     number = random.randint(1, 100)
#     return number


# def count():
#     ROUNDS = 3
#     return ROUNDS
ROUNDS = 3


def engine(game):
    
    
    def welcome():
        print('Welcome to the Brain Games!')
    
    
    def welcome_user():
        name = prompt.string('May I have your name? ')
        print('Hello, ' + name + '!')
        return name
    

    welcome() #
    name = welcome_user() #
    # task = game[1]
    print(TASK)
    for current_round in range(ROUNDS):
        question = game['question']
        correct_answer = game['correct_answer']
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if isinstance(correct_answer, int):
            answer = int(answer)
        if answer == correct_answer:
            print('Correct!')
            current_round += 1
        else:
            print("'" + str(answer) + "' is the wrong answer :c.\
            Correct answer was '" + str(correct_answer) + "'\
\nLet\'s try again, " + name + '!')
            return False
    if current_round == 3:
        print('Congratulations, ' + name + '!')


if __name__ == "__main__":
    engine()
