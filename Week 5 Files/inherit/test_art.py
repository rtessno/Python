### test_art.py

import art

def main():
    
    priceless = art.Framed('Mona Lisa','Leonardo da Vinci','painting')
    print(priceless)

    classic = art.Music('Clair de Lune','Claude Debussy','piano')
    print(classic)

    timeless = art.Music("Knockin' on Heaven's Door",'Bob Dylan','folk rock')
    print(timeless)

    divine = art.Art('Pieta','Michelangelo')
    print(divine.get_artist(),'made the beautiful',divine.get_title(),'sculpture')

    ### two calls of how_experienced() method
    classic.how_experienced()
    divine.how_experienced()
    priceless.how_experienced()

    ### three calls of art_info function 
    art_info(priceless)    ### works because Framed is a subclass of Art
    art_info(classic)       ### works because Music is a subclass of Art
    art_info('Hello')        ### Error. A string is not a subclass of Art
    
def art_info(opus):
    ### the isinstance function is used to detect object type
    if isinstance(opus,art.Art):
        print(opus.get_title(),end='. ')
        opus.how_experienced()
    else:
        print('Oops. That was not Art.')

    
    
main()
