import random
from selectors import EpollSelector
import random_names
from time import sleep

y_responses = ['y', 'yes', 'ya', 'yup', 'send it', 'hit me']
n_responses = ['n', 'no', 'nope', 'nah']
quit_commands = ['quit', 'exit', 'x', 'bye']



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
            random_index = random.randint(1, len(self.cards))
            random_card = self.cards[random_index]
        return random_card

# def win_calc(dealer_cards, *player_cards):



class Player:

    def __init__(self, name, chip_count=1000, high_roller=False):
        self.name = name
        self.chip_count = chip_count
        self.high_roller = high_roller
        self.bank = 0

    def win(self, amount):
        self.chip_count += amount

    def lose(self, amount):
        if amount > chip_count:
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


def clean_input(string):
    cleaned = string.strip().lower()
    return cleaned 

def killswitch():
    print("Goobye!")
    quit()

def command_parse(user_input):
    while True:
        raw_input = input(user_input)
        if type(raw_input) == int:
            return raw_input
        elif "What is your name?" in user_input:
            if raw_input == "":
                print("Please enter a name!")
                continue
            else:
                 return raw_input
        cleaned = raw_input.strip().lower()
        if cleaned in quit_commands:
            killswitch()
        elif cleaned == "chips":
            try:
                print("You have {} chips.".format(player1.chip_count))
                continue
            except NameError:
                print("Player does not exist. (start a game first)")
                break
        elif cleaned in y_responses:
            return "y"
        elif cleaned in n_responses:
            return "n"
        else: 
            print("Invalid input")
            continue

def get_bet(min=50, max=500):
    while True:
        raw_bet = input("Place your bets!:\n")
        bet = int(raw_bet)
        if bet > max:
            print("Table limit is ${}".format(max))
            continue
        elif bet < min:
            print("Table minimum is ${}".format(min))
            continue
        elif bet > player1.chip_count:
            print("Not enough chips. You currently have ${}".format(player1.chip_count))
            continue
        else:
            return bet




while True:
    
    welcome = command_parse("Welcome! What is your name?: \n")
    player1 = Player(welcome)
    is_ready = command_parse("Ready to play?\n")
    if is_ready == "n":
        killswitch()
    else:
        print("Shuffling cards...\n")
        deck = Deck()
        while True:
            player_cards = []
            dealer_cards = []
            players = [player1.name]
            hand = {}
            bet = get_bet()
            print("{} bets ${}...\n".format(player1.name, bet))
            print("\nCards coming out...\n\n")
            for i in range(2):
                for player in players:
                    rnd_player_card = deck.deal_card()
                    deck.cards.remove(rnd_player_card)
                    rnd_dealer_card = deck.deal_card()
                    deck.cards.remove(rnd_dealer_card)
                    player_cards.append(rnd_player_card)
                    dealer_cards.append(rnd_dealer_card)
                print("Dealer gives {} a {}...\n".format(player1.name, rnd_player_card))
                print("Dealer draws a card...")
            print("Dealer shows {}".format(dealer_cards[1]))
            hand["Dealer"] = dealer_cards
            for player in players:
                hand[player] = player_cards
            print(player_cards)
            print(dealer_cards)
            print(hand)
        



        
        
