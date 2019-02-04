#### dictionary1.py

def main():

    authors = {'Tolkien':'The Hobbit',
               'Steinbeck':'Of Mice and Men',
               'Hemingway':'For Whom the Bell Tolls',
               'Fizgerald':'The Great Gatsby'
               }

    print(authors['Tolkien'])

    for key in authors:
        print(key,'wrote',authors[key])


main()
