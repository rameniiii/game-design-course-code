import random
import numpy as np

class dangerousMonster:

    def __init__(self, monsterLocation =""):
        self.isthere = True
        self.total_places = ["the Temple", "the Spring", "the Beach", "the Ravine", "the Camp"]
        self.random_number_moves = 0
        self.random_number_one_four = random.randrange(5)
        self._monsterLocation = monsterLocation

    def print_warning(self):
        self.new_random_number = random.randrange(5)
        print("The monster crawls to " + str(self.total_places[self.new_random_number]))

    def set_monsterLocation(self):
        self._monsterLocation = self.total_places[self.random_number_one_four]

    def get_monsterLocation(self):
        return self._monsterLocation

        #if self.random_number_one_four == 0:
        #     return str(self.total_places[0])
        #     return str(self.total_places[1])
        # elif self.random_number_one_four == 2:
        #     return str(self.total_places[2])
        # elif self.random_number_one_four == 3:
        #    return str(self.total_places[3])
        #else:
        #    return str(self.total_places[4])
        

#if monster.moves_after_encounter == 'run' and tile == 'run':
                    #print("Today is your lucky day! I wonder what made you so intimidating...")
                    #continue
                #elif monster.moves_after_encounter == 'attack' and tile == 'temple':
                   # self.alive = False
                    #print("You are as dead as a five course meal." and tile == 'temple')
                    #continue
               # elif monster.moves_after_encounter == 'die':
                    #print("Damn son. You think you could take on the Rock?")


#What I wanted to do (but the inventory won't update with its cumulative items) is that if the player is given the option
#to fight, run, or dodge

    def moves_after_encounter(self):
        self.random_number_moves = random.randint(0,1)
        if (self.random_number_moves == 0):
            return "run"
            #"You have successfully avoided the monster!"
        elif (self.random_number_moves == 1):
            return "attack"
            #"You die!"
        else: 
            return "die"
            #"Damn son!"

    #def equip_from_Inventory(self):
        #if monster_encounter = True:

            #if "Golden Monkey Statuette" in your_Inventory:
                #monster_current_move = 'run'
            #elif "a beat up Practice Dummy" in your_Inventory:
                #monster_current_move = 'attack'
                #player_monster_choice = input("Lucky day! You remember you have the practice dummy. Now, you can either 'attack,' 'run,' or 'dodge.' Please type in your choice.")
                #if player_monster_choice = 'attack'
                    #monster_current_move = 'die'
                #elif player_monster_choice = "dodge"
                    #print("It's coming again to attack you!")
                #else:
                    #self.alive = False
            #else:
                #self.alive = False

        #else:
            #print("No monster, no worries!")
