### make_list.py

import random                           ### needed for randint method

def main():
    mylist = []                         ### empty list
    for n in range(6):                  ### loop will cycle 6 times
        rand = random.randint(10,20)    ### integer from 10-20
        mylist.append(rand)             ### add rand to list

    print(mylist)                       ### crude dump of list

    myfile = open('data.txt','w')       ###open a file for writing    

    for num in mylist:                  ### better way to see list
        print(num,end=' ')              ### end suppresses newline (p 65)
        ### we write elements to file
        myfile.write(str(num) + '\n')   ### must convert number to string

    myfile.close()                      ### done with file for now

    print()                             ### needed to end the line in loop
    listing()                           ### execute the listing function

def listing():
    data = open('data.txt','r')         ### open file for reading
    total = 0                           ### accumulator for adding list elements
    line = data.readline()              ### read a line; the PRIMING READ
    while line != '':
        num = int(line)                 ### convert string to int
        total += num                    ### accumulate the total
        
        ### print as ints in columns 8 characters wide
        print(num,format(num ** 2,'8.2f'),format(num ** 3,'8.2f'))
        line = data.readline()          ### read the next line in the file

    data.close()                        ### close file
    print('The list total was',total)


main()
