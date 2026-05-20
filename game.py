
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

def print_middle(msg, char, end="\n", leftover: bool = False):
    pos_offset = int((char - len(msg))/2)
    print_copies(" ",pos_offset,False)
    printF(msg,end)
    if leftover:
        leftovers = char - (pos_offset + len(msg))
        print_copies(" ",leftovers,False)

def clamp(n, lowest, highest):
    return max(lowest,min(n,highest))
    
class StoreFront:
    def __init__(self, game, item_amount):
        self.game = game
        self._item_amount = item_amount
        self._items = []
        self._potential_items = [
            Roid("Speed Pills","💊",350,0,3),
            Roid("Performance enhancer","😃",500,3,0),
            Roid("CRAZY STUFF!!!","💓",1000,-2,10),
            Roid("Sallad","🥬",800,2,2),
            Advertisement("TOOTHBRUSH AD","🪥",250,500),
            Advertisement("Big Spender","😎",2500,1000,3),
            Advertisement("Illegal Bet","🕵️",500,2000,1.5)
        ]
        self.store_pick = 0
    
    def get_new_items(self):
        self.items = []
        for _ in range(self._item_amount):
            random_index = randint(1,self._item_amount) -1
            new_item = self._potential_items[random_index]
            self.items.append(new_item)
    
    def store_input(self, characters):
        print_copies("-",characters)
        print_middle("controls",characters)
        print_middle("Input: (A) <--  (D) --> (S) Go Back (ENTER) buy selected item",characters)
        if error:
            print_middle(error,characters)
        print_copies("-",characters)

        print_copies("=",characters)
        
        choice = input("Input?:  ").upper()
        continue_val = False
        error = None

        if choice == "S":
            self.game.on_store = False
        else:
            if choice == "A":
                self.store_pick = clamp(self.store_pick-1 , 1, len(self.betting_options))
            elif choice == "D":
                self.store_pick = clamp(self.store_pick+1 , 1, len(self.betting_options))
            elif choice == "":
                stage = 2
        
        return [continue_val, error, stage]

    def print_storefront(self, msg):
        game._clear_frame()

        characters = 0
        inbetween = "|   |"

        item_characters_dict = {}
        
        for item in self.items:
            item_characters = clamp(len(item.name), 20, math.inf)
            item_characters_dict[item] = item_characters
            characters += item_characters + len(inbetween)
        
        print_copies("=",characters)
        print_middle("dallars:" + str(game.money) + "$",characters)
        print_copies("=",characters)
        print_middle(msg,characters)
        print_copies("-",characters)

        
        

        for item in self.items:
            printF(inbetween,"")
            item_characters = item_characters_dict[item]
            print_middle(item.name, item_characters,"", True)
        printF(inbetween)

        for item in self.items:
            printF(inbetween,"")
            item_characters = item_characters_dict[item]
            print_middle(item.visual, item_characters -1,"", True)
        printF(inbetween)

        for item in self.items:
            printF(inbetween,"")
            item_characters = item_characters_dict[item]
            if type(item) == Roid:
                if item.speed_buff != 0:
                    print_middle("Speed: "+str(item.speed_buff), item_characters , "",True)
                else:
                    print_middle(" ", item_characters , "",True)
            elif type(item) == Advertisement:
                if item.cash_buff != 0:
                    print_middle("Extra cash: "+str(item.cash_buff), item_characters , "",True)
                else:
                    print_middle(" ", item_characters , "",True)
        printF(inbetween)

        for item in self.items:
            printF(inbetween,"")
            item_characters = item_characters_dict[item]
            if type(item) == Roid:
                if item.agility_buff != 0:
                    print_middle("Agility: "+str(item.agility_buff), item_characters , "",True)
                else:
                    print_middle(" ", item_characters , "",True)
            elif type(item) == Advertisement:
                if item.money_multiplier != 0:
                    print_middle("Money Mult: "+str(item.money_multiplier), item_characters , "",True)
                else:
                    print_middle(" ", item_characters , "",True)
        printF(inbetween)

        for item in self.items:
            printF(inbetween,"")
            print_middle("Cost: "+str(item.cost), item_characters_dict[item],"",True)
        printF(inbetween)

        print_copies("-",characters)
        test = input("wait a bit ")

            

class Item:
    def __init__(self, name, visual, cost):
        self.name = name
        self.visual = visual
        self.cost = cost
    
    def buy(self, money, selected_horse):
        error = None
        if money > self.cost:
            money -= self.cost
            self._buff(selected_horse)
        else:
            error = "YOU ARE TOO POOR TO BUY THIS ITEM!"
        return [money, error]
    
    def _buff(self, selected_horse):
        pass

class Roid(Item):
    def __init__(self, name, visual, cost, agility_buff, speed_buff):
        super().__init__(name,visual,cost)
        self.agility_buff = agility_buff
        self.speed_buff = speed_buff
        
    
    def _buff(self, selected_horse):
        selected_horse.speed += self.speed_buff
        selected_horse.agility += self.agility_buff

class Advertisement(Item):
    def __init__(self, name, visual, cost, cash_buff, money_multiplier = 1):
        super().__init__(name,visual,cost)
        self.cash_buff = cash_buff
        self.money_multiplier = money_multiplier

    def _buff(self, selected_horse):
        selected_horse.cash_gain += self.cash_buff
        selected_horse.money_multiplier += self.cash_multiplier



class Horse:
    def __init__(self) -> None:
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
        
        self.speed = 1
        self.agility = 1

        self.spaces_moved = 0
        self.money_multiplier = 1
        self.cash_gain = 0

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
    
    def set_values(self,speed,agility):
        stat_difference = clamp(abs(speed - agility) - 2, 0, math.inf)
        stat_from_max = max_stat_total - (speed + agility)

        self.money_multiplier = 1 + (stat_from_max * 0.25) + (stat_difference * 0.15)
        self.speed = speed
        self.agility = agility

class Horse_handler:
    def __init__(self, horse_amount):
        self.horse_amount = horse_amount
        
        self.betting_options = [0.25,0.5,0.75,0.9]
        self.bet_value = self.betting_options[0]

        self.money = 500
        self.horses = []
        self.selected_horse = None

        self.horse_option = 1
        self.bet_option = 1
    
    def _generate_new_horse(self):
        #Decide speed based on the maximum stat total the horse can have.
        #Speed can be maximum of the total stats -1 to leave room for agility
        max_speed = max_stat_total -1
        speed = randint(1,max_speed)

        #Decide max_agility by taking what's leftover of the stat total when speed is subtracted
        #Max agility is still random to make horses more varied and not have their stat total always be that of the max_stat_total variable
        max_agility = max_stat_total - speed
        agility = randint(1, max_agility)

        new_horse = Horse()
        new_horse.set_values(speed,agility)

        return new_horse
    
    def generate_horses(self):
        self.horses = []
        for _ in range(0,self.horse_amount):
            new_horse = self._generate_new_horse()
            self.horses.append(new_horse)
    
    def reroll(self) -> str:
        if self.money >= 100:
            self.money -= math.floor(self.money * 0.05)
            self.generate_horses()
            self.horse_option = 1
            return None
        else:
            return "YOU ARE TOO POOR TO REROLL!"

class Game(Horse_handler):
    def __init__(self, horse_amount, track_length, visual_length):
        super().__init__(horse_amount)
        
        self.track_length = track_length
        self.visual_length = visual_length
        self.store = StoreFront(self,3)  
        self.on_store = False
        

    def _bet_val_to_str(self, val) -> str:
        return str(int(val*100)) + "% (" + str(int(self.money*val)) + "$)"

    def _clear_frame(self):
        os.system("clear")
        printF("\n\n\n\n\n")


    def render_betting_frame(self, msg, controls, stage, error = None) -> bool:
        if self.on_store:
            self.store.print_storefront()
            pass
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
                self.bet_value = bet
            betval += "   "
            bet_visuals += betval

        selected_display = "[[[ " + self.selected_horse.name + " " + self.selected_horse.visual + "  |  💸 Bet: " + self._bet_val_to_str(self.bet_value) + "]]]"

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

        stats = "Speed: " + str(self.selected_horse.speed) + "   Agility: " + str(self.selected_horse.agility) + "   Cash Multiplier: " + str(self.selected_horse.money_multiplier) + "\n\n"
        
        print_middle(stats,characters)

        print_copies("-",characters)

        if stage ==2:
            printF("")
        printF(bet_visuals)
        if stage ==2:
            printF("")

        return self.bet_input(stage, controls, characters, error)

    def bet_input(self, stage, controls, characters, error) -> bool:
        print_copies("-",characters)
        print_middle("controls",characters)
        print_middle(controls,characters)
        if error:
            print_middle(error,characters)
        print_copies("-",characters)

        print_copies("=",characters)
        
        choice = input("Input?:  ").upper()
        continue_val = False
        error = None

        if choice == "R":
            error = self.reroll()
            stage = 1
        elif choice == "X":
            self.on_store = True
        else:
            if stage == 1:
                if choice == "A":
                    self.horse_option = clamp(self.horse_option-1 , 1, len(self.horses))
                elif choice == "D":
                    self.horse_option = clamp(self.horse_option+1 , 1, len(self.horses))
                elif choice == "":
                    stage = 2
            elif stage == 2:
                if choice == "A":
                    self.bet_option = clamp(self.bet_option-1 , 1, len(self.betting_options))
                elif choice == "D":
                    self.bet_option = clamp(self.bet_option+1 , 1, len(self.betting_options))
                elif choice == "S":
                    stage = 1
                elif choice == "":
                    continue_val = True
        
        return [continue_val, error, stage]


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
            new_money += int(self.bet_value * self.money * self.selected_horse.money_multiplier + self.selected_horse.cash_gain)
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
        self.store.get_new_items()

        error = None
        
        stage = 1

        #Continue on rendering the betting frame till players have made their final bet on their chosen horse
        continue_val = False
        while not continue_val:
            goback = ""
            
            action = None
            if stage == 1:
                action = "🐴 pick your horse! 🐴"
            elif stage == 2:
                action = "💸 pick how much you wanna bet! 💸"
                goback = "  (S) Go Back"
            
            action_controls = "Input: (A) <--  (D) -->" + goback +  "  (R) reroll {" + self._bet_val_to_str(0.05) + "}  (ENTER) pick"
        
            continue_values = self.render_betting_frame(action, action_controls, stage, error)
            continue_val = continue_values[0]
            error = continue_values[1]
            stage = continue_values[2]

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
                
            sleep(0.1)
        self.bet_option = 1
        self.horse_option = 1


game = Game(5, 100, 50)

while game_running:
    game.run_round()

    
