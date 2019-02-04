### rays2.py
### it's almost baseball time
### unpickle the file

import pickle

def main():

    rays_file = open('rays.dat','rb')       # open file in binary mode for reading
    
    rays = pickle.load(rays_file)           # unpickle the file back to a dictionary

    rays_file.close()

    print('Here is the rays data retrieved from file')
    for key in rays:
        # same syntax as used in rays1.py
        print(key,rays[key][0],'could hit',rays[key][1],'home runs')    

    print(rays.get('Longoria')[0])

    print('Well, I can dream, right?')

    
main()

