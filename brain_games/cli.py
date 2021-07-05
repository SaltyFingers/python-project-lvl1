#!/usr/bin/env python
import prompt


def welcome_user():
    name = prompt.string('Hello there!\nMay I have your name, friend?\nMy name is ')
    print('Nice to meet you, ' + name + '!')
    return name 

if __name__ == "__main__":
    welcome_user()