#                   Robert Tessnow-Ramirez 2310889
# The Pseudocode
#   Start of program
#   Get degrees Fahrenheit, assign to variable named F
#   Change F fom string to interger.
#   Use formula (F-32)*(5/9), assign variable to name C
#   Change C to float and format C to 3 decimal places using ,.3f, Assign variable to C
#   Print C
#   End program

Fahrenheit = input('Please input degrees Fahrenheit:')
Celcius = (int(Fahrenheit)-32)*(5/9)       # the int() changes F from a String statement to and interger.
Celcius = float(format(Celcius, ',.3f'))# The float() changes C to a decimal number and then format() makes it to 3 decimal places.
print('If', Fahrenheit ,' degrees Fahrenheit then' ,Celcius , 'degrees Celcius.')
