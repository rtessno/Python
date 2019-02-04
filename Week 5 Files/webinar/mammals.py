##### mammals.py
# The Mammal class represents a generic mammal.

class Mammal:
    
    def __init__(self, species):
        self.__species = species
    
    def show_species(self):
        print('I am a', self.__species)
    
    def make_sound(self):
        print('Grrrrr')

# The Dog class is a subclass of the Mammal class.

class Dog(Mammal):
    
    def __init__(self,breed):
        Mammal.__init__(self, 'Dog')
        self.__breed = breed

    def get_breed(self):
        return self.__breed
    
    def make_sound(self):
        print('Woof! Woof!')

# The Cat class is a subclass of the Mammal class.

class Cat(Mammal):

    def __init__(self,breed):
        Mammal.__init__(self, 'Cat')
        self.__breed = breed

    def get_breed(self):
        return self.__breed

    def make_sound(self):
        print('Meow')

class Cow(Mammal):
    def __init__(self,variety):
        Mammal.__init__(self, 'Cow')
        self.__variety = variety

    def get_variety(self):
        return self.__variety

    def make_sound(self):
        print('Mooooo')    
