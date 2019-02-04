##### boat.py
# a boat class and its subclasses.

class Boat:
    
    def __init__(self, boat_type):
        self.__boat_type = boat_type
    
    def show_type(self):
        print('This is a', self.__boat_type)
    
    def power(self):
        print('Moves somehow in water')

# The Canoe class is a subclass of the Boat class.

class Canoe(Boat):
    
    def __init__(self,boat_type,capacity):
        Boat.__init__(self, 'canoe')
        self.__capacity = capacity

    def get_capacity(self):
        return self.__capacity
    
    def power(self):
        print('Powered by human muscle')

