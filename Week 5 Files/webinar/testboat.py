### testboat.py

import boat

def main():

    fishing = boat.Boat('Fishing Boat')
    fishing.show_type()
    fishing.power()

    paddling = boat.Canoe('motorless',2)
    print('Canoe capacity is',paddling.get_capacity())
    paddling.power()
    
main()
