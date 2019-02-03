#                   Robert Tessnow-Ramirez 2310889
# The Pseudocode
#       Start of program.
#       Get quantity of Item(s), assign to Q as int() 
#       Get price of Item(S), assign to P as float()
#       Use Addition to add Q and P for amount due, assign to amount_due
#       If amount_due is greater or equal to 1000 format it to use a comma seperator
#       print out quantity Q
#       print out unit price P
#       print out amount_due and include sep=() function to remove space between amount_due and $ symbol
#       End program

Quantity = int(input('Enter quantity:'))           # user enters quatity and is made an interger
Price = float(input('Enter price:'))            # user enters price and is made an deimal
amount_due = float(format(Quantity + Price, '.2f'))    # amount due is calculat as decimal by adding quantity and price
amount_due >= 1000                          # if amount due is greater than or equal to 1000 
amount_due = format(Quantity + Price, ',.2f')          # it is fomatted to display with a comma seperator
print('Enter the quantity:', Quantity)
print('Enter the unit price:', Price)
print('Amount due is $',amount_due, sep='') # the sep() funtion removes the space between the dollar sign and the amount_due
  
