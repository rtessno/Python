#### checkout.py

import tkinter

class Cashier:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title('Cashier')

        # Create four frames
        self.qty_frame = tkinter.Frame(self.main_window)
        self.price_frame = tkinter.Frame(self.main_window)
        self.total_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the qty frame
        self.qty_label = tkinter.Label \
                             (self.qty_frame, \
                              #bg="yellow", fg="red",                             
                              text = 'Enter the quantity:')
                                     
        self.qty_entry = tkinter.Entry(self.qty_frame, width = 6)

        # Pack the qty frame widgets
        self.qty_label.pack(side = 'left')
        self.qty_entry.pack(side = 'left')

        # Create the widgets for the price frame
        self.price_label = tkinter.Label \
                           (self.price_frame, \
                            #bg="yellow", fg="red",                            
                            text = 'Enter the unit price:')
        self.price_entry = tkinter.Entry(self.price_frame, width = 6)                                 

        # Pack the price frame widgets
        self.price_label.pack(side ='left')
        self.price_entry.pack(side = 'left')
        
        # Create the widgets for the total frame
        self.total_label = tkinter.Label \
                            (self.total_frame, \
                             #bg="yellow", fg="red",
                             text = 'Please pay')
                             
        
        # Create a blank label 
        self.result = tkinter.StringVar()
        self.result_label = tkinter.Label(self.total_frame, \
                                       textvariable= self.result)
        # Pack the total frame widgets
        self.total_label.pack(side = 'left')
        self.result_label.pack(side = 'left')
        
        # Create two buttons in the button frame
        self.total_button = tkinter.Button \
                          (self.button_frame, \
                           text = 'Calculate total', \
                           bg="blue", fg="yellow",
                           command = self.calculate_total)
        self.quit_button = tkinter.Button \
                           (self.button_frame, \
                            text = 'Quit', \
                            bg="blue", fg="yellow",                            
                            command = self.main_window.destroy)
              
        # Pack widgets in button frame, padx adds padding
        self.total_button.pack(side='left', padx=8)
        self.quit_button.pack(side='left')
                
        # Pack the frames
        self.qty_frame.pack()
        self.price_frame.pack()
        self.total_frame.pack()
        self.button_frame.pack(ipadx=2)

        # Add some color

        self.main_window.configure(background = 'green')
        self.button_frame.configure(background = 'green')
        
        # Enter the tkinter main loop
        tkinter.mainloop()

    # Define the calculate_total function
    def calculate_total(self):
        # Get the values entered
        self.qty = int(self.qty_entry.get())
        self.price = float(self.price_entry.get())

        # Calculate total
        self.total = self.qty * self.price

        # Update the result_label
        self.result.set(format(self.total,'.2f'))

# Create an instance of Cashier
pay = Cashier()


