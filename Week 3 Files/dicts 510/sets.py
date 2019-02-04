### sets.py
### set: an UNORDERED collection of values with NO DUPLICATES

def main():

    ### use the set() function and pass an iterable sequence
    set1 = set([8, 13, 15, 5, 13, 6])   ### use a list

    print('Size of set1 is',len(set1))  ### 5 not 6!!
    print('set1, crude dump:',set1)      ### only to test set

    print('Here is set1.')
    ### let's total the set, too
    total = 0                           ### accumulator
    for n in set1:
        print(n,end=' ')
        total += n

    print('\nThe set1 total is',total)

    ### add one more element with add method
    set1.add(3)
    ### add several more elements with update method
    set1.update('XYZ')
    ### each character in string is added as an element

    print('Here is set1 now.')
    for n in set1:
        print(n,end=' ')    

    set2 = set('abcde')                 ### a new set
    print('\nset2 contains',len(set2),'elements')

    set1.update(set2)                   ### add set2 to set1
    
    print('Here is set1 now.')
    for n in set1:
        print(n,end=' ')  
    
main()



    
