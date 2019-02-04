### spritetest.py

### import the sprite module
import sprite

def main():
    enemy = sprite.Sprite('Bandit','AK-47',5)
    print(enemy)

    friend = sprite.Sprite('Zombie','stick',0)
    print(friend)

    ## somebody shoots Bandit
    enemy.got_hit()

    ## added after lesson to test new shoot method
    print('\nZombie now has a bead on Bandit...\n')
    friend.shoot(enemy)
    friend.shoot(enemy)    
    friend.shoot(enemy)
    friend.shoot(enemy)

    
main()
