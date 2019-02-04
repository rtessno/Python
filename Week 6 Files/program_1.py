# Robert Tessnow-Ramirez
# October 17, 2016 ©
# Assignment 6
# The Pseudocode
#   Start the Program
# Design a recursive function that prints each character of a string on its own line.
# The function should take only one argument,
# the string to be processed. The string to be processed should be entered by the user.
#   End Program


# Define main function
import re


def main():
    user_string = input("Please enter a string: ")
    while not re.match("^\w\D[a-z]*$", user_string):
        print("Error! Only letters a-z allowed! and single line strings allowed")
        user_string = input("Please enter a string: ")

    print_char(user_string)


def print_char(string):

    if string == '':
        return string

    else:
        print(string[0])
        return print_char(string[1: len(string)])


main()  # call main function
