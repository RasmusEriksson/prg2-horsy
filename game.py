
import random
from random import randint
import math
from time import sleep
import os

game = True


horse_amount = 6
max_stat_total = 8

track_length = 100
visual_length = 50


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
    "STUPID IDIOT",
    "Bruh",
    "folded paper",
    "death bringer",
    "rose",
    "Toad",
    "Lalaboola",
    "Triceratops",
    "7",
    "Horse5.png",
    "uhmm uhhhh.... uh... uhmmm",
    "joe"
]


def printF(msg,end="\n"):
    print(msg,end = end,flush=True)

def print_copies(string,copies,new_line = True):
    for i in range(0, copies):
        printF(string,end="")
    if new_line:
        printF("")


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

    horse_name = random.choice(horse_names)

    new_horse = horse(horse_name,speed,agility)

    

    return new_horse


def render_race_frame(msg):
    os.system("clear")

    printF("\n\n\n\n\n")

    printF(msg)

    print_copies("=",visual_length)

    for horse in horses:

        track_alpha = float(horse.spaces_moved) / float(track_length)
        spaces_traveled = clamp(int(track_alpha * visual_length),-1,visual_length)

        spaces_left = visual_length - (spaces_traveled+1)

        printF(str(horse.name) +":"+ str(horse.spaces_moved))
        print_copies(".",spaces_left,False)
        print_copies("🐎",1,False)
        print_copies("+",spaces_traveled,True)




        print_copies("-",visual_length)
    
    print_copies("=",visual_length)
 

for i in range(0,horse_amount):
    new_horse = generate_new_horse()
    horses.append(new_horse)
    print(new_horse.name,new_horse.speed,new_horse.agility)

render_race_frame("Ready???")
sleep(3)

while game:
    
    
    winning_horse = False
    winning_value = track_length -1

    for horsey in horses:
        horsey.gallop()
        if horsey.spaces_moved > winning_value:
            winning_horse = horsey
            winning_value = horsey.spaces_moved

    render_race_frame("RACE!!!")

    if winning_horse:
        game = False
        

        print_copies("🎉--",int(visual_length/3))
        printF(f"{winning_horse.name.upper()} HAS WON!!!!!! WOOOOOOOOO!!!!!!")
        print_copies("🎉--",int(visual_length/3))
    
    sleep(1)




