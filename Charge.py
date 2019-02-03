#                   Robert Tessnow-Ramirez ID: 2310889
# The Pseudocode
#   Start of Program
#   Get float value of order, assign to Value
#   use if statement to decide determin if the charges is equal or greater than 100
#   if greater or equal to 100 print Value
#   use else statement to get weight from user, assign to weight
#   use if statement to determin if weight is  greater or equal to 40 to multiply by 1.09 and add the value
#   use if statement to determin if weight is greater than or equal to 20 and less than 40 to multiply by .99 and add the value
#   use if statemtnt to determin if weight is less then 20 to multiply weight times 0.89 and add the value
#   print your charges are and formatted Value
#   end program

Value = float(input('Please enter item(s) value ')) #gets user to enter Value
if Value >= 100: # determnes if Value is greater or equal to 100
    print(' Your charges are: ','$',format(Value, ',.2f'), sep='')
else:
    Weight = float(input('Please enter weight. '))
    if Weight >= 40:
        Value = Value + 1.09 * Weight
        print('Your charges are ','$', format(Value, '.2f'), sep='')
    if Weight >= 20 and Weight < 40: # determines whether weight entered is greater or equal to 20 and less then 40
        Value = Value + .99 * Weight # Value of the item is added to the product of .99 and the Weight
        print('Your charges are ','$', format(Value, '.2f'), sep='')
    if Weight < 20:
        Value = Value + 0.89 * Weight
        print('Your charges are ','$', format(Value, '.2f'), sep='')

