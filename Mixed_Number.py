#                   Robert Tessnow-Ramirez ID: 2310889
# The Pseudocode
#   Start program.
#   Get Numerator from user, assign interger value to variable Numerator
#   Get Denominator from user, asign interger value to variable Denominator
#   Get whole_number by dividing the Numerator by Denominator using // to get an interger
#       and assign to variable whole_number
#   Get the fraction_numberator by using the remainder symbol '%', assign to fraction_numerator
#   print the numerator is numerator
#   print the denominator is denominator
#   print the mixed number is whole number 'space' fraction_numberator '/' and denominator followed by a item seperator.

Numerator = int(input('Please enter numerator: '))
Denominator = int(input('Please enter denominator: '))
whole_number = int(Numerator//Denominator)  #this gets the whole number interger for the mixed number
fraction_numerator = Numerator%Denominator  # this gets the numerator for the mixed number fraction; the remainder
print('The numerator is:', Numerator)
print('The denominator is:', Denominator)
print('The mixed number is ', whole_number ,' ', fraction_numerator,'/',Denominator,sep='')
