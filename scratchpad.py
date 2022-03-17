import random
import sys
import time
import itertools

class Blackjack:
    def __init__(self):
        self.total_bet = 0
        self.dealer_show_card_value = 0
        self.dealer_hole_card_value = 0

    def spinning_cursor(self, wait):
        self.spinner = itertools.cycle(['-', '/', '|', '\\'])
        for _ in range(wait):
            sys.stdout.write(next(self.spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')

    def set_up(self):
        print("Hello! What's your name? ")
        self.name = input()
        self.spinning_cursor(5)
        print(f"\nNice to meet you {self.name}! How much money do you have on you?\n")
        self.money = int(input())
        self.spinning_cursor(5)
        print("\nAlright, let's play some blackjack!\n")

    def cards(self):
        # Player cards
        self.player_card_1 = random.randint(1, 14)
        if self.player_card_1 == 1 or self.player_card_1 == 11:
            self.player_card_1 = "Ace"
        self.player_card_2 = random.randint(1, 14)
        if self.player_card_2 == 1 or self.player_card_2 == 11:
            self.player_card_2 = "Ace"
        self.player_card_3 = random.randint(1, 14)
        if self.player_card_3 == 1 or self.player_card_3 == 11:
            self.player_card_3 = "Ace"
        self.player_card_4 = random.randint(1, 14)
        if self.player_card_4 == 1 or self.player_card_4 == 11:
            self.player_card_4 = "Ace"
            
        # Dealer cards    
        self.dealer_show_card = random.randint(1, 14)
        if self.dealer_show_card == 1 or self.dealer_show_card == 11:
            self.dealer_show_card = "Ace"
        self.dealer_hole_card = random.randint(1, 14)
        if self.dealer_hole_card == 1 or self.dealer_hole_card == 11:
            self.dealer_hole_card = "Ace"

        # Dealer Ace decision: 1 or 11
        if self.dealer_show_card == "Ace" and self.dealer_hole_card != "Ace":
            if self.dealer_hole_card > 10:
                self.dealer_show_card_value == 1
            else:
                self.dealer_show_card_value == 11
        if self.dealer_hole_card == "Ace" and self.dealer_show_card != "Ace":
            if self.dealer_show_card > 10:
                self.dealer_hole_card_value == 1
            else:
                self.dealer_hole_card_value == 11
        if self.dealer_show_card == "Ace" and self.dealer_hole_card == "Ace":
            self.dealer_show_card_value == 11
            self.dealer_hole_card_value == 1
        if self.dealer_show_card != "Ace" and self.dealer_hole_card != "Ace":
            self.dealer_hole_card_value = self.dealer_hole_card
            self.dealer_show_card_value = self.dealer_show_card

    def dealing_the_cards(self):
        self.spinning_cursor(5)
        print("Let's deal some cards.")
        self.spinning_cursor(20)
        print(f"Your cards are: {self.player_card_1} & {self.player_card_2}.")
        self.spinning_cursor(5)
        print(f"The dealer's show card is {self.dealer_show_card}.")
        if self.player_card_1 == "Ace":
            print("Your first card is an Ace. Would you like to count it as 1 or 11?")
            self.player_card_1 = int(input())
            while self.player_card_1 != 1 or self.player_card_1 != 11:
                if self.player_card_1 == 1 or self.player_card_1 == 11:
                    break
                print("Please enter either 1 or 11: ")
                self.player_card_1 = int(input())

        if self.player_card_2 == "Ace":
            print("Your second card is an Ace. Would you like to count it as 1 or 11?")
            self.player_card_2 = int(input())
            while self.player_card_2 != 1 or self.player_card_2 != 11:
                if self.player_card_2 == 1 or self.player_card_2 == 11:
                    break                 
                print("Please enter either 1 or 11: ")
                self.player_card_2 = int(input())

        self.player_score = self.player_card_1 + self.player_card_2

        self.spinning_cursor(10)   
        if self.player_score > 21:
            print("Game over!\nWould you like to start over? yes/no")
            self.start_over = input()
            if self.start_over.lower() == "yes":
                blackjack.initialize()
            else: 
                print("Thanks for playing.")
                sys.exit()

    def betting(self):
        self.spinning_cursor(10)
        print("How much would you like to bet?")
        self.first_bet = int(input())
        while self.first_bet < 0 or self.first_bet > self.money:
            print("Come one man, enter a valid bet.")
            self.first_bet = int(input())
            if self.first_bet >= 0 and self.first_bet <= self.money:
                self.total_bet += self.first_bet
                break   

        if self.player_score < 21:
            print("Would you like another card? 'hit me/pass'")
            self.want_new_card_1 = input()
            if self.want_new_card_1.lower() == "hit me" and self.player_card_3 != "Ace":
                print("Your new card is:")
                self.spinning_cursor(10)   
                print(self.player_card_3)
            elif self.player_card_3 == "Ace":
                print("The card is an Ace. Would you like to count it as 1 or 11?")
                self.player_card_3 = int(input())
                while self.player_card_3 != 1 or self.player_card_3 != 11:
                    if self.player_card_3 == 1 or self.player_card_3 == 11:
                        break                        
                    print("Please enter either 1 or 11: ")
                    self.player_card_3 = int(input())

        self.player_score += self.player_card_3
        
        if self.player_score > 21:
            self.spinning_cursor(10)   
            print("Game over!\nWould you like to start over? Yes/No")
            self.start_over = input()
            if self.start_over.lower() == "yes":
                blackjack.initialize()
            else:
                print("Thanks for playing.")
                sys.exit()

        self.spinning_cursor(10)
        print("How much would you like to bet?")
        self.second_bet = int(input())
        while self.second_bet < 0 or (self.second_bet + self.total_bet) > self.money:
            print("Come one man, enter a valid bet.")
            self.second_bet = int(input())
            if self.second_bet >= 0 and (self.second_bet + self.total_bet) <= self.money:
                self.total_bet += self.second_bet
                break                

        if self.player_score < 21:
            print("Would you like another card? 'hit me/pass'")
            self.want_new_card_2 = input()
            if self.want_new_card_2 == "hit me" and self.player_card_4 != "Ace":
                print(f"Your new card is:")
                self.spinning_cursor(10)   
                print(self.player_card_4)
            if self.player_card_4 == "Ace":
                print("The card is an Ace. Would you like to count it as 1 or 11?")
                self.player_card_4 = int(input())
                while self.player_card_4 != 1 or self.player_card_4 != 11:
                    if self.player_card_4 == 1 or self.player_card_4 == 11:
                        break                      
                    print("Please enter either 1 or 11: ")
                    self.player_card_4 = int(input())
               
        self.player_score += self.player_card_4

        if self.player_score > 21:
            self.spinning_cursor(10)   
            print("Game over!\nWould you like to start over? yes/no")
            self.start_over = input()
            if self.start_over.lower() == "yes":
                blackjack.initialize()
            else:
                print("Thanks for playing.")
                sys.exit()

        self.spinning_cursor(10)
        print("How much would you like to bet?")
        self.third_bet = int(input())
        while self.third_bet < 0 or (self.third_bet + self.total_bet) > self.money:
            print("Come one man, enter a valid bet.")
            self.third_bet = int(input())
            if self.third_bet >= 0 and (self.third_bet + self.total_bet) <= self.money:
                self.total_bet += self.third_bet
                break                

    def results(self):
        self.dealer_score = self.dealer_hole_card_value + self.dealer_show_card_value
        print(f"The dealer's cards are: {self.dealer_show_card} & {self.dealer_hole_card}")
        if self.player_score == 21:
            print(f"Blackjack! You won {self.total_bet*2}.")
            sys.exit()
        elif self.dealer_score == 21:
            print("The dealer has Blackjack. You lose.")
            sys.exit()
        elif self.player_score > 21 and self.dealer_score < 21:
            print("You lose.")
            sys.exit()
        elif self.player_score < 21 and self.dealer_score > 21:
            print(f"You won {self.total_bet*2}.")
            sys.exit()

    def initialize(self):

        self.set_up()
        self.cards()
        self.dealing_the_cards()
        self.betting()
        self.results()

blackjack = Blackjack()
blackjack.initialize()
