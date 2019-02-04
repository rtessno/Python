# Robert Tessnow-Ramirez
# October 17, 2016 ©
# Assignment 3
# The Pseudocode
#   Start the Program
# make a dictionary for nine Tampa Bay Rays (see below). You can make up the player names. These are old.
# Use the player names as keys and a list for each value. See page 374.
# Each value list should hold the position played by the player, the batting order, and current batting average.
# When the dictionary is complete, use a for loop to display the dictionary keys and values.
# Next, use loop(s) to print the "lineup" (the dictionary in batting order).
# Duplicate the sample output for full points.
# Pull Rivera and DeJesus. Substitute Wilson as catcher and Beckham as DH (see sample output).
# Reprint the new lineup.
# SAMPLE OUTPUT
# Rays starters
#
# DeJesus ['DH', 6, 299]
# Loney ['1B', 4, 222]
# Rivera ['C', 9, 194]
# Forsythe ['2B', 5, 304]
# Souza Jr ['RF', 2, 229]
# Longoria ['3B', 3, 282]
# Cabrera ['SS', 7, 214]
# Kiermaier ['CF', 1, 240]
# Guyer ['LF', 8, 274]
#
# Today's lineup
#
# Batting 1 : CF Kiermaier ,current avg: 240
# Batting 2 : RF Souza Jr ,current avg: 229
# Batting 3 : 3B Longoria ,current avg: 282
# Batting 4 : 1B Loney ,current avg: 222
# Batting 5 : 2B Forsythe ,current avg: 304
# Batting 6 : DH DeJesus ,current avg: 299
# Batting 7 : SS Cabrera ,current avg: 214
# Batting 8 : LF Guyer ,current avg: 274
# Batting 9 : C Rivera ,current avg: 194
#
# Lineup changed
#
# Batting 1 : CF Kiermaier ,current avg: 240
# Batting 2 : RF Souza Jr ,current avg: 229
# Batting 3 : 3B Longoria ,current avg: 282
# Batting 4 : 1B Loney ,current avg: 222
# Batting 5 : 2B Forsythe ,current avg: 304
# Batting 6 : DH Beckham ,current avg: 200
# Batting 7 : SS Cabrera ,current avg: 214
# Batting 8 : LF Guyer ,current avg: 274
# Batting 9 : C Wilson ,current avg: 152
#
# PART B: Write all code in the main function:
#
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


def main():                                                     ### Define main function

    print('Rays starters\n')
    rays_players = {'Dejesus':['DH',6,299],                     ##create dictionary key and list values
                    'Loney': ['1B', 4, 222],
                    'Rivera': ['C', 9, 194],
                    'Forsythe': ['2B', 5, 304],
                    'Souza Jr': ['RF', 2, 229],
                    'Longoria': ['3B', 3, 282],
                    'Cabrera' :['SS', 7, 214],
                    'Kiermaier': ['CF', 1, 240],
                    'Guyer': ['LF', 8, 274]}
    for key,value in sorted(rays_players.items()):              ## display sorted key and value
        print(key,value)

    print('\nToday\'s lineup\n')

    for key, value in sorted(rays_players.items(), key=lambda function: function[1][1]):##print key and value in correct batting order
        
        print('Batting ', value[1], ': ', value[0], ' ', key, ' ,current avg: ', value[2], sep='')
    print()                                                     ## creates an empty line

    print('Lineup changed\n')

    substitute = {'Wilson':['C', 9, 152], 'Beckham': ['DH', 6, 299]} # create substitute dictionary
    del rays_players['Dejesus']                                      # remove element from rays_player dictionary
    del rays_players['Rivera']                                       # remove element from rays_player dictionary
    rays_players.update(substitute)                                  # update rays_player dictionary to include substitute dictionary
    for key, value in sorted(rays_players.items(),
                             key=lambda function: function[1][1]):  ##print key and value in correct batting order

        print('Batting ', value[1], ': ', value[0], ' ', key, ' ,current avg: ', value[2], sep='')
    print()

    integer_set = set()                                         ## create empty set
    i = 0
    while i <= 10:              
        random_num = random.randint(10, 30)                      ## add random numbers to set
        integer_set.add(random_num)
        i += 1
    for elements_in_set in integer_set:                         ##iterate through set to print out elements
        print(elements_in_set, '**', sep='', end='')

    
        
        even_elements = 0
        odd_elements = 0
    for even_odd_elements_in_set in integer_set:                ## for loop to process loop and find even and odd integers
        if even_odd_elements_in_set % 2 == 0:
            even_elements += 1
        else:
            odd_elements += 1
    print('\nSet has', even_elements, 'even numbers and', odd_elements, 'odd numbers')

main()                                                          # call main function
