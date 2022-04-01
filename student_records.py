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

import validation

students = list()
id = 0


def find_student_index(students, id):
    for student in students:
        if id in student:
            return students.index(student)
    return -1


def create_student():
    global id

    print('Add Student')
    print('-' * 11)
    first_name = input('Please enter the Student\'s First Name: ')
    first_name = first_name.lower()
    first_name = first_name.capitalize()
    last_name = input('Please enter the Student\'s Last Name: ')
    last_name = last_name.lower()
    last_name = last_name.capitalize()
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


def update_student():
    global identification, first_name, last_name
    print(f'Update Student')
    print('-' * 11)

    if len(students) == 0:
        print('There are no students in this list')
        return

    id = validation.get_pos_num('Enter the ID of the student you want to update: ')

    student_index = find_student_index(students, id)

    if student_index == -1:
        print('There is no student with that ID, please try again.')
        return

    for selected_student in students[id]:
        identification, first_name, last_name = selected_student

    user_confirm = validation.get_yes_no(f'Do you want to update Student ID #{identification} {first_name} {last_name}')

    if user_confirm:
        new_first_name = input('Please enter the student\'s first name or press enter to keep '
                               + students[id - 1][1] + ': ').title()

        new_last_name = input('Please enter the student\'s last name or press enter to keep '
                               + students[id - 1][2] + ': ').title()

    if new_first_name > '':
        students[student_index][1] = new_first_name

    else:
        new_first_name = first_name

    if new_last_name > '':
        students[student_index][1] = new_last_name
    else:
        new_last_name = last_name


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