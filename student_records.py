#!/usr/bin/env python3

"""
This module contains functions related to adding, modifying, deleting, and showing records of students including names
and IDs
"""

__author__ = 'Matthew Meyer and Kyla Phillips'
__version__ = '1.0'
__copyright__ = "Copyright 2022.03.26, Student Records"
__github__ = "https://github.com/mattdotpy/Records.git"

import validation  # import the validation to get validation functions
import sys


students = list()  # this is our list to store the students
id = 0


def create_student():
    """
    This function gets the user input to create the student to be put in the list.  Once it is created,
    the list is appended to follow the structure of id, first name, last name.
    """
    global id

    print('Add Student')
    print('-' * 11)
    first_name = input('Please enter the Student\'s First Name: ')  # the first name is put in by the user
    first_name = first_name.lower()
    first_name = first_name.title()
    last_name = input('Please enter the Student\'s Last Name: ')  # the last name is put in by the user
    last_name = last_name.lower()
    last_name = last_name.title()
    id += 1
    students.append([id, first_name, last_name])
    # id will be assigned depending on order entered, then  the first name, then the last name


def list_student():
    """
    This function is how we display the list of students
    """
    if len(students) == 0:  # if there are no students in the list, display the message
        print('There are no students in this list')
        print()
        return
    print(f'{"ID":>4s} {"First Name":<15s} {"Last Name":<15s}')  # match spacing
    print('=' * 4, '=' * 15, '=' * 15)
    for student_info in students:
        identification, first_name, last_name = student_info
        print(f'{identification:>4d} {first_name:<15s} {last_name:<15s}')  # match spacing
    print()


def find_student_index(students, selected_id):
    """

    :param students: student data (id, first_name, last_name)
    :type students: 2d list
    :param selected_id: student id that the user wants to find
    :type selected_id: int
    :return: the index of the student in the 2D list or -1 if not found
    :rtype: int
    """
    for student in students:
        if selected_id in student:
            return students.index(student)
    return -1


def update_student():
    """
    Updates the select student. The user can either change the selected student's first or last name.
    :return:
    """
    print(f'Update Student')
    print('-' * 11)

    if len(students) == 0:
        print('There are no students in this list')
        return

    #  the user selected id is the one student that will be changed by their first or last name
    selected_id = validation.get_num('Enter the ID of the student you want to update: ', 0)

    student_index = find_student_index(students, selected_id)   # use the index to find the student in the list

    if student_index == -1:  # if -1 is returned, then the student does not exist in the list
        print('There is no student with that ID, please try again.')
        return

    student = students[student_index]
    identifier, first_name, last_name = student

    #  Ask the user to confirm that this is the student they want to update
    user_confirm = validation.get_yes_no(f'Do you want to update ' 
                                         f'Student ID #{identifier} {first_name} {last_name} (y/n): ')

    if not user_confirm:
        print('Update cancelled')
        return

    # new names for the students or they can choose to keep the names.
    new_first_name = input(f'Please enter the student\'s first name or press enter to keep {first_name}: ').title()

    new_last_name = input(f'Please enter the student\'s last name or press enter to keep {last_name}: ').title()

    if new_first_name == '' and new_last_name == '':
        print('No data changed. Update Cancelled')
        return

    if new_first_name > '':
        student[1] = new_first_name

    if new_last_name > '':
        student[2] = new_last_name

    print('Update Complete')


def delete_student():

    print(f'Delete Student')
    print('-' * 11)

    if len(students) == 0:
        print('There are no students in this list')
        return

    # The selected student will be the one deleted.
    selected_id = validation.get_num('Enter the ID of the student you want to delete: ', 0)

    student_index = find_student_index(students, selected_id)

    if student_index == -1:
        print('There is no student with that ID, please try again.')
        return

    student = students[student_index]  # sets the student in the list.
    identifier, first_name, last_name = student

    # Confirm that the selected student is the one that will be deleted
    user_confirm = validation.get_yes_no(f'Are you sure you want to delete '
                                         f'Student ID #{identifier} {first_name} {last_name} (y/n): ')

    if not user_confirm:  # can choose to not go through with it.
        print('Delete cancelled')
        return

    del students[student_index]  # removes the selected student from the list.

    print('Delete Completed Complete')


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
            delete_student()
        elif user_input == 0:
            print('Goodbye')
            sys.exit()
        else:
            print('Invalid Input: Please enter a number greater or equal to 4')


if __name__ == '__main__':
    main()
