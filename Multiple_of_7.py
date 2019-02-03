#                   Robert Tessnow-Ramirez ID: 2310889
# The Pseudocode
#   Start of program
#   Get multiples of 7 from user, assign to user_input
#   Compare number to multiples of 7 by using '%' symbol to get a remainder 0
#   If true print 'your response is correct'
#   Else print 'your response is false'
#   End program


user_input = int(input('Please enter a multiple of seven '))
result = user_input % 7# This shows that if result is 0 then it is a multiple of 7
if result == 0:
    print('You are a genius, by being correct!')
else:
    print('False, please review your response')
