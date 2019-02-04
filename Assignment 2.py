#Robert Tessnow-Ramirez
#October 17, 2016 ©
#Assignment 2
# The Pseudocode
## prompt the user to enter his/her full name (see sample output).
## display the number of characters in the full name.
## use a while loop to print the name backwards.
## use slicing to make a new string in the format lastname, firstname. Print the new string.
## use a loop and counter variables to determine the number of upper and lower case letters in the name. Print both totals.
## assign "You have to be vewy, vewy twicky to twap a wascally wabbit" to another new string.
## use a method to correct Elmer Fudd's bad spelling above. Print the corrected string.



def main():                                         ## Define main function    
    user_fullname = input('Enter your full name ')# prompts user to enter his/her name
    index = 0                                    #char. Index initialized to 0    
    while index < len(user_fullname):            #process users name the full length
        index += 1                               #accumulate length of name
    print('Your name consists of',index, 'characters')                                 #prints the number of charaters in name
    reverse_name = ''                            #create variable reverse_name assign empty string
    i = len(user_fullname)                       #assign i the length of user_fullname
    while i >0:                                  #process the length of user_fullname backwards
        reverse_name += user_fullname[i-1]       #decrement i by 1
        i -= 1
    print('backwards your name is',reverse_name) #print reverse name

    
   
    space = user_fullname.index(' ')             #assign variable space the index that the space holds
    formated_name = user_fullname[space:] + ', ' + user_fullname[:space]# formats the name Aplhabetically

    print('Alphabetically, your name is',formated_name)# prints names in order
    
  

    


   
    uppercase = 0                               #initialize accumulator
    lowercase = 0                               #initialize accumulator
    for i in user_fullname:                     #use for loop to process through user name
        if i.isupper():                         #process name to find upper case letters
            uppercase += 1                      #if uppercase add 1 to accumulator
        else:
            lowercase += 1                      #if lower case add 1 to accumulator
    print('Your name has',uppercase,'upper case letters and',lowercase,'lower case letters')
    incorrect_fudd_str =  "You have to be vewy, vewy twicky to twap a wascally wabbit"   
    correct_fudd(incorrect_fudd_str)
   
def correct_fudd(incorrect_fudd_str):           #defines correct_fudd method takes incorrect string as argument
     fix_fudd = incorrect_fudd_str.replace('w','r')                    #replace all w's with r's
     print(fix_fudd)
main()#call main function
