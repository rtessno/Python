#### dictionary2.py

def main():

    grades = {'Denny':[80,90,85],
              'Lenny':[78,95,81],
              'Penny':[88,65,84],
              'Benny':[90,75,87],
              'Kenny':[71,100,82]
             }

##    print('On test 3, Penny got',grades['Penny'][2])

    for key in grades:
        print(key,' test scores:',grades[key][0],',',grades[key][1],',',grades[key][2],sep='')

##    benny = grades['Benny']
##    print(benny)
    
main()
