import random
from re import L
import sys
import os
from xml.etree.ElementTree import TreeBuilder
import random_names
from time import sleep

y_responses = ['y', 'yes', 'ya', 'yup', 'send it', 'hit me']
n_responses = ['n', 'no', 'nope', 'nah']
quit_commands = ['quit', 'exit', 'x', 'bye']
hand_commands = ['hit', 'h', 'hit me', 'double', 'd', 'double down', 'stay', 'stand', 's', 'split']
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

    def shuffle(self, num_shuffles=1):
        for i in range(num_shuffles):
            random.shuffle(self.cards)

class Player:

    def __init__(self, name, chip_count=1000, high_roller=False):
        self.name = name
        self.chip_count = chip_count
        self.high_roller = high_roller
        self.bank = 0
        self.last_bet = 0

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
                print("\nPlease enter a name!")
                continue
            elif raw_input.isalpha() == False:
                print("\nPlease use letters only")
                continue
            else:
                 return raw_input
        cleaned = raw_input.strip().lower()
        if cleaned in ["chips", "ch"]:
            try:
                print("You have {} chips.".format(player1.chip_count))
                continue
            except NameError:
                print("Player does not exist. (start a game first)")
                continue
        elif cleaned in ["commands", "cmd"]:
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
        clearFunc()
        if raw_bet in quit_commands:
            killswitch()
        elif raw_bet == "chips":
            print("\nYou have ${}".format(player1.chip_count))
            continue
        elif raw_bet in ['r', 'rebet']:
            if player1.last_bet == 0:
                print("\nNo previous bet.")
                continue
            else:
                if player1.last_bet < player1.chip_count: 
                    bet = player1.last_bet
                    player1.chip_count -= bet
                    return bet
                else:
                    print("\nNot enough chips. You currently have ${}".format(player1.chip_count))
                    continue
        else:
            try:
                bet = int(raw_bet)
            except ValueError:
                print("\nMust enter a bet. (Can be numbers only)")
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
                player1.last_bet = bet
                return bet

def get_card_val(card, get_name=False):
    card_val = 0
    for key in deck.card_values.keys():
        if card.startswith(key):
            if get_name == True:
                split_card = card.split()
                card_name = split_card[0]
                return card_name
            else:
                card_val = deck.card_values[key]
                return card_val
    

def sum_cards(card_list):  
    # will return list if multiple values under 21
    card1 = card_list[0]
    card2 = card_list[1]
    if type(card_list[0]) is list and type(card_list[1]) is list:
        if card1 == [1, 10]:
            card1.pop(1) 
            cards_val = 2
        else:
            sum1, sum2 = card1[0] + card2[0], card1[1] + card2[1]
            if sum2 > 21:
                cards_val = sum1
            elif sum1 > 21:
                cards_val = sum2
            else:
                cards_val = [sum1, sum2]
                cards_val.sort()
    elif type(card1) is list and type(card2) is int:
        sum1, sum2 = card1[0] + card2, card1[1] + card2
        if sum1 > 21:
            cards_val = sum2
        elif sum2 > 21:
            cards_val = sum1
        else: 
            cards_val = [sum1, sum2]
            cards_val.sort() 
    elif type(card1) is int and type(card2) is list:
        sum1, sum2 = card1 + card2[0], card1 + card2[1]
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
        sleep(.05)
        print("\nEveryone loses =(")
        if player_val == 21:
            pass
        else:
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
        while True:
            player_hit = command_parse("\nWould you like to hit? (try: 'hit me', 'double down', 'stand')\n")
            clearFunc()
            # split command - test if values match, if so create new hand
            if player_hit == 'split':
                print("\nSplit command under construction. Soz.")
                continue

                # this code is fine, but need to recursively call play_hand function, but as is it will overwrite a number of variables (i think)
                # moving on to core functions for now, will revisit

                # if player_card_vals[0] != player_card_vals[1]:
                #     print("\nCards must be same value to split!\n")
                #     continue
                # else:
                #     print("\nSplitting {}'s!".format(get_card_val(player_cards[0], True)))
                #     sleep(.02)
                #     total_bet += bet
                #     player1.chip_count -= bet
                #     print("\n{} bets another ${}".format(player1.name, bet))
                #     split_card, split_cards = player_cards.pop(-1), [split_card]
                #     split_player_val, split_vals = player_card_vals.pop(-1), [split_player_val]
                #     print("\nFirst card coming out...")
                #     sleep(.02)
                #     print("Dealer gives {} a {}".format(player1.name, new_card))
                #     new_card, new_card_val = deck.deal_card(), get_card_val(new_card)
                #     split_cards.append(new_card), split_vals.append(new_card_val)
                #     split_val = sum_cards(split_cards)
                #     print("You have {}.".format(player_val)), sleep(.02)
            # double down command 
            elif player_hit in ['double', 'double down', 'd']:
                total_bet += bet
                # add face up or down function later?
                print("\n{} bets another ${}.".format(player1.name, bet))
                sleep(.05)
                if player_val == 12:
                    print("\nDoubling hard 12! May god have mercy on your soul.")
                else:
                    print("\nDealing one more card! Good luck...")
                final_player_val = hit_me(player_cards, player_card_vals, player_val, True)
                # BUG: something wrong here, loop ends when doubling an ace value pair
                if final_player_val in ["Bust", "Win"]:
                    if final_player_val == "Win":
                        player_win(total_bet)   
                        return "Win"     
                else:
                    return final_player_val
            elif player_hit in ['stay', 'stand', 's'] or player_hit in n_responses:
                if type(player_val) is list:
                    final_player_val = max(player_val)
                    return final_player_val
                else:
                    print('\nWike stands with {}.'.format(player_val))
                    final_player_val = player_val
                    print("\n{} stands with {}".format(player1.name, final_player_val))
                    return final_player_val
            elif player_hit in ['hit', 'hit me', 'h'] or player_hit in y_responses:
                final_player_val = hit_me(player_cards, player_card_vals, player_val)
                if final_player_val in ["Bust", "Win"]:
                    if final_player_val == "Win":
                        player_win(total_bet)   
                        break
                    else:     
                        print("Reached play_hand")
                        break
                else:
                    return final_player_val
            else:
                print('\nInvalid input.')
                continue
        dealer_hand(dealer_cards, dealer_card_vals)
        # calc winner

# bed time -- so far should be good

def dealer_hand(dealer_cards, dealer_card_vals):
    print("\nDealer's flips second card..."), sleep(.5)
    dealer_val = sum_cards(dealer_card_vals)
    print("\nDealer flips over {}. Dealer has {}.".format(dealer_cards[0], dealer_val))
    sleep(.2)
    new_dealer_val = 0
    while new_dealer_val < 17:
        new_card = deck.deal_card()
        new_val = get_card_val(new_card)
        dealer_cards.append(new_card)
        dealer_card_vals.append(new_val)
        print("\nDealer draws a {}.".format(new_card)), sleep(.5)
        new_dealer_val = sum_cards(dealer_card_vals)
        try:
            if 21 in new_dealer_val:
                print("\nOof. Dealer hits 21."), sleep(.2)
                return "Dealer Win"
        except:
            if new_dealer_val == 21:
                print("\nOof. Dealer hits 21."), sleep(.2)
                return "Dealer Win"
        if new_dealer_val > 21:
            print("\nDealer busts! Table win!") 
            return "Dealer Bust"
        else:
            try:
                print("\nDealer has {} / {}".format(new_dealer_val[0]),new_dealer_val[1])
                return new_dealer_val
            except:
                print("\nDealer has {}.".format(new_dealer_val))
                return new_dealer_val

def ask_hit_again(player_card_vals, player_cards, player_val):
    while True:
        hit_again = command_parse("\nWould you like to hit again?\n")
        clearFunc()
        if hit_again in ['hit me', 'hit', 'h'] or hit_again in y_responses:
            hit_me(player_cards, player_card_vals, player_val)
        elif hit_again in ['stay', 'stand', 's'] or hit_again in n_responses:
            print("\n{} stands with {}.".format(player1.name, player_val))
            return player_val
        else:
            print("Invalid input.")
            continue
    

def hit_me(player_cards, player_card_vals, player_val, double_down=False):
    print("\nDealing card...")
    sleep(.5)
    new_card = deck.deal_card()
    player_cards.append(new_card)
    new_val = get_card_val(new_card)
    player_card_vals.append(new_val)
    # if two aces
    print("Dealer gives {} a {}".format(player1.name, new_card)), sleep(.2)
    if type(player_val) is list and type(new_val) is list:
        player_val[0] += new_val[0]
        player_val[1] += new_val[1]
        if player_val[1] > 21:
            new_player_val = player_val[0]
            print("\nYou have {}".format(new_player_val))
            if double_down == True:
                return new_player_val
            else:
                ask_hit_again(player_card_vals, player_cards, new_player_val)
        elif 21 in player_val:
            print("\n21!!! You win!")
            return "Win"
        elif player_val[0] < 21 and player_val[1] < 21:
            print("\nYou have {} / {}".format(player_val[0]),player_val[1])
            if double_down == True:
                return player_val
            else:
                ask_hit_again(player_card_vals, player_cards, player_val)

    # if ace and another card - 
    elif type(player_val) is list and type(new_val) is int:
        player_val[0] += new_val
        player_val[1] += new_val
        if 21 in player_val:
            print("\nDealer gives {} a {}".format(player1.name, new_card))
            print("\n21!!! You win!")
            return "Win"
        elif player_val[0] < 21 and player_val[1] < 21:
            if double_down == True:
                return player_val
            else:
                ask_hit_again(player_card_vals, player_cards, player_val)
        elif player_val[1] > 21:
            new_player_val = player_val[0]
            if double_down == True:
                return new_player_val
            else:
                print("\nYou have {}.".format(player_val))
                ask_hit_again(player_card_vals, player_cards, new_player_val)
    elif type(player_val) is int and type(new_val) is list:
        new_player_val = [(player_val+new_val[0]), (player_val+new_val[1])]
        if 21 in new_player_val:
            print("\nDealer gives {} a {}".format(player1.name, new_card))
            print("\n21!!! You win!")
            return "Win"
        elif new_player_val[0] < 21 and new_player_val[1] < 21:
            if double_down == True:
                return player_val
            else:
                ask_hit_again(player_card_vals, player_cards, player_val)
        elif new_player_val[1] > 21:
            new_player_val.pop(1)
            if double_down == True:
                return new_player_val
            else:
                ask_hit_again(player_card_vals, player_cards, new_player_val) 
    # no aces - stable
    else:
        player_val += new_val
        print("\nDealer gives {} a {}".format(player1.name, new_card))
        if player_val == 21:
            print("\n21!!! You win!")
            return "Win"
        elif player_val > 21:
            print("\nYou have {}. You bust!".format(player_val))
            print("Did not reach play_hand")
            return "Bust"
        else:
            print_player_cards(player_cards)
            print("\nYou have {}".format(player_val))
            if double_down == True:
                return player_val
            else:
                print("Wildcard bitch!")
                ask_hit_again(player_card_vals, player_cards, player_val)
             

def welcome_msg():
    sleep(.5)
    print("""\n
    What up, {}! The game is 50 / 500 Blackjack. 

    The minimum bet is $50 and the max bet is $100.\n
    I'm a big noob in this is currently broken as fuck,
    but we're getting there.\n
    Enjoy =)
    """.format(player1.name)), sleep(.5)

# gameplay loop

while True:
    clearFunc()
    welcome = command_parse("\n\nWelcome! What is your name?: \n")
    player1 = Player(welcome)
    welcome_msg()
    is_ready = command_parse("\nReady to play?\n")
    clearFunc()
    if is_ready == "n":
        killswitch()
    else:
        clearFunc()
        print("\nShuffling cards...\n")
        sleep(.05)
        # get bets and deal cards -- turn into sep function?
        deck = Deck(3)
        deck.shuffle(7)
        while True:
            player_cards = []
            dealer_cards = []
            players = [player1.name]
            hand = {}
            bet = get_bet()
            print("\n{} bets ${}...\n".format(player1.name, bet)), sleep(.5) 
            clearFunc()
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
            if player1.chip_count > 0:
                play_again = command_parse("\nPlay another hand?\n") 
                clearFunc()
                if play_again in y_responses:
                    print("\n{}'s current chip count: {}".format(player1.name, player1.chip_count))
                    continue
                else:
                    killswitch()
            else:
                print("\nYou're out of chips!\nYou can find an ATM every 6 feet. Surcharge only $99.99 for a limited time!!!")
                clearFunc()
                print("\n\n\n\n\n\n\n\n\nMAY GOD HAVE MERCY ON YOUR SOUL.")
                killswitch()





        
        
