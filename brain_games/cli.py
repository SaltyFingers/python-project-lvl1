#!/usr/bin/env python
import prompt


def user_name():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


if __name__ == "__main__":
    user_name()
