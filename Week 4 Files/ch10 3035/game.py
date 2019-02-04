### game.py

import player, random, sys

def main():
    ## both players start with health = 3 and ammo = 5
    warrior = player.Player(1,3,5)  ## you are player with id = 1
    enemy = player.Player(2,3,5)

    while(True): ## game loop runs until sys.exit()
        hit_enemy = random.randint(0,1)
        hit_me = random.randint(0,1)
        my_ammo = warrior.get_ammo()
        enemy_ammo = enemy.get_ammo()
        
        if my_ammo > 0:
            warrior.shoot(hit_enemy,hit_me)
        if enemy_ammo > 0:
            enemy.shoot(hit_me,hit_enemy)
        
        if my_ammo == 0 and enemy_ammo == 0:
            print('Both players out of ammo. Game over')
            print('Player',warrior.get_id(),'final health',warrior.get_health())
            print('Player',enemy.get_id(),'final health',enemy.get_health())
            sys.exit()

main()
