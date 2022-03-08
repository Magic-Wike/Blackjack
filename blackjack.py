import random
from re import L
import sys
import os
import random_names
from time import sleep

y_responses = ['y', 'yes', 'ya', 'yup', 'send it', 'hit me']
n_responses = ['n', 'no', 'nope', 'nah']
quit_commands = ['quit', 'exit', 'x', 'bye']
hand_commands = ['hit', 'hit me', 'double', 'double down', 'stay', 'stand', 'split']
user_commands = {'chips': 'return current # of player chips', 'commands': 'show commands list'}



class Deck:
    card_names = ['Two of Clubs', 'Two of Spades', 'Two of Diamonds', 'Two of Hearts', 'Three of Clubs', 'Three of Spades', 'Three of Diamonds', 'Three of Hearts', 'Four of Clubs', 'Four of Spades', 'Four of Diamonds', 'Four of Hearts', 'Five of Clubs', 'Five of Spades', 'Five of Diamonds', 'Five of Hearts', 'Six of Clubs', 'Six of Spades', 'Six of Diamonds', 'Six of Hearts', 'Seven of Clubs', 'Seven of Spades', 'Seven of Diamonds', 'Seven of Hearts', 'Eight of Clubs', 'Eight of Spades', 'Eight of Diamonds', 'Eight of Hearts', 'Nine of Clubs', 'Nine of Spades', 'Nine of Diamonds', 'Nine of Hearts', 'Ten of Clubs', 'Ten of Spades', 'Ten of Diamonds', 'Ten of Hearts', 'Jack of Clubs', 'Jack of Spades', 'Jack of Diamonds', 'Jack of Hearts', 'Queen of Clubs', 'Queen of Spades', 'Queen of Diamonds', 'Queen of Hearts', 'King of Clubs', 'King of Spades', 'King of Diamonds', 'King of Hearts', 'Ace of Clubs', 'Ace of Spades', 'Ace of Diamonds', 'Ace of Hearts']
    card_values = {'Two' : 2, 'Three': 3, 'Four' : 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 10]}

    def __init__(self, num_shoes=1):
        self.cards = self.generate_deck(num_shoes)
        self.shoe_size = str(num_shoes)
        pass

    def generate_deck(self, num_shoes=1):
        deck = []
        for i in range(num_shoes):
            for card in self.card_names:
                deck.append(card)
            random.shuffle(deck)
        return deck

    def deal_card(self, num_cards=1):
        for i in range(num_cards):
            random_index = random.randint(1, len(self.cards)-1)
            random_card = self.cards[random_index]
            self.cards.remove(random_card)
        return random_card        

class Player:

    def __init__(self, name, chip_count=1000, high_roller=False):
        self.name = name
        self.chip_count = chip_count
        self.high_roller = high_roller
        self.bank = 0

    def win(self, amount):
        self.chip_count += amount

    def lose(self, amount):
        if amount > self.chip_count:
            self.chip_count -= amount
        else:
            self.chip_count = 0

    def bank_deposit(amount):
        pass



class CPU_player:

    def __init__(self, chip_count=random.randrange(500, 5000, 50), high_roller=False):
        self.name = random_names.random_name()
        self.chip_count = chip_count
        self.high_roller = high_roller

userOS = str(sys.platform)

def clearFunc():
  if "win32" not in userOS:
    os.system('clear')
  else:
    os.system('cls')

def clean_input(string):
    cleaned = string.strip().lower()
    return cleaned 

def killswitch():
    print("\n\n\n\nGoobye!\n\n\n\n")
    quit()

def print_user_commands():
    print("\n")
    for k, v in user_commands.items():
        print("{}: {}".format(k, v))
    

def command_parse(user_input):
    while True:
        raw_input = input(user_input)
        if raw_input in quit_commands:
            killswitch()
        elif type(raw_input) == int:
            return raw_input
        elif "What is your name?" in user_input:
            if raw_input == "":
                print("Please enter a name!")
                continue
            elif raw_input.isalpha() == False:
                print("Please use letters only")
                continue
            else:
                 return raw_input
        cleaned = raw_input.strip().lower()
        if cleaned == "chips":
            try:
                print("You have {} chips.".format(player1.chip_count))
                continue
            except NameError:
                print("Player does not exist. (start a game first)")
                continue
        elif cleaned == "commands":
                print_user_commands()
                continue
        elif cleaned in hand_commands:
            return cleaned
        elif cleaned in y_responses:
            return "y"
        elif cleaned in n_responses:
            return "n"
        else: 
            print("Invalid input")
            continue

def get_bet(min=50, max=500):
    while True:
        raw_bet = input("\nPlace your bets!:\n")
        try:
            bet = int(raw_bet)
        except ValueError:
            print("Must enter a bet. (Can be numbers only)")
            continue
        if bet > max:
            print("\nTable limit is ${}".format(max))
            continue
        elif bet < min:
            print("\nTable minimum is ${}".format(min))
            continue
        elif bet > player1.chip_count:
            print("\nNot enough chips. You currently have ${}".format(player1.chip_count))
            continue
        else:
            player1.chip_count -= bet
            return bet

def get_card_val(card):
    card_val = 0
    for key in deck.card_values.keys():
        if card.startswith(key):
            card_val = deck.card_values[key]
    return card_val

def sum_cards(card_list):  
    # will return list if multiple values under 21
    if type(card_list[0]) is list and type(card_list[1]) is list:
        card_list[0].pop(10)
        card_list[1].pop(10)
        cards_val = 2
    if type(card_list[0]) is list:
        ace = card_list[0]
        sum1 = ace[0] + card_list[1]
        sum2 = ace[1] + card_list[1]
        if sum1 > 21:
            cards_val = sum2
        elif sum2 > 21:
            cards_val = sum1
        else: 
            cards_val = [sum1, sum2]
            cards_val.sort() 
    elif type(card_list[1]) is list:
        ace = card_list[1]
        sum1 = ace[0] + card_list[0]
        sum2 = ace[1] + card_list[0]
        if sum1 > 21:
            cards_val = sum2
        elif sum2 > 21:
            cards_val = sum1
        else: 
            cards_val = [sum1, sum2]
            cards_val.sort() 
    else:
        cards_val = sum(card_list)
    return cards_val


def player_win(bet, is_bj=False):
    if is_bj == True:
        print("\nYou have blackjack!")
        bj_win = bet + (bet * 1.5)
        print("\nYou win ${:.2f}".format(bj_win))
        player1.chip_count += bj_win
    else:
        reg_win = bet * 2
        print("\nYou win ${:.2f}!".format(reg_win))
        player1.chip_count += reg_win     

def print_player_cards(player_cards):
    print("\n{}'s cards:".format(player1.name))
    for card in player_cards:
        print(str(card))
      

def play_hand(dealer_cards, player_dict, bet):
    total_bet = bet
    # go through all players (will have cpus later), and append card vals to list, process Aces
    for player in player_dict:
        player_card_vals = []
        for card in player_dict[player]:
            player_card_vals.append(get_card_val(card))
    print("player_card_vals:", player_card_vals)
    player_val = sum_cards(player_card_vals)
    print("player_val:", player_val)
    # check if player has BJ
    try:
        if 21 in player_val:
            player_win(bet, is_bj=True)
    except:
        pass
    if player_val == 21:
        player_win(bet, is_bj=True)
    # add dealer card vals to list and process Aces
    dealer_card_vals =[]
    for card in dealer_cards:
        card_val = get_card_val(card)
        dealer_card_vals.append(card_val)
    print("dealer_card_vals:", dealer_card_vals)
    dealer_val = sum_cards(dealer_card_vals)
    print("dealer_val", dealer_val)
    # will add Insurance? function here
    print("\n\nDealer checking for 21...\n")
    sleep(2)
    if type(dealer_val) is list and 21 in dealer_val:
        print("Dealer has blackjack! \n")
        if player_val == 21:
            pass
        else:
            print("\nEveryone loses =(")
            print("\nYou lose ${:.2f}".format(bet))
    else:
        print("\nNobody home!\n")
        print("\nDealer shows: {}".format(dealer_cards[1]))
        # blackjacks handled. accept player inputs for hit, stand, etc
        try:
            print("You have {} / {}".format(player_val[0], player_val[1]))
        except:
            print("You have {}".format(player_val))
            pass 
        player_stand = False
        while player_stand == False:
            player_hit = command_parse("\nWould you like to hit? (try: 'hit me', 'double down', 'stand', 'split')\n")
            # split command - test if values match, if so create new hand
            if player_hit == 'split':
                if player_card_vals[0] != player_card_vals[1]:
                    print("\nCards must be same value to split!\n")
                    continue
                else:
                    total_bet += bet
                    player1.chip_count -= bet
                    split_card = player_cards.pop(-1)
                    split_cards = [split_card]
                    split_player_val = player_card_vals.pop(-1)
                    split_vals = [split_player_val]
                    # while bust, stay false
                    # hit_me()
                    # if hit me returns int, process it vs. dealer
                    # if hit me returns "Bust"/"Stand" process


            # double down command 
            elif player_hit in ['double', 'double down']:
                total_bet += bet
                # add face up or down function later?
                print("\n{} bets another ${}.".format(player1.name, bet))
                sleep(.05)
                print("\nDealing one more card! Good luck...")
                final_player_val = hit_me(player_cards, player_card_vals, player_val, True)
                if final_player_val in ["Bust", "Win"]:
                    player_stand = True
                else:
                    return final_player_val
            elif player_hit in ['stay', 'stand', n_responses]:
                if type(player_val) is list:
                    final_player_val = max(player_val)
                    return final_player_val
                else:
                    print('\nWike stands with {}.'.format(player_val))
                    final_player_val = int(player_val)
                    return final_player_val
            elif player_hit in ['hit', 'hit me', y_responses]:
                final_player_val = hit_me(player_cards, player_card_vals, player_val)
                if final_player_val in ["Bust", "Win"]:
                    if final_player_val == "Win":
                        player_win(total_bet)        
                    player_stand = True
                else:
                    return final_player_val
            else:
                print('\nInvalid input.')
                continue
        # dealer hit me
        # calc winner

def hit_me(player_cards, player_card_vals, player_val, double_down=False):
    print("\nDealing card...")
    sleep(.05)
    new_card = deck.deal_card()
    player_cards.append(new_card)
    new_val = get_card_val(new_card)
    player_card_vals.append(new_val)
    # if two aces
    if type(player_val) is list and type(new_val) is list:
        player_val[0] += new_val[0]
        player_val[1] += new_val[1]
        if 21 in player_val:
            print("\n21!!! You win!")
            return "Win"
        if player_val[0] < 21 and player_val[1] < 21:
            print("You have {} / {}".format(player_val[0]),player_val[1])
            if double_down == True:
                return player_val
            else:
                while True:    
                    hit_again = command_parse("\nWould you like to hit again?\n")
                    if hit_again in ['hit me', 'hit', y_responses]:
                        hit_me(player_cards, player_card_vals, player_val)
                    elif hit_again in ['stay', 'stand', n_responses]:
                        print("\n{} stands with {}.".format(player1.name, player_val))
                        return player_val
                    else:
                        print("Invalid input.")
                        continue
        elif player_val[1] > 21:
            new_player_val = player_val[0]
            print("\nYou have {}".format(new_player_val))
            if double_down == True:
                return new_player_val
            else:
                while True:
                    hit_again = command_parse("\nnWould you like to hit again?\n")
                    if hit_again in ['hit me', 'hit', y_responses]:
                        hit_me(player_cards, player_card_vals, player_val)
                    elif hit_again in ['stay', 'stand', n_responses]:
                        print("\n{} stands with {}.".format(player1.name, player_val))
                        return new_player_val    
                    else:
                        print("Invalid input.")
                        continue
    # if ace and another card - 
    elif type(player_val) is list and type(new_val) is int:
        player_val[0] += new_val
        player_val[1] += new_val
        if 21 in player_val:
            print("\n21!!! You win!")
            return "Win"
        elif player_val[0] < 21 and player_val[1] < 21:
            while True:
                print("You have {} / {}".format(player_val[0]),player_val[1])
                hit_again = command_parse("\nWould you like to hit again?\n")
                if hit_again in ['hit me', 'hit', y_responses]:
                    hit_me(player_cards, player_card_vals, player_val)
                elif hit_again in ['stay', 'stand', n_responses]:
                    print("\n{} stands with {}.".format(player1.name, player_val))
                    return player_val
                else:
                    print("Invalid input.")
                    continue
        elif player_val[1] > 21:
            new_player_val = player_val[0]
            if double_down == True:
                return new_player_val
            else:
                while True:
                    hit_again = command_parse("\nnWould you like to hit again?\n")
                    if hit_again in ['hit me', 'hit', y_responses]:
                        hit_me(player_cards, player_card_vals, player_val)
                    elif hit_again in ['stay', 'stand', n_responses]:
                        print("\n{} stands with {}.".format(player1.name, player_val))
                        return new_player_val  
                    else:
                        print("Invalid input.")
                        continue
    # no aces - stable
    else:
        player_val += new_val
        print("\nDealer gives {} a {}".format(player1.name, new_card))
        if player_val > 21:
            print("\nYou have {}. You bust!".format(player_val))
            return "Bust"
        else:
            print_player_cards(player_cards)
            print("\nYou have {}".format(player_val))
            if double_down == True:
                return player_val
            else:
                while True:
                    hit_again = command_parse("\nWould you like to hit again?\n")
                    if hit_again in ['hit me', 'hit', y_responses]:
                        hit_me(player_cards, player_card_vals, player_val)
                    elif hit_again in ['stay', 'stand', n_responses]:
                        print("\n{} stands with {}.".format(player1.name, player_val))
                        return player_val
                    else:
                        print("Invalid input.")
                        continue

      
            

# gameplay loop

while True:
    clearFunc()
    welcome = command_parse("\n\nWelcome! What is your name?: \n")
    player1 = Player(welcome)
    is_ready = command_parse("\nReady to play?\n")
    if is_ready == "n":
        killswitch()
    else:
        print("\nShuffling cards...\n")
        # get bets and deal cards -- turn into sep function?
        deck = Deck(3)
        while True:
            player_cards = []
            dealer_cards = []
            players = [player1.name]
            hand = {}
            bet = get_bet()
            print("\n{} bets ${}...\n".format(player1.name, bet))
            print("\nCards coming out...\n\n")
            for i in range(2):
                for player in players:
                    rnd_player_card = deck.deal_card()
                    rnd_dealer_card = deck.deal_card()
                    player_cards.append(rnd_player_card)
                    dealer_cards.append(rnd_dealer_card)
                print("Dealer gives {} a {}...".format(player1.name, rnd_player_card))
                print("Dealer draws a card...")
            print("\nDealer shows {}".format(dealer_cards[1]))
            # add all players + vals to dict...for cpus later
            for player in players:
                hand[player] = player_cards
            print("dealer_cards:", dealer_cards)
            print("player_cards:", player_cards)
            play_hand(dealer_cards, hand, bet)

            # end loop
            play_again = command_parse("\nPlay another hand?\n")
            if play_again in y_responses:
                print("{}'s current chip count: {}".format(player1.name, player1.chip_count))
                continue
            else:
                killswitch()




        
        
