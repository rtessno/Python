### dictionary1.py
### a dictionary is a collection of key = value pairs
### values are accessed by their keys


def main():

    states = {'FL':'Tallahassee','GA':'Atlanta',
              'NY':'New York','CA':'Sacramento',
              'OH':'Columbus','NH':'Concord'}

    states['NY'] = 'Albany'         ### correction
    states['Hawaii'] = 'Honolulu'   ### add another pair

    print('There are',len(states),'states in the dictionary')

    print('\nHere are the states and capitals')
    for key in states:
        print('The capital of',key,'is',states[key])

    print('\nAnother way to get the states and capitals')
    for key in states:
        print('The capital of',key,'is',states.get(key))
        
    print('\nYet another way to get the states and capitals')
    ### see page 378-379 about items() method
    for key,value in states.items():
        print('The capital of',key,'is',value)

    print('\nJust the state abbreviations')
    ### the keys() method returns all keys
    for abb in states.keys():
        print(abb,end=' ')

    print('\n\nJust the state capitals')
    ### the values method returns all values
    for cap in states.values():
        print(cap,end=' ')    


main()



    
