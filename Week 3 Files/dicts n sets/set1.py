#### set1.py
# a set is an unordered collection of values without duplicates

def main():
    set_1 = set()                                              ## make an empty set with set function
    set_1.add(100)                                           ## add one element
    set_1.update(['Danny','Lanny',200,'Lonny'])     ## add a list to set_1 with update
    
    print(set_1)                                                ## crude output to check set                          
    for elem in set_1:                                        ## better way to a process list
        print(elem,end=' ')

    set_1.remove('Danny')                                 ## goodbye Danny

    set_1.add('Lanny')                                      ## futile, no duplicates in a set
    print('\n',set_1)

    set_2 = set('Hello world ')                           ## each chara. becomes an element
    print(len(set_2))
    for s in set_2:
        print(s, end=' ')

    
main()
