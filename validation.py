#!/usr/bin/env python3

"""
This module verifies input
"""

__author__ = 'Matthew Meyer'
__version__ = '1.0'
__copyright__ = "Copyright 2022.03.26, Student Records"
__github__ = "https://github.com/mattdotpy/Records.git"


def get_int_range(prompt, low, high):
    while True:
        user_input = input(f'{prompt} (Valid {low}--{high}): ')

        try:
            if user_input == 'int':
                number = int(user_input)
            else:
                number = float(user_input)

            if low <= number <= high:
                return number
            else:
                print(f'Invalid Input: Please enter a number greater than or equal to {low} and less than or equal '
                      f'to {high}')

        except ValueError:
            print('Must enter a number')


def get_yes_no(prompt, id, first_name, last_name):
    user_input = input(f'{prompt} (y=yes, n=No): ').lower()

    if user_input in ['y', 'yes']:
        return True
    elif user_input in ['n', 'no']:
        return False
    else:
        print('Invalid Input: Please enter a y=yes or n=no')

def get_pos_num(prompt):
