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


import rectangle
def main():  ### Define main function

    length = float(input('Enter the length '))			#prompts user to enter rectangle length
    width = float(input('Enter the width '))			#prompts user to enter rectangle width


    my_rectangle = rectangle.Rectangle(length,width)	#creats a rectangle object

    print('Length:', my_rectangle.get_length())
    print('Width:',  my_rectangle.get_width())
    print('Rectangle area is','%.2f' % my_rectangle.get_area())
    print('Rectangle perimeters is','%.2f' % my_rectangle.get_perimeter())

    my_rectangle.set_length(22.345)						#sets rectangle length to new value
    my_rectangle.set_width(15.789)						#modifys current rectangle width and sets rectangle width to new value

    print('Changed rectangle area is','%.2f' % my_rectangle.get_area())
    print('Changed rectangle perimeter is','%.2f' % my_rectangle.get_perimeter())



main()  # call main function
