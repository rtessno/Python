#### dwelling.py
# defines classes Dwelling, House, Apt, and Condo

class Dwelling:
    def __init__(self,address,area,price):
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
    def __init__(self,address,area,price,detached,storeys):
        Dwelling.__init__(self,address,area,price)
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
