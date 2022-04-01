#!/usr/bin/env python3

"""
This module contains functions related to adding, modifying, deleting, and showing records of students including names
and IDs
"""

__author__ = 'Matthew Meyer'
__version__ = '1.0'
__copyright__ = "Copyright 2022.03.26, Student Records"
__github__ = "https://github.com/mattdotpy/Records.git"

import validation
import student_records

def main():
    """
    Main module that takes user input from 0-4 and calls functions based on that input

    :return: None
    """
    while True:
        print('Student Menu')
        print('=' * 22)
        print('1 - List all students')
        print('2 - Add a student')
        print('3 - Update a student')
        print('4 - Delete a student')
        print('0 - Exit program')
        print()
        user_input = validation.get_int_range('Please enter a menu #', 0, 4)

        if user_input == 1:
            print('1 - List all students')
            list_student()
        elif user_input == 2:
            print('2 - Add a student')
            create_student()
        elif user_input == 3:
            print('3 - Update a student')
            update_student()
        elif user_input == 4:
            print('4 - Delete a student')
            #delete_student()
        elif user_input == 0:
            print('Goodbye')
            sys.exit()
        else:
            print('Invalid Input: Please enter a number greater or equal to 4')


if __name__ == '__main__':
    main()