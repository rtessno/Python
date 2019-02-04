### player.py

import sys

class Player:

    def __init__(self,id,health,ammo):
        self.__id = id
        self.__health = health
        self.__ammo = ammo

    def shoot(self,target,hit):
        self.__ammo -= 1
        if hit == 1:
            print(self.__id + ' shoots and hits ' + target.get_id() + '. Ammo now', self.__ammo,end='. ')
            target.set_health(target.get_health() - 1)
            if target.get_health() == 0:
                print("'",target.get_id(),"': Aargghhh. Ya got me!",sep='')
                print('\n\t\t<<<<<< GAME OVER >>>>>>>>')
                sys.exit()
            else:
                print('"',target.get_id(),': I am hit! My health now ',target.get_health(),'"',sep='')
        else:
            print(self.__id,'shoots but misses! Damn! Ammo now',self.__ammo)


    def get_id(self):
        return self.__id

    def get_ammo(self):
        return self.__ammo

    def get_health(self):
        return self.__health

    def set_health(self,health):
        self.__health = health
    
