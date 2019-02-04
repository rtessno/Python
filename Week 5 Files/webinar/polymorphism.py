##### polymorphism.py
# This program demonstrates polymorphism.

import mammals

def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object, and a Cow object.
    mammal = mammals.Mammal('generic mammal')
    dog = mammals.Dog('beagle')
    cat = mammals.Cat('siamese')
    cow = mammals.Cow('holstein')

    print('The dog breed is',dog.get_breed())
    print('The cow is a',cow.get_variety())

    # Display information about each one.
    print('Mammals and the sounds they make.')
    print('--------------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    print()
    show_mammal_info(cow)
    print()
    show_mammal_info('Hello')    
    
# The show_mammal_info function accepts an object
# as an argument, and calls its show_species and
# make_sound methods,IF APPLICABLE by using isinstance.

def show_mammal_info(creature):
    if isinstance(creature, mammals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('That is not a Mammal!')

# Call the main function.
main()
