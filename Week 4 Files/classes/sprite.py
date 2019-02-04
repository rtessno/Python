### sprite.py

class Sprite:
    def __init__(self,name,weapon,health):
        self.__name = name
        self.__weapon = weapon
        self.__health = health
        
    def got_hit(self):
        self.__health -= 1        
        status = "I've been hit!, says " + self.__name
        if self.__health == 0:
            status += '. I am done for...arghh'
        else:
            status += '. My health now ' + str(self.__health)
        print(status)

    def get_health(self):
        return self.__health

    def get_name(self):
        return self.__name
    
    def __str__(self):
        s = 'Character name: ' + self.__name
        s += ' weapon is ' + self.__weapon
        s += ' health is ' + str(self.__health)
        return s

    ## added this shoot method after lesson
    def shoot(self,victim):
        print(self.__name + ' shoots ' + victim.get_name())
        victim.got_hit()
        if victim.get_health() == 0:
            print(victim.__name + ' was killed.')
            print('Ha ha, got ya, gloats ' + self.__name)

    
