# Robert Tessnow-Ramirez
# October 17, 2016 ©
# Assignment 3 b
# The Pseudocode
#   Start the Program
# PART B: Write all code in the main function:
# create an empty set.
# use a loop to add 10 random integers, all from 10 to 30 inclusive, to the set.
# use another loop to process the set:
# display all elements of the set on one line separated by ** (see sample outputs).
# count how many elements are even and how many elements are odd.
# display the counts.
# SAMPLE OUTPUT
# 12**16**17**18**20**21**22**23**24**28**
# Set has 7 even numbers and 3 odd numbers
#
# SAMPLE OUTPUT
# 10**12**14**16**18**20**21**22**25**26**
# Set has 8 even numbers and 2 odd numbers
#   End Program
import random
def main():  ### Define main function
    integer_set = []                     ## create empty set

    #integer_set = [random.randint(10,30) for i in range(10)]
    for i in range(10):
        integer_set.append(random.randint(10,30))

    for elements_in_set in integer_set:      ##iterate through set to print out elements
        print(elements_in_set, '**', sep='', end='')
        even_elements = 0
        odd_elements = 0
    for even_odd_elements_in_set in integer_set:  ## for loop to process loop and find even and odd integers
        if even_odd_elements_in_set % 2 == 0:
            even_elements += 1
        else:
            odd_elements += 1
    print('\nSet has', even_elements, 'even numbers and', odd_elements, 'odd numbers')

main()  # call main function
