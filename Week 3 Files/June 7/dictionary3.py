#### dictionary1.py

def main():

    authors = {'Tolkien':'The Hobbit',
               'Steinbeck':'Of Mice and Men',
               'Hemingway':'For Whom the Bell Tolls',
               'Fizgerald':'The Great Gatsby'
               }

    authlist = []
    for key in authors:
        authlist.append(key)

    authlist.sort()

    for auth in authlist:
        print(auth,'wrote',authors[auth])

        


main()
