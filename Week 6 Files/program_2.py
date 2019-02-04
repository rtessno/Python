# Robert Tessnow-Ramirez
# October 17, 2016 ©
# Assignment 6
# The Pseudocode
# Design a recursive function that returns the sum of a range in a list of integers.
#  The recursive function should take three arguments;
# the list name, the start index of the range, and the end index of the range.
#  To test your function, make a ten element list of small random integers,
# all from 1 to 20 inclusive. Duplicates are okay.
# Prompt the user to enter the start and end index for the range.
# NOTE: The user could enter bad index values. Assume this does not happen.
#   End Program

import random


def main():  ### Define main function

    numbers = []  # creates an empty list

    for i in range(10):
        numbers.append(random.randint(1, 20))
    print(numbers)
    start_index = int(input('Enter start index '))
    end_index = int(input('Enter end index '))

    my_sum = range_sum(numbers,start_index, end_index)

    # Display the sum.
    print('The sum of items',start_index, 'through',end_index,'is', my_sum)


def range_sum(num_list, start, end):
    
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)


main()  # call main function
