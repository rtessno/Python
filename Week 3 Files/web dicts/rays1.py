### rays1.py
### it's almost baseball time

import pickle

def main():
    ### dictionary with player names as keys and lists as values
    some_rays = {'Loney':['1B',24],'Longoria':['3B',32],'Mahtook':['CF',38]}

    for key in some_rays:
        # note syntax here is also shown on page 374 in text
        print(key,some_rays[key][0],'could hit',some_rays[key][1],'home runs')

    rays_file = open('rays.dat','wb')       # open file in binary mode for writing
    
    pickle.dump(some_rays,rays_file)        # serialize the dictionary in rays.dat

    rays_file.close()                       # close the file
    print('File was pickled')

main()

