# Robert Tessnow-Ramirez
# October 17, 2016 ©
# Assignment 5
# The Pseudocode
##  In program111.py, create instances of both new subclasses and display their attributes..
#   End Program


### program111.py

import dwelling

def main():

    home = dwelling.House('5 Ash Dr',1800,200000,True,2)
    print('For the House')
    print(home,'\n')


    ### repeat for an Apt instance
    apartment = dwelling.Apt('2557 Hidden Ln',1500,60000,1000,True)
    print('For the Apartment')
    print(apartment,'\n')

    ### repeat for a Condo instance
    condo = dwelling.Condo('123 Main st', 1100, 40000, 600, ['pool','fitness center'])
    print('For the Condo')
    print(condo)

main()