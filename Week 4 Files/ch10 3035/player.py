### player.py

import sys

class Player:

    def __init__(self,id,health,ammo):
        self.__id = id
        self.__health = health
        self.__ammo = ammo

    def shoot(self,hit,hitme):
        if self.__ammo > 0:
            self.__ammo -= 1
            print('Player',self.__id,'shoots ammo now',self.__ammo)
            if hit == 1:
                print('Player',self.__id,'scored a hit!')
        else:
            print('Click. Player',self.__id,'out of ammo!')
        if hitme == 1:
            self.__health -= 1
            print('Player',self.__id,"I'm hit! Health now",self.__health)
            if self.__health == 0:
                print('Player',self.__id,'argghhh. Ya got me! Game over')
                sys.exit()

    def get_id(self):
        return self.__id

    def get_ammo(self):
        return self.__ammo

    def get_health(self):
        return self.__health
    
