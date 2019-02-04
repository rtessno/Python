#Robert Tessnow-Ramirez
#October 10, 2016 ©
#Assignment 1
# The Pseudocode
#   Start the Program
#   in main, generate a random integer that is greater than 5 and less than 13.
#   print this number on its own line.
#   use a loop to append to the list a number of elements equal to the random
#   integer argument. All new list elements must be random integers ranging from 1
#   to 100, inclusive. Duplicates are okay.
#   Return the list to main
#   back in main, catch the returned list and sort it.
#   finally, use a for loop to display the sorted list elements, all on one line,
#   separated by single spaces.
#   End Program

import random

def makelist(rand):                     ### defines the makelist function with rand as its sole argument
    mylist = []                         ### empty list
    for n in range(rand):               ### loop will cycle number of times equal to the random integer
        rand = random.randint(1,100)    ### creates integer from 10-20 each loop 
        mylist.append(rand)             ### adds each rand to list
    return mylist                       ### retruns mylist to the main function


def main():                                       ### Define main function
    random_integer = random.randint(6,12)         ### creates a random number greater than 5 & less than 13
    print('List size will be',random_integer)     ### prints random generated on a single line
    my_list = makelist(random_integer)            ### calls from main the makelist function passing random_integer; catches return mylist and assigns it to varibale my_list 
    print('Here is the sorted list:')    ### prints sting on a single line
    my_list.sort()                       ### sorts mylist    
    for i in my_list:                    ### uses a for loop to iterated each element is my_list and prints them on one line seperated my a single space
        print(i,'',end = '')
    

    
main()
