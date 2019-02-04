# Robert Tessnow-Ramirez
# October 17, 2016 ©
# Assignment 5
# The Pseudocode
#   Start the Program
# Class Apt:
#
# inherits from Dwelling and requires two more attributes:
# rent, a numeric attribute for monthly rent.
# terrace, a boolean attribute that is True for an apartment that has a terrace or balcony.
# requires a str method to display the status of an Apt instance (all attributes). Code as you see fit.
# Class Condo:
#
# also inherits from Dwelling and requires two additional attributes:
# mtce, a numeric attribute for the monthly maintenance.
# amenities, a string attribute listing Condo amenities such as pool, gym, etc.
# also requires a str method to display the status of a Condo instance (all attributes). Again, code as you wish.
#   End Program

#### dwelling.py
# defines classes Dwelling, House, Apt, and Condo

class Dwelling:
    def __init__(self, address, area, price):
        self.__address = address
        self.__area = area
        self.__price = price

    def get_address(self):
        return self.__address

    def get_area(self):
        return self.__area

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return self.__address + ', ' + str(self.__area) + ' sq ft, $' + str(self.__price)


class House(Dwelling):
    def __init__(self, address, area, price, detached, storeys):
        Dwelling.__init__(self, address, area, price)
        self.__detached = detached
        self.__storeys = storeys

    def get_detached(self):
        return self.__detached

    def get_storeys(self):
        return self.__storeys

    def __str__(self):
        s = Dwelling.__str__(self)
        s += '\n' + 'Detached:' + str(self.__detached) + ', storeys:' + str(self.__storeys)
        return s


####################### Complete these class definitions here
##class Apt
##
##class Condo
class Apt(Dwelling):
    def __init__(self,address,area,price,rent,terrace):
        Dwelling.__init__(self,address,area,price)
        self.__rent = rent
        self.__terrace = terrace

    def __str__(self):
        string = Dwelling.__str__(self)
        string += '\n' + 'rent: $' + str(self.__rent) + ', terrace: ' + str(self.__terrace)
        return string

class Condo(Dwelling):
    def __init__(self,address,area,price,mtce,amenities):
        Dwelling.__init__(self,address,area,price)
        self.__mtce = mtce
        self.__amenities = ','.join(amenities)

    def __str__(self):
        s = Dwelling.__str__(self)
        s += '\n' + 'mtce: $' + str(self.__mtce) + ', amenities: ' + str(self.__amenities)
        return s



