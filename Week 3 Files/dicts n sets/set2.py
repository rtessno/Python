#### set2.py
# a set is an unordered collection of values without duplicates

def main():

    ## a set could hold acceptable answers for a question
    
    ## make a set of acceptable answers
    ans = set(['Barack','Obama','Barack Obama','Mr Obama','obama'])

    response = input('Who is the USA commander in chief? ')
    if response in ans:
        print('Correct. President Obama is the commander in chief.')
    else:
        print('Sorry. That is not correct.')
        

    
main()
