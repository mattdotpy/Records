#!/usr/bin/env python3

"""
This module contains functions related to adding, modifying, deleting, and showing records of students including names
and IDs
"""

import sys

__author__ = 'Matthew Meyer'
__version__ = '1.0'
__copyright__ = "Copyright 2022.03.26, Student Records"
__github__ = "https://github.com/mattdotpy/Records.git"


#def create_student():

def main():
    while True:
        print('Student Menu')
        print('=' * 22)
        print('1 - List all students')
        print('2 - Add a student')
        print('3 - Update a student')
        print('4 - Delete a student')
        print('0 - Exit program')
        print()
        user_input = input('Please enter a Menu # (Valid 0-4): ')
        if user_input == '1':
            print('1 - List all students')
        elif user_input == '2':
            print('2 - Add a student')
        elif user_input == '3':
            print('3 - Update a student')
        elif user_input == '4':
            print('4 - Delete a student')
        elif user_input == '0':
            sys.exit()
        else:
            print('Invalid Input: Please enter a number greater or equal to 4')