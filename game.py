from random import randint
import math
from time import sleep

game = True


horse_amount = 4
max_stat_total = 8

horses = []

horse_names = [
    "Horse Meat",
    "Brochowski",
    "Lilypad",
    "Pikachu",
    "Dumbface",
    "Horseyface",
    "Sally Nally",
    "Cat",
    "Fluff ball",
    "STUPID IDIOT"
]

def clamp(n,lowest,highest):
    return max(lowest,min(n,highest))

class horse:
    def __init__(self,name,speed,agility) -> None:
        
        self.name = name

        self.speed = speed
        self.agility = agility

        self.spaces_moved = 0

    def gallop(self):
        roll = randint(1,6)
        agility_roll = randint(1,self.agility) + 2

        multiplier = 1

        if agility_roll < roll:
            multiplier = -1
            
        final_move = self.speed * multiplier
        self.spaces_moved += final_move

def generate_new_horse():
    max_stat = max_stat_total -1
    
    speed = randint(1,max_stat)

    max_agility = max_stat_total - speed
    min_agility = clamp(max_agility-2, 1, max_agility)
    agility = clamp(randint(1, max_stat), min_agility, max_agility)

    horse_name_index = randint(0,len(horse_names)-1)
    horse_name = horse_names[horse_name_index]

    new_horse = horse(horse_name,speed,agility)

    

    return new_horse



for i in range(0,horse_amount):
    new_horse = generate_new_horse()
    horses.append(new_horse)
    print(new_horse.name,new_horse.speed,new_horse.agility)

while game:
    print("---------------------------")
    for horsey in horses:
        horsey.gallop()
        print(horsey.name,horsey.spaces_moved)
    sleep(1)
    print("---------------------------")




