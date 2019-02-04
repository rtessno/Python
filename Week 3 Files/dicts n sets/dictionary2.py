#### dictionary2.py
# a dictionary is a data type consisting of key-value pairs

def main():
    ## dictionary films below uses film title as key and a list as a value (p374)
    ## the list contains the director, star, and genre of the film

    films = {'The Godfather' : ['Coppola','Brando','Crime Drama'],
                "Schindlers's List" : ['Spielberg','Neeson','War Drama'],
                'Casablanca' : ['Curtiz','Bogart','War Drama'],
                'Star Wars' : ['Lucas','Hamill','Science Fiction'],
                'Citizen Kane' : ['Welles','Welles','Drama'],
                'The Wizard of Oz' : ['Fleming','Garland','Fantasy'],
                'Forest Gump' : ['Zemeckis','Hanks','Comedy Drama'],
                'Chinatown' : ['Polanski','Nicholson','Suspense Drama']
             }
    print(films['Chinatown'])

    title = 'Forest Gump'
    ## list elements can be accessed by key and index
    print(films[title][1],'starred in the',films[title][2],'Forest Gump,',films[title][0],'directed.')

    show_films(films)   ## call show_films function with argument films

def show_films(movies):
    ## processing the dictionary with a for loop
    print('\nTITLE\t\t\tDIRECTOR\tSTARRING\tGENRE')
    print()
    for item in movies:
        print(item + '\t\t' + movies[item][0] +  '\t\t' + movies[item][1] + '\t\t' + movies[item][2])

main()
