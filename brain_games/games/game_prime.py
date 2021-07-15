#!/usr/bin/env python
from random import randint


def prime_logic():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    number = randint(1, 100)
    question = str(number)
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
    game = {
        'task': task,
        'question': question,
        'correct_answer': is_prime(number),
    }
    return game    


if __name__ == '__main':
    prime_logic()
   