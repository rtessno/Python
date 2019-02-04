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
#   End Program
import random
def main():  ### Define main function

    print('Rays starters\n')
    rays_players = {'Dejesus': ['DH', 6, 299],  ##create dictionary key and list values
                    'Loney': ['1B', 4, 222],
                    'Rivera': ['C', 9, 194],
                    'Forsythe': ['2B', 5, 304],
                    'Souza Jr': ['RF', 2, 229],
                    'Longoria': ['3B', 3, 282],
                    'Cabrera': ['SS', 7, 214],
                    'Kiermaier': ['CF', 1, 240],
                    'Guyer': ['LF', 8, 274]}
    for player_name, player_attribute in sorted(rays_players.items()):  ## display sorted key and value
        print(player_name, player_attribute)
    #################################################################################################
                                                                        #uses nested list
    print('\nToday\'s lineup\n')
    # sorted_list = [(key,value) for value,key in sorted([(value[1],key) for key,value in rays_players.items()])]
    # for key, value in sorted_list:
    #     print('Batting ', value,': ', rays_players[key][0], key,',current avg',rays_players[key][2])
    #################################################################################################
    # Here is a method that works...
    # start a for loop that will run from 1 to 9 inclusive
    # inside that loop, start another loop that uses the items method
    #  (like line 4 in the code atop page 379)
    # in that loop, test to see if the batting order matches the control variable of the outer loop
    # if it does, print
    ctrl_vari = 0
    for i in range(9):
        ctrl_vari += 1
        for key, value in rays_players.items():
            if rays_players[key][1] == ctrl_vari:
                print('Batting ', rays_players[key][1],': ', rays_players[key][0], key,',current avg',rays_players[key][2])
    #################################################################################################
    print()                                                             ## creates an empty line
    print('Lineup changed\n')
    substitute = {'Wilson': ['C', 9, 152], 'Beckham': ['DH', 6, 299]}   # create substitute dictionary
    del rays_players['Dejesus']                                         # remove element from rays_player dictionary
    del rays_players['Rivera']                                          # remove element from rays_player dictionary
    rays_players.update(substitute)                                     # update rays_player dictionary to include substitute dictionary
    #################################################################################################
    ctrl_vari = 0
    for i in range(9):
        ctrl_vari += 1
        for key, value in rays_players.items():
            if rays_players[key][1] == ctrl_vari:
                print('Batting ', rays_players[key][1],': ', rays_players[key][0], key,',current avg',rays_players[key][2])
    #################################################################################################

    # sorted_list = [(key,value) for value,key in sorted([(value[1],key) for key,value in rays_players.items()])]
    # for key, value in sorted_list:

    #     print('Batting ', value,': ', rays_players[key][0], key,',current avg',rays_players[key][2])
    #################################################################################################
main()  # call main function
