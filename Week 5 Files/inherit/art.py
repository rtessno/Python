### art.py  This is a custom module that defines class Art 
###           and two Art subclasses, Framed and Music.

class Art:
    def __init__(self,title,artist):
        self.__title = title
        self.__artist = artist

    def get_title(self):
        return self.__title

    def get_artist(self):
        return self.__artist

    ### we will override this method in subclasses to demonstrate polymorphism
    def how_experienced(self):
        print('Generally best experienced live, in person.')

class Framed(Art):
    def __init__(self,title,artist,medium):
        Art.__init__(self,title,artist)
        self.__medium = medium

    def __str__(self):
        return self.get_artist() + ' created the ' + self.__medium + ' ' + self.get_title()
    def how_experienced(self):
        print('Experienced visually. The original is best, but photos work.')

class Music(Art):
    def __init__(self,title,artist,genre):
        Art.__init__(self,title,artist)
        self.__genre = genre
    def __str__(self):
        return self.get_artist() + " created the " + self.__genre + " music " + self.get_title()
    def how_experienced(self):
        print('Experienced by ear, best at a concert, but also by recordings.')




              
