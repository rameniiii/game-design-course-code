
import numpy as np
from islandTiles import stuffonisland as island
from dangerousMonster import dangerousMonster as monster

class GameController:

    #I've used a dictionary here to access the classes above by their names. This is called a map, and common in coding.
    island_map = {"temple": island.temple, 
                "spring": island.spring, 
                "beach": island.beach, 
                "ravine": island.ravine, 
                "camp": island.camp}
    
    def __init__(self):
        self.alive = True
        self.days = 0
        self.inventory = []
        self.where_you_are = ""


    def print_your_inventory(self):
        for item in self.inventory:
            print(item)

    def play(self):
        while(self.alive):
            if self.days == 0:
                print("You have washed up on a Deserted Island! You must search the island for Food and Water to survive until rescue...")
            print("Days on the deserted island: "+str(self.days))
            
            #Our code to search the Island goes here
            tile = self.island_map[input("Where would you like to search today? (temple, spring, beach, ravine, camp): ")]
            tile.enterTile()
            loot, encounter = tile.search()

            m = monster()
            m.print_warning()
            tile.yourLocation()

            if m.get_monsterLocation() == tile.name:
                print("!!!!You encountered the monster!!!!")
                if "Golden Monkey Statuette" in self.inventory:
                    print("You have successfully avoided the monster!")
                elif "a beat up Practice Dummy" in self.inventory:
                    player_to_monster = input("Lucky day! You remember you have the practice dummy. Now, you can either 'attack,' 'run,' or 'dodge.' Please type in your choice.")
                    if player_to_monster == 'attack':
                        print("Damn son!")
                        self.inventory.append("Monster Heart")
                    elif player_to_monster == 'run':
                        print("You are as dead as a five course meal!")
                        self.alive = False
                    else:
                        print()
                        
                else:
                    print()
                    

                        
            else: 
                print("No monster was found there...phew!")
                print(m.get_monsterLocation())

            if encounter == "Crocodile":
                self.alive = False
                print("You are eaten by a Crocodile")
                continue
            elif encounter == "Crumbling Cliffs":
                self.alive = False
                print("The cliffs below you crumble and you fall to your death")
                continue
            
            if encounter == None:
                print("Your search yields nothing...")
            else:
                if loot != None:
                    print("You encounter "+str(encounter)+" and find "+str(loot))
                    self.inventory.append(loot)
                else:
                    print("You encounter "+str(encounter)+" but find nothing...")
                
            tile.leaveTile()
                
            #This is the start of our player input section. We'll modify this code to make the gameplay fun.
            view_inventory = input("Do you wish to look at your inventory? Type in 'yes' or 'no' ")
           
            if view_inventory == 'yes':
                self.print_your_inventory()
            else:
                print("Alright. Moving on.")

            decision = input("Keep searching the Deserted Island? (Y/N) Type 'quit' if you wish to exit the game.")
            

            if decision == 'quit':
                break
            elif decision == 'Y':
                print("Good choice, maybe you'll survive another day.")
            elif decision == 'N':
                print("Too bad! You're stuck here... Gotta keep searching.")
            else:
                print("I didn't understand. Maybe you've been stuck on this Island for too long...")
            self.days += 1
        else:
            print("Game over. You survived for "+str(self.days)+" days.")
