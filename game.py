
import random
from random import randint
import math
from time import sleep
import os


game_running = True
racing = True

max_stat_total = 8


#Establishes printing functions for positioning and repetition in the terminal 
# + a useful clamp function which clamps a number between two number values
def printF(msg, end="\n"):
    print(msg,end = end,flush=True)

def print_copies(string, copies, new_line = True):
    for i in range(0, copies):
        printF(string,end="")
    if new_line:
        printF("")

def print_middle(msg, char, end="\n"):
    pos_offset = int((char - len(msg))/2)
    print_copies(" ",pos_offset,False)
    printF(msg,end)

def clamp(n, lowest, highest):
    return max(lowest,min(n,highest))
    


class horse:
    def __init__(self, speed, agility) -> None:
        self.horse_visuals = ["🏇","🎠","🐎","🐴 ","🫎 ","🦕 ","🐈 ","🥸 "]
        self.horse_names = [
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
        
        self.speed = speed
        self.agility = agility

        self.spaces_moved = 0

        self.name = random.choice(self.horse_names)
        self.visual = random.choice(self.horse_visuals)

    def gallop(self):
        roll = randint(1,6)
        agility_roll = randint(1,self.agility) + 2

        multiplier = 1

        if agility_roll < roll:
            multiplier = -1
            
        final_move = self.speed * multiplier
        self.spaces_moved += final_move

class game_logic:
    def __init__(self, horse_amount, track_length):
        self.horse_amount = horse_amount
        self.track_length = track_length

        self.betting_options = [0.25,0.5,0.75,0.9]
        self.bet_value = self.betting_options[0]

        self.money = 500
        self.horses = []
        self.selected_horse = None
    
    def _generate_new_horse(self):
        #Decide speed based on the maximum stat total the horse can have.
        #Speed can be maximum of the total stats -1 to leave room for agility
        max_speed = max_stat_total -1
        speed = randint(1,max_speed)

        #Decide max_agility by taking what's leftover of the stat total when speed is subtracted
        #Max agility is still random to make horses more varied and not have their stat total always be that of the max_stat_total variable
        max_agility = max_stat_total - speed
        agility = randint(1, max_agility)

        new_horse = horse(speed,agility)

        return new_horse
    
    def generate_horses(self):
        self.horses = []
        for _ in range(0,self.horse_amount):
            new_horse = self._generate_new_horse()
            self.horses.append(new_horse)
        
class game(game_logic):
    def __init__(self, horse_amount, track_length, visual_length):
        game_logic.__init__(self, horse_amount, track_length)
        
        self.visual_length = visual_length  

        self.horse_option = 1
        self.bet_option = 1
        

    def _bet_val_to_str(self, val) -> str:
        return str(int(val*100)) + "% (" + str(int(self.money*val)) + "$)"

    def _clear_frame(self):
        os.system("clear")
        printF("\n\n\n\n\n")

    def render_beting_frame(self, msg, controls, stage) -> bool:
        self._clear_frame()

        #Establishing variables
        current_option = 0
        characters = 0
        names_visual = ""

        #Creates the visuals to be printed out for what horses there are and which are picked
        for horse in self.horses:
            current_option += 1

            name = horse.name + horse.visual

            if current_option == self.horse_option:
                name = "[⭐ " + name + " ⭐]"
                selected = horse
                self.selected_horse = horse
            
            name += "   "
            characters += len(name)

            names_visual += name
        
        #Creates the visuals to be printed out for which betting option is currently picked
        current_option = 0
        bet_visuals = ""

        for bet in self.betting_options:
            current_option += 1
            betval = self._bet_val_to_str(bet)

            if current_option == self.bet_option:
                betval = "{💰 " + betval + " 💰}"
                bet_value = bet
            betval += "   "
            bet_visuals += betval

        selected_display = "[[[ " + self.selected_horse.name + " " + self.selected_horse.visual + "  |  💸 Bet: " + self._bet_val_to_str(bet_value) + "]]]"

        print_copies("=",characters)
        print_middle("dallars:" + str(self.money) + "$",characters)
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

        stats = "Speed: " + str(self.selected_horse.speed) + "   Agility: " + str(self.selected_horse.agility) + "\n\n"
        
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
                self.horse_option = clamp(self.horse_option-1 , 1, len(self.horses))
            elif choice == "D":
                self.horse_option = clamp(self.horse_option+1 , 1, len(self.horses))
            elif choice == "":
                continue_val = True
        elif stage == 2:
            if choice == "A":
                self.bet_option = clamp(self.bet_option-1 , 1, len(self.betting_options))
            elif choice == "D":
                self.bet_option = clamp(self.bet_option+1 , 1, len(self.betting_options))
            elif choice == "":
                continue_val = True

        
        return continue_val

    def render_race_frame(self, msg):
        self._clear_frame()

        printF(msg)

        your_horse = "you've bet: " + self._bet_val_to_str(self.bet_value) + " on "  + self.selected_horse.name + " " + self.selected_horse.visual

        print_copies("=",self.visual_length)
        print_middle(your_horse,self.visual_length)
        print_copies("=",self.visual_length)

        for horse in self.horses:

            track_alpha = float(horse.spaces_moved) / float(self.track_length)
            spaces_traveled = clamp(int(track_alpha * self.visual_length),-1,self.visual_length)

            spaces_left = self.visual_length - (spaces_traveled+1)

            horse_name = str(horse.name) +":"+ str(horse.spaces_moved)
            if horse == self.selected_horse:
                horse_name += " <---- your horse"

            printF(horse_name)
            print_copies(".",spaces_left,False)
            print_copies(horse.visual,1,False)
            print_copies("+",spaces_traveled,True)
            print_copies("-",self.visual_length)
        print_copies("=",self.visual_length)
    
    def render_win_frame(self, winning_horse):
        self._clear_frame()

        previous_money = self.money
        new_money = previous_money

        print_copies("=",self.visual_length)
        print_copies("🎉--",int(self.visual_length/3))
        printF("")
        print_middle(f"{winning_horse.name.upper()} HAS WON!!!!!! WOOOOOOOOO!!!!!!",self.visual_length)
        print_middle("0===========0",self.visual_length)
        printF("")
        print_copies("🎉--",int(self.visual_length/3))
        print_copies("=",self.visual_length)
        printF("")
        
        if winning_horse == self.selected_horse:
            new_money += int(self.bet_value * self.money)
            print_middle("(+) your horse won!!!!!! (+)",self.visual_length)
        else:
            new_money -= int(self.bet_value * self.money)
            print_middle("(-) your horse lost...... (-)",self.visual_length)

        print_middle(str(previous_money) + "$  --->  " + str(new_money) + "$",self.visual_length)
        printF("")

        print_copies("=",self.visual_length)
        _next_round = input("input anything to continue: ")

        self.money = new_money


    def run_round(self):
        self.generate_horses()

        #Continue on rendering the betting frame till players have made their choice of horse
        continue_val = False
        while not continue_val:
            continue_val = self.render_beting_frame("🐴 pick your horse! 🐴","Input: (A) <--,(D) -->, (ENTER) pick",1)
        #Continue on rendering the betting frame till players have made their choice of how much they wanna bet
        continue_val = False
        while not continue_val:
            continue_val = self.render_beting_frame("💸 pick how much you wanna bet! 💸","Input: (A) <--,(D) -->, (ENTER) pick",2)

        #Small introduction to showcase the board and "build tenstion"
        racing = True
        self.render_race_frame("Ready???")
        sleep(3)

        #Race until a winner is decided and then render the win frame which also sets the new money value before restarting the process
        while racing:
        
            winning_horse = False
            winning_value = self.track_length -1

            for horsey in self.horses:
                horsey.gallop()
                if horsey.spaces_moved > winning_value:
                    winning_horse = horsey
                    winning_value = horsey.spaces_moved

            self.render_race_frame("RACE!!!")

            if winning_horse:
                sleep(0.5)
                racing = False
                self.render_win_frame(winning_horse)
                
            sleep(0.5)
        self.bet_option = 1
        self.horse_option = 1


Game = game(5, 100, 50)

while game_running:
    Game.run_round()

    
