import random
import sys
import os
import random_names # for CPU players later
from time import sleep

# global variables 

y_responses = ['y', 'yes', 'ya', 'yup', 'send it', 'hit me']
n_responses = ['n', 'no', 'nope', 'nah']
quit_commands = ['quit', 'exit', 'x', 'bye']
hand_commands = ['hit', 'h', 'hit me', 'double', 'd', 'double down', 'stay', 'stand', 's', 'split']
user_commands = {'chips': 'return current # of player chips', 'commands / cmd': 'show commands list',}
userOS = str(sys.platform)

#class defintions 

class Deck:
    card_names = ['Two of Clubs', 'Two of Spades', 'Two of Diamonds', 'Two of Hearts', 'Three of Clubs', 'Three of Spades', 'Three of Diamonds', 'Three of Hearts', 'Four of Clubs', 'Four of Spades', 'Four of Diamonds', 'Four of Hearts', 'Five of Clubs', 'Five of Spades', 'Five of Diamonds', 'Five of Hearts', 'Six of Clubs', 'Six of Spades', 'Six of Diamonds', 'Six of Hearts', 'Seven of Clubs', 'Seven of Spades', 'Seven of Diamonds', 'Seven of Hearts', 'Eight of Clubs', 'Eight of Spades', 'Eight of Diamonds', 'Eight of Hearts', 'Nine of Clubs', 'Nine of Spades', 'Nine of Diamonds', 'Nine of Hearts', 'Ten of Clubs', 'Ten of Spades', 'Ten of Diamonds', 'Ten of Hearts', 'Jack of Clubs', 'Jack of Spades', 'Jack of Diamonds', 'Jack of Hearts', 'Queen of Clubs', 'Queen of Spades', 'Queen of Diamonds', 'Queen of Hearts', 'King of Clubs', 'King of Spades', 'King of Diamonds', 'King of Hearts', 'Ace of Clubs', 'Ace of Spades', 'Ace of Diamonds', 'Ace of Hearts']
    card_values = {'Two' : 2, 'Three': 3, 'Four' : 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 11]}

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

# utility functions, input handling 

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

def welcome_msg():
    sleep(.5)
    print("""\n
    What up, {}! The game is 50 / 500 Blackjack. 

    The minimum bet is $50 and the max bet is $100.\n
    I'm a big noob in this is currently broken as fuck,
    but we're getting there.\n
    Enjoy =)
    """.format(player1.name)), sleep(.5)

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
        raw_bet = input("\nPlace your bets! (try: 'rebet' / 'r'):\n")
    #    clearFunc()
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
                if player1.last_bet <= player1.chip_count: 
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
            elif bet >= player1.chip_count:
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

def sum_cards(card_list, player_val=0):  
    # will return list if multiple values under 21
    print("Card list", card_list)
    if not player_val == 0:
        new_card = card_list[-1]
        new_vals = [player_val, new_card]
    else:
        new_vals = card_list
    print("1 new_vals", new_vals)
    card1 = new_vals[0]
    card2 = new_vals[1]
    if type(card1) is list and type(card2) is list:
        sum1 = card1[0] + card2[0]
        sum2 = card1[1] + card2[0]
        if sum2 == 21:
            final_val = sum2
        else:
            final_val = [sum1, sum2]
        print("2 new_vals", final_val)
        return final_val
    elif type(card1) is list and type(card2) is int:
        sum1 = card1[0] + card2
        sum2 = card1[1] + card2
        if sum2 == 21 or sum1 == 21:
            final_val = 21
        elif sum2 > 21:
            final_val = sum1
        else:
            final_val = [sum1, sum2]
        return final_val
        print("3 new_vals", final_val)
    elif type(card1) is int and type(card2) is list:
        sum1 = card1 + card2[0]
        sum2 = card1 + card2[1]
        if sum2 == 21 or sum1 == 21:
            final_val = 21
        elif sum2 > 21:
            final_val = sum1
        else:
            final_val = [sum1, sum2]
        return final_val
        print("4 new_vals", final_val)
    else:
        if type(new_vals) is list:
            final_val = sum(new_vals)
        else:
            final_val = new_vals
        print("5 new_vals", final_val)
        return final_val

# dealer hand, stands w/ 17 or above. returns final dealer val or dealer win/bust

def dealer_hand(dealer_cards, dealer_card_vals):
    print("\nDealer's flips second card..."), sleep(.5)
    first_dealer_val = sum_cards(dealer_card_vals)
    if type(first_dealer_val) is int and first_dealer_val > 17:
        final_dealer_val = first_dealer_val
        print("\nDealer stands with {}".format(final_dealer_val))
        sleep(.5)
        return final_dealer_val
    elif type(first_dealer_val) is list:
        print("first_Dealer_val", first_dealer_val)
        for val in first_dealer_val:
            if val > 17 and val < 21:
                final_dealer_val = val
                print("\nDealer stands with {}".format(final_dealer_val))
                sleep(.5)
                return final_dealer_val
            else:
                pass
    else:
        try:
            print("\nDealer has {}".format(first_dealer_val))
            sleep(.5)
        except:
            print("\nDealer has {} / {}".format(first_dealer_val[0], first_dealer_val[1]))
            sleep(.5)
        finally:
            new_dealer_val = first_dealer_val
            try:
                high_dealer_val = max(new_dealer_val)
            except TypeError:
                high_dealer_val = new_dealer_val
            while high_dealer_val < 17:
                new_card = deck.deal_card()
                new_val = get_card_val(new_card)
                dealer_cards.append(new_card)
                dealer_card_vals.append(new_val)
                print("\nDealer draws a {}.".format(new_card)), sleep(.5)
                new_dealer_val = sum_cards(dealer_card_vals, new_dealer_val)
                try:
                    if 21 in new_dealer_val:
                        print("\nOof. Dealer hits 21."), sleep(.2)
                        return "Dealer Win"
                except TypeError:
                    if new_dealer_val == 21:
                        print("\nOof. Dealer hits 21."), sleep(.2)
                        return "Dealer Win"
                try:
                    if new_dealer_val > 21:
                        print("\nDealer busts with {}! Table win!".format(new_dealer_val)) , sleep(.5)
                        return "Dealer Bust"
                        
                except TypeError:
                    if all(i>21 for i in new_dealer_val) == True:
                        print("\nDealer busts with {}! Table win!".format(new_dealer_val)), sleep(.5)
                        return "Dealer Bust"    
                else:
                    try:
                        print("\nDealer has {} / {}".format(new_dealer_val[0]),new_dealer_val[1])
                        high_dealer_val = max(new_dealer_val)
                    except TypeError:
                        print("\nDealer has {}.".format(new_dealer_val))
                        high_dealer_val = new_dealer_val
        return new_dealer_val
    
def calc_winner(final_dealer_val, final_player_val):
    print("Dealer", final_dealer_val)
    print("Player", final_player_val)
    if final_player_val == final_dealer_val:
        return "Push"
    elif final_player_val > final_dealer_val:
        return "Player Win"
    elif final_player_val < final_dealer_val:
        return "Dealer Win"

def player_win(bet, is_bj=False):
    if is_bj == True:
        print("\nYou have blackjack!")
        bj_win = bet + (bet * 1.5)
        print("\nYou win ${:.2f}!".format(bj_win))
        player1.chip_count += bj_win
    else:
        reg_win = bet * 2
        print("\nYou win ${:.2f}!".format(reg_win))
        player1.chip_count += reg_win     

def print_player_cards(player_cards):
    print("\n{}'s cards:".format(player1.name))
    for card in player_cards:
        print(str(card))

def print_player_val(new_player_val):
    try:
        print("\nYou have {}/{}.".format(new_player_val[0], new_player_val[1]))
    except TypeError:
        print("\nYou have {}".format(new_player_val))

# first level of the hand. initial hit/stand/double/etc. returns final player value and accrued bets

def play_hand(player_cards, player_card_vals, player_val, bet):
    total_bet = bet
    while True:
        if player_val == 21 or player_val == [11, 21]:
            break
        else:
            try:
                print("You have {} / {}".format(player_val[0], player_val[1]))
            except:
                print("You have {}".format(player_val))
            player_hit = command_parse("\nWould you like to hit? (try: 'hit me', 'double down', 'stand')\n")
        #    clearFunc()
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
                player1.chip_count -= bet
                # add face up or down function later?
                print("\n{} bets another ${}.".format(player1.name, bet))
                sleep(.05)
                if player_val == 12:
                    print("\nDoubling hard 12! May god have mercy on your soul.")
                else:
                    print("\nDealing one more card! Good luck...")
                new_player_val = hit_me(player_cards, player_card_vals, player_val, True)
                # BUG: something wrong here, loop ends when doubling an ace value pair
                if new_player_val in ["Bust", "Win"]:
                    if new_player_val == "Win":
                        player_win(total_bet) 
                break
            elif player_hit in ['stay', 'stand', 's'] or player_hit in n_responses:
                if type(player_val) is list:
                    new_player_val = max(player_val)
                    print("\n{} stands with {}".format(player1.name, new_player_val))
                    break
                else:
                    new_player_val = player_val
                    print("\n{} stands with {}".format(player1.name, new_player_val))
                    break
            elif player_hit in ['hit', 'hit me', 'h'] or player_hit in y_responses:
                
                new_player_val = hit_me(player_cards, player_card_vals, player_val)
                print("new_player_val", new_player_val)
                try:
                    if new_player_val == "Win" or new_player_val == 21:
                        print("Reached play_hand")
                        player_win(total_bet)   
                        break
                    elif new_player_val == "Bust" or new_player_val > 21:  
                        print("\nYou lose ${}.".format(total_bet))
                        break
                    else:
                        final_player_val = ask_hit_again(player_card_vals, player_cards, new_player_val)
                        # while True:
                        #     if next_player_val in ["Bust"]:
                        #         print("\nYou lose ${}.".format(total_bet))
                        #         break
                        #     elif if next_player_val in ["Win", 21]:
                        #         print("Reached play_hand")
                        #         player_win(total_bet)   
                        #         break
                        #     else:
                        #         continue
                        return final_player_val, total_bet
                except TypeError:
                    if new_player_val in ["Win", 21]:
                        print("Reached play_hand")
                        player_win(total_bet)   
                        break
                    elif new_player_val in ["Bust"]:  
                        print("\nYou lose ${}.".format(total_bet))
                        break
                    else:
                        final_player_val = ask_hit_again(player_card_vals, player_cards, new_player_val)
                        return final_player_val, total_bet
            else:       
                print('\nInvalid input.')
                continue
    return new_player_val, total_bet            
                
def ask_hit_again(player_card_vals, player_cards, player_val):
    while True:
        print('You have {}.'.format(player_val))
        hit_again = command_parse("\nWould you like to hit again?\n")
    #    clearFunc()
        if hit_again in ['hit me', 'hit', 'h'] or hit_again in y_responses:
            next_player_val = hit_me(player_cards, player_card_vals, player_val)
            if next_player_val in ["Win", "Bust"]:
                return next_player_val
            else:
                final_player_val = ask_hit_again(player_card_vals, player_cards, next_player_val)
                return final_player_val
        elif hit_again in ['stay', 'stand', 's'] or hit_again in n_responses:
            if type(player_val) is list:
                final_player_val = max(player_val)
                print("\n{} stands with {}.".format(player1.name, final_player_val))
                player_stand = True
                return final_player_val
            else:
                final_player_val = player_val
                print("\n{} stands with {}.".format(player1.name, final_player_val))
                player_stand = True
                return final_player_val
        else:
            print("Invalid input.")
            continue

# will return "Win", "Bust" or final_player_val
def hit_me(player_cards, player_card_vals, player_val, double_down=False, count=0):
    print("\nDealing card...")
    sleep(.5)
    new_card = deck.deal_card()
    player_cards.append(new_card)
    new_val = get_card_val(new_card)
    player_card_vals.append(new_val)
    print("\nDealer gives {} a {}".format(player1.name, new_card)), sleep(.2)
    new_player_val = sum_cards(player_card_vals, player_val)
    try:
        if new_player_val == 21:
            print("\n21!!! You win!"), sleep(.5)
            final_player_val = "Win"
            return final_player_val
        elif new_player_val > 21:
            print("\nYou have {}.".format(new_player_val)), sleep (.5)
            print("\nYou bust! Sorry!"), sleep(.5)
            final_player_val = "Bust"
            return final_player_val
        else:
            final_player_val = new_player_val
            print_player_val(final_player_val)
            return final_player_val
    except TypeError:
        if 21 in new_player_val:
            print("\n21!!! You win!")
            final_player_val = "Win"
            print("1", final_player_val) 
            return final_player_val
        elif all(i>21 for i in new_player_val) == True:
            print("\nYou bust! Sorry!"), sleep(.5)
            final_player_val = "Bust"
            print("1",final_player_val)    
            return final_player_val
        else:
            final_player_val = new_player_val
            print_player_val(final_player_val)
            return final_player_val    

def ask_play_again():
    while True:
        if player1.chip_count > 0:
            play_again = command_parse("\nPlay another hand?\n") 
            if play_again in y_responses:
                print("\n{}'s current chip count: {}".format(player1.name, player1.chip_count))
                blackjack()
            elif play_again in n_responses:
                killswitch()
            else:
                print("\nInvalid input.")
                continue   
        else:
                print("\nYou're out of chips!\nYou can find an ATM every 6 feet. Surcharge only $99.99 for a limited time!!!")
            #    clearFunc()
                print("\n\n\n\nMAY GOD HAVE MERCY ON YOUR SOUL.")
                killswitch()

def blackjack():
    while True:
        player_cards = []
        dealer_cards = []
        players = [player1.name]
        hand = {}
        bet = get_bet()
        # total_bet = bet
        print("\n{} bets ${}...\n".format(player1.name, bet)), sleep(.5) 
#           clearFunc()
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
        for player in hand:
            player_card_vals = []
            for card in hand[player]:
                player_card_vals.append(get_card_val(card))
        print("player_card_vals:", player_card_vals)
        player_val = sum_cards(player_card_vals)
        print("player_val:", player_val)
        try:
            if 21 in player_val:
                player_win(bet, is_bj=True)
                break
        except:
            if player_val == 21:
                player_win(bet, is_bj=True)   
                break
        dealer_card_vals =[]
        for card in dealer_cards:
            card_val = get_card_val(card)
            dealer_card_vals.append(card_val)
        print("dealer_card_vals:", dealer_card_vals)
        dealer_val = sum_cards(dealer_card_vals)
        print("dealer_val", dealer_val)
        print("\n\nDealer checking for 21...\n")
        sleep(2)
        if dealer_val == 21:
            print("\nDealer has blackjack!")
            sleep(.05)
            print("\nEveryone loses =(")
            if player_val == 21:
                pass
            else:
                print("\nYou lose ${:.2f}".format(bet))
            ask_play_again()
        else:
            print("\nNobody home!\n")
            print("\nDealer shows: {}".format(dealer_cards[1]))
            results = play_hand(player_cards, player_card_vals, player_val, bet)
            print("results", results)
            final_player_val = results[0]
            total_bet = results[1]
            resolved = ["Win", "Bust"]
            if final_player_val in resolved:
                ask_play_again()
            else:
                final_dealer_val = dealer_hand(dealer_cards, dealer_card_vals)
                if final_dealer_val == "Dealer Bust":
                    player_win(total_bet)
                    sleep(.5)
                elif final_dealer_val == "Dealer Win":
                    print("You lose ${}. Better luck next time!".format(total_bet))
                    sleep(.5)
                else:
                    winner = calc_winner(final_dealer_val , final_player_val)
                    if winner == "Dealer Win":
                        sleep(1)
                        print("\nDealer wins with {}. You lose ${}.".format(final_dealer_val, total_bet)), sleep(.5)
                    elif winner == "Player Win":
                        sleep(1)
                        player_win(total_bet)
                        # print("\n{} wins with {}! You win ${}!".format(player1.name, final_player_val, total_bet)), sleep(.5)
                    elif winner == "Push":
                        sleep(1)
                        print("\nPush! You get back your original bet of ${}".format(bet)), sleep(.5)
                        player1.chip_count += bet
                    else:
                        print("\nSomething be broke")
                ask_play_again()

# gameplay loop

while True:
#    clearFunc()
    welcome = command_parse("\n\nWelcome! What is your name?: \n")
    player1 = Player(welcome)
    welcome_msg()
    is_ready = command_parse("\nReady to play?\n")
 #   clearFunc()
    if is_ready == "n":
        killswitch()
    else:
 #       clearFunc()
        print("\nShuffling cards...\n")
        sleep(.05)
        # get bets and deal cards -- turn into sep function?
        deck = Deck(3)
        deck.shuffle(7)
        blackjack()
        




