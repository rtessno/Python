##Robert Tessnow-Ramirez
##St. Petersburg College
## 99 Bottles of Bear © 2017
## April 25, 2017

s = "s"
beers = 99
while beers >-1:
        while beers != 1 and beers >- 1:
            print(beers," bottle",s," of beer on the wall,",beers," bottle",s," of beer.", sep='')
            beers -= 1
            if beers == -1:
                print("Go to the store, buy some more,","99 bottles of beer on the wall.")
            else:
                print("Take one down and pass it around,",beers," bottle"," of beer on the wall",sep='')
                print()
        if beers == 1:
            print(beers," bottle"," of beer on the wall,",beers," bottle",s," of beer.", sep='')
            beers -= 1
            if beers == -1:
                print("Go to the store, buy some more,","99 bottles of beer on the wall.")
            else:
                print("Take one down and pass it around,",beers," bottle"," of beer on the wall",sep='')
                print()
        if beers == 1:
            print(beers," bottle"," of beer on the wall,",beers," bottle",s," of beer.", sep='')
            beers -= 1

# // C++ version of 99 Bottles of beer
# // programmer: Tim Robinson timtroyr@ionet.net
# // Corrections by Johannes Tevessen

# #include <iostream>
# using namespace std;
#
# int main()
#     {
#     int bottles = 99;
#     while ( bottles > 0 )
#         {
#         cout << bottles << " bottle(s) of beer on the wall," << endl;
#         cout << bottles << " bottle(s) of beer." << endl;
#         cout << "Take one down, pass it around," << endl;
#         cout << --bottles << " bottle(s) of beer on the wall." << endl;
#         }
#     return 0;
#     }


