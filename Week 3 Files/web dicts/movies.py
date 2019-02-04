### movies.py
### A dictionary of movies by genre
### A dictionary is a collection of key : value pairs

def main():
    # next, make the dictionary
    movies = {'scifi':'Star Wars','drama':'Gone With The Wind','western':'Unforgiven',
              'crime':'The Godfather','romance':'Casablanca','action':'Die Hard'}

    print('A popular crime movie:',movies['crime'])     # use key to retrieve value
    print('Is Blade Runner the popular scifi movie?','Blade Runner' in movies)

    movies['comedy'] = 'Dumb and Dumber'                # add another to the dictionary
    movies['fantasy'] = 'Lord of the Rings'             # add another
    movies['scifi'] = 'Blade Runner'                    # change scifi movie

    print('\nHere are the movies by genre') 
    for genre in movies:
        print(genre,':',movies[genre])                  # using the key inside []

    print('\nHere are the movies by genre accessed another way') 
    for genre,movie in movies.items():                  # the items() method, p377
        print(genre,movie)

    print('\nHere are some good movies')
    for movie in movies.values():                       # the values() method, p377
        print(movie)

main()
