#                   Robert Tessnow-Ramirez ID: 2310889
# The Pseudocode
#   Start of program
#   prompt user with a question that requires a numerical value, assign to
#   numerical_value
#   prompt user a question that requires a string value, assign to variable string_value
#   compare numerical value to correct response, if correct print true else print false
#   compare string value to correct response, if correct print true else print false
#   end program

correct_numerical_value = 27
correct_string_value ='The U.S. Constitution'

user_numerical_value = int(input('How many amendments to the constitution? '))
user_string_value = input('what is the supreme law of the land? ')

if user_numerical_value == 27:
    print('You are a genius!')
else:
        print('Please re-evaluate your response')

if user_string_value == 'The U.S. Constitution':
    print('You are a genius!')
else:
    print('Please evaluate your response')

                        
