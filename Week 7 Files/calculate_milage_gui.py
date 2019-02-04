# Robert Tessnow-Ramirez
# October 17, 2016 ©
# Assignment 7
# The Pseudocode
#   Start the Program

#   End Program

# Create a Python tkinter GUI for calculating mileage in miles per gallon after a road trip.
# Your GUI should enable a user to enter the gallons used and the miles driven after the drive.
# Design and layout are up to you. Clicking a button should display the mileage in mpg right in
# the GUI, not in a new popup window. You are free to add more features, but if you do, make sure
# they work.


import tkinter


class Calculate_mileage:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title('Calculate Mileage (MPG)')
        self.main_window.geometry('300x100')

        # Create four frames
        self.gallons_frame = tkinter.Frame(self.main_window)
        self.miles_frame = tkinter.Frame(self.main_window)
        self.mileage_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the gallons frame
        self.gallons_label = tkinter.Label \
            (self.gallons_frame, \
             # bg="black", fg="red",
             text='Enter the Gallons used:')

        self.gallons_entry = tkinter.Entry(self.gallons_frame, width=6)

        # Pack the gallons frame widgets
        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        # Create the widgets for the miles frame
        self.miles_label = tkinter.Label \
            (self.miles_frame, \
             
             text='Enter the Miles driven:')
        self.miles_entry = tkinter.Entry(self.miles_frame, width=6)

        # Pack the miles frame widgets
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        # Create the widgets for the mileage frame
        self.mileage_label = tkinter.Label \
            (self.mileage_frame, \
             # bg="black", fg="red",
             text='Your Mileage is')

        # Create a blank label
        self.result = tkinter.StringVar()
        self.result_label = tkinter.Label(self.mileage_frame, \
                                          textvariable=self.result)
        # Pack the mileage frame widgets
        self.mileage_label.pack(side='left')
        self.result_label.pack(side='left')

        # Create two buttons in the button frame
        self.total_button = tkinter.Button \
            (self.button_frame, \
             text='Calculate mileage', \
             bg="whitesmoke", fg="black",
             command=self.calculate_total)
        self.quit_button = tkinter.Button \
            (self.button_frame, \
             text='Quit', \
             bg="whitesmoke", fg="black",
             command=self.main_window.destroy)

        # Pack widgets in button frame, padx adds padding
        self.total_button.pack(side='left', padx=8)
        self.quit_button.pack(side='left')

        # Pack the frames
        self.gallons_frame.pack()
        self.miles_frame.pack()
        self.mileage_frame.pack()
        self.button_frame.pack(ipadx=2)

        # Add some color

        self.main_window.configure(background='darkgrey')
        self.button_frame.configure(background='darkgrey')

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Define the calculate_total function
    def calculate_total(self):
        # Get the values entered
        self.gallons = int(self.gallons_entry.get())
        self.miles = float(self.miles_entry.get())

        # Calculate mileage
        self.mileage = self.miles / self.gallons

        # Update the result_label
        self.result.set(format(self.mileage, '.2f') + ' miles per gallon')


# Create an instance of Calculate_mileage
mileage = Calculate_mileage()
