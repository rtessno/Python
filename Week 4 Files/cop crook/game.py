### game.py

import player, random, sys

def main():
    ## both players start with health = 3 and ammo = 3
    cop = player.Player("Cop",3,5)  
    crook = player.Player("Crook",3,5)

    while(True): ## game loop runs until sys.exit()
        hit_cop = random.randint(0,1)   ## 1 will be a hit
        hit_crook = random.randint(0,1)
        cop_ammo = cop.get_ammo()
        crook_ammo = crook.get_ammo()
        
        if cop_ammo > 0:
            cop.shoot(crook,hit_crook)
        else:
            print('Click.Click."',cop.get_id(),'": Uh oh. I am out of ammo!',sep='')    
        if crook_ammo > 0:
            crook.shoot(cop,hit_cop)
        else:
            print('Click.Click."',crook.get_id(),'": Uh oh. I am out of ammo!',sep='')    
        if cop_ammo == 0 and crook_ammo == 0:
            print('Both players out of ammo.')
            print(cop.get_id(),'final health',cop.get_health())
            print(crook.get_id(),'final health',crook.get_health())
            print('\n\t\t<<<<<< GAME OVER >>>>>>>>')
            sys.exit()

main()
