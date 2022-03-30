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


students = list()
id = 0


def create_student():

    global id

    print('Add Student')
    print('-' * 11)
    first_name = input('Please enter the Student\'s First Name: ')
    last_name = input('Please enter the Student\'s Last Name: ')
    id += 1
    students.append((id, first_name, last_name))
    print(students)


def list_student():
    print(f'ID First Name      Last Name')
    print(f'== =============== ===============')
    for student_info in students:
        identification, first_name, last_name = student_info
        print(f'{identification}  {first_name}            {last_name}')
    print()


def update_student(students):
    print(f'Update Student')
    print('-' * 11)

    if len(students) == 0:
        print('There are no students in this list')
        return

    id = v.get_pos_num('Enter the ID of the student you want to update')
    student_index = list_student(students, id)

    if student_index == -1:
        print('There is no student with that ID, please try again.')
        return

    selected_student = students[id]
    id, first_name, last_name = selected_student

    user_confirm = v.get_yes_no(f'Do you want to update Student ID # {id} {first_name} {last_name} ')

    if user_confirm:
        new_first_name = input('Please enter the student\'s first name or press enter to keep '
                               + students[id - 1][1] + ': ').title()
        new_last_name = input('Please enter the student\'s last name or press enter to keep '
                               + students[id - 1][2] + ': ').title()


def delete_student():
    print(f'Delete Student')
    print('-' * 11)








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
        user_input = input('Please enter a Menu # (Valid 0-4): ')
        if user_input == '1':
            print('1 - List all students')
            list_student()
        elif user_input == '2':
            print('2 - Add a student')
            create_student()
        elif user_input == '3':
            print('3 - Update a student')
            update_student()
        elif user_input == '4':
            print('4 - Delete a student')
            #delete_student()
        elif user_input == '0':
            sys.exit()
        else:
            print('Invalid Input: Please enter a number greater or equal to 4')

if __name__ == '__main__':
    main()