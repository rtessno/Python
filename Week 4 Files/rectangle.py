# Robert Tessnow-Ramirez
# October 15, 2016 ©
# Assignment 4
# The Pseudocode
# prompt the user to enter the length and width of a rectangle.
# create a new Rectangle instance with the dimensions entered by the user.
# to verify the above step, print both dimensions using their respective "getter" methods.
# test the area() method by printing the rectangle area accurate to two decimal places.
# test the perimeter() method by printing the rectangle perimeter accurate to two decimal places.
# change the length to 22.345 and change the width to 15.789.
# test the area() and perimeter() methods again. You should get the results shown in the sample output.
#   End Program


class Rectangle:							#The Rectangle class simulates a rectangle
    def __init__(self, length, width):		#rectangle length and width is assign to the __length and __width attribute
        self.__length = length
        self.__width = width

    def set_length(self, length):			#creates setter to modify length
        self.__length = length

    def get_length(self):					#get method returns the rectangle length
        return self.__length

    def set_width(self,width):				#creates setter to modify width
        self.__width = width

    def get_width(self):					#get method returns the rectangle width
        return self.__width

    def get_area(self):						#get method calculates and returns the rectangle area
        return self.get_width() * self.get_length()

    def get_perimeter(self):				#get method calculates and returns the rectangle perimeter
        return self.get_width() * 2 + self.get_length() * 2
