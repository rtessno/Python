#### dictionary1.py
# a dictionary is a data type consisting of key : value pairs

def main():

    animals = { 'mosquito' : 'insect', 'dog' : 'canine', 'cat' : 'feline', 'dolphin' : 'mammal' }
    
    animals['grouper'] = 'fish'  ### add one more

    ## what is a dolphin?
    print('A dolphin is a',animals['dolphin'])

    print('\nHere is the entire dictionary')

    ## loop through entire dictionary. NOTE: order not maintained
    for key in animals:
        print(key,animals[key])
    
    ## remove the cat
    del animals['cat']
    
    print('\nAfter removing the cat')
    ## loop through dictionary again
    for key in animals:
        print(key,animals[key])    

main()
