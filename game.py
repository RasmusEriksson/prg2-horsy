
import random
from random import randint
import math
from time import sleep
import os


game = True
racing = True


horse_amount = 5
max_stat_total = 8

track_length = 100
visual_length = 50

money = 500
horse_option = 1
bet_option = 1


horses = []
betting_options = [0.25,0.5,0.75,0.9]

selected_horse = NotImplemented
bet_value = betting_options[0]




horse_visuals = ["🏇","🎠","🐎","🐴 ","🫎 ","🦕 ","🐈 ","🥸 "]
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

def print_middle(msg,char,end="\n"):
    pos_offset = int((char - len(msg))/2)
    print_copies(" ",pos_offset,False)
    printF(msg,end)

def clamp(n,lowest,highest):
    return max(lowest,min(n,highest))
    


class horse:
    def __init__(self,name,speed,agility) -> None:
        
        self.name = name

        self.speed = speed
        self.agility = agility

        self.spaces_moved = 0

        self.visual = random.choice(horse_visuals)

    def gallop(self):
        roll = randint(1,6)
        agility_roll = randint(1,self.agility) + 2

        multiplier = 1

        if agility_roll < roll:
            multiplier = -1
            
        final_move = self.speed * multiplier
        self.spaces_moved += final_move

def bet_val_to_str(val) -> str:
    return str(int(val*100)) + "% (" + str(int(money*val)) + "$)"

def generate_new_horse():
    max_stat = max_stat_total -1
    
    speed = randint(1,max_stat)

    max_agility = max_stat_total - speed
    min_agility = clamp(max_agility-2, 1, max_agility)
    agility = clamp(randint(1, max_stat), min_agility, max_agility)

    horse_name = random.choice(horse_names)

    new_horse = horse(horse_name,speed,agility)

    return new_horse

def clear_frame():
    os.system("clear")
    printF("\n\n\n\n\n")

def render_beting_frame(msg,controls,stage) -> bool:
    clear_frame()
    global horse_option
    global bet_option

    global selected_horse
    global bet_value

    current_option = 0
    selected = NotImplemented
    selected_bet = NotImplemented
    
    characters = 0
    names_visual = ""

    #Creates the visuals to be printed out for what horses there are and which are picked
    for horse in horses:
        current_option += 1

        name = horse.name + horse.visual

        if current_option == horse_option:
            name = "[⭐ " + name + " ⭐]"
            selected = horse
            selected_horse = horse
        
        name += "   "
        characters += len(name)

        names_visual += name
    
    #Creates the visuals to be printed out for which betting option is currently picked
    current_option = 0
    bet_visuals = ""

    for bet in betting_options:
        current_option += 1

        betval = bet_val_to_str(bet)

        if current_option == bet_option:
            betval = "{💰 " + betval + " 💰}"
            bet_value = bet

        
        
        betval += "   "

        bet_visuals += betval

    selected_display = "[[[ " + selected_horse.name + " " + selected_horse.visual + "  |  💸 Bet: " + bet_val_to_str(bet_value) + "]]]"

    print_copies("=",characters)
    print_middle("dallars:" + str(money) + "$",characters)
    print_copies("=",characters)
    print_middle(msg,characters)
    print_copies("-",characters)

    if stage ==1:
        printF("")
    printF(names_visual)
    if stage ==1:
        printF("")

    print_copies("-",characters)
    printF("")
    print_middle(selected_display, characters)
    printF("")

    stats = "Speed: " + str(selected.speed) + "   Agility: " + str(selected.agility) + "\n\n"
    
    print_middle(stats,characters)

    print_copies("-",characters)

    if stage ==2:
        printF("")
    printF(bet_visuals)
    if stage ==2:
        printF("")

    print_copies("-",characters)
    print_middle("controls",characters)
    print_middle(controls,characters)
    print_copies("-",characters)

    print_copies("=",characters)
    
    choice = input("Input?:  ").upper()
    continue_val = False

    if stage == 1:
        if choice == "A":
            horse_option = clamp(horse_option-1 , 1, len(horses))
        elif choice == "D":
            horse_option = clamp(horse_option+1 , 1, len(horses))
        elif choice == "":
            continue_val = True
    elif stage == 2:
        if choice == "A":
            bet_option = clamp(bet_option-1 , 1, len(betting_options))
        elif choice == "D":
            bet_option = clamp(bet_option+1 , 1, len(betting_options))
        elif choice == "":
            continue_val = True

    
    return continue_val

def render_race_frame(msg):
    clear_frame()

    printF(msg)

    your_horse = "you've bet: " + bet_val_to_str(bet_value) + " on "  + selected_horse.name + " " + selected_horse.visual

    print_copies("=",visual_length)
    print_middle(your_horse,visual_length)
    print_copies("=",visual_length)

    for horse in horses:

        track_alpha = float(horse.spaces_moved) / float(track_length)
        spaces_traveled = clamp(int(track_alpha * visual_length),-1,visual_length)

        spaces_left = visual_length - (spaces_traveled+1)

        horse_name = str(horse.name) +":"+ str(horse.spaces_moved)
        if horse == selected_horse:
            horse_name += " <---- your horse"

        printF(horse_name)
        print_copies(".",spaces_left,False)
        print_copies(horse.visual,1,False)
        print_copies("+",spaces_traveled,True)




        print_copies("-",visual_length)
    
    print_copies("=",visual_length)
 
def render_win_frame(winning_horse):
    clear_frame()

    previous_money = money
    new_money = previous_money

    print_copies("=",visual_length)
    print_copies("🎉--",int(visual_length/3))
    printF("")
    print_middle(f"{winning_horse.name.upper()} HAS WON!!!!!! WOOOOOOOOO!!!!!!",visual_length)
    print_middle("0===========0",visual_length)
    printF("")
    print_copies("🎉--",int(visual_length/3))
    print_copies("=",visual_length)

    printF("")
    
    if winning_horse == selected_horse:
        new_money += int(bet_value * money)
        print_middle("(+) your horse won!!!!!! (+)",visual_length)
    else:
        new_money -= int(bet_value * money)
        print_middle("(-) your horse lost...... (-)",visual_length)

    print_middle(str(previous_money) + "$  --->  " + str(new_money) + "$",visual_length)

    printF("")

    print_copies("=",visual_length)
    next_round = input("input anything to continue: ")
    return new_money



while game:

    horses = []

    for i in range(0,horse_amount):
        new_horse = generate_new_horse()
        horses.append(new_horse)

    continue_val = False
    while not continue_val:
        continue_val = render_beting_frame("🐴 pick your horse! 🐴","Input: (A) <--,(D) -->, (ENTER) pick",1)
    continue_val = False
    while not continue_val:
        continue_val = render_beting_frame("💸 pick how much you wanna bet! 💸","Input: (A) <--,(D) -->, (ENTER) pick",2)

    racing = True

    render_race_frame("Ready???")
    sleep(3)

    while racing:
        
        
        winning_horse = False
        winning_value = track_length -1

        for horsey in horses:
            horsey.gallop()
            if horsey.spaces_moved > winning_value:
                winning_horse = horsey
                winning_value = horsey.spaces_moved

        render_race_frame("RACE!!!")

        if winning_horse:
            racing = False
            money = render_win_frame(winning_horse)
            
        sleep(0.5)
    bet_option = 1
    horse_option = 1