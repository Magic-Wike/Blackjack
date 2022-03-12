# # # ## a pile of junk, ignore
# import random

# class Deck:
#     card_names = ['Two of Clubs', 'Two of Spades', 'Two of Diamonds', 'Two of Hearts', 'Three of Clubs', 'Three of Spades', 'Three of Diamonds', 'Three of Hearts', 'Four of Clubs', 'Four of Spades', 'Four of Diamonds', 'Four of Hearts', 'Five of Clubs', 'Five of Spades', 'Five of Diamonds', 'Five of Hearts', 'Six of Clubs', 'Six of Spades', 'Six of Diamonds', 'Six of Hearts', 'Seven of Clubs', 'Seven of Spades', 'Seven of Diamonds', 'Seven of Hearts', 'Eight of Clubs', 'Eight of Spades', 'Eight of Diamonds', 'Eight of Hearts', 'Nine of Clubs', 'Nine of Spades', 'Nine of Diamonds', 'Nine of Hearts', 'Ten of Clubs', 'Ten of Spades', 'Ten of Diamonds', 'Ten of Hearts', 'Jack of Clubs', 'Jack of Spades', 'Jack of Diamonds', 'Jack of Hearts', 'Queen of Clubs', 'Queen of Spades', 'Queen of Diamonds', 'Queen of Hearts', 'King of Clubs', 'King of Spades', 'King of Diamonds', 'King of Hearts', 'Ace of Clubs', 'Ace of Spades', 'Ace of Diamonds', 'Ace of Hearts']
#     card_values = {'Two' : 2, 'Three': 3, 'Four' : 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 10]}

#     def __init__(self, num_shoes=1):
#         self.cards = self.generate_deck(num_shoes)
#         self.shoe_size = str(num_shoes)
#         pass

#     def generate_deck(self, num_shoes=1):
#         deck = []
#         for i in range(num_shoes):
#             for card in self.card_names:
#                 deck.append(card)
#             random.shuffle(deck)
#         return deck

#     def deal_card(self, num_cards=1):
#         for i in range(num_cards):
#             random_index = random.randint(1, len(self.cards)-1)
#             random_card = self.cards[random_index]
#         return random_card        


# deck = Deck()

# def get_card_val(card, get_name=False):
#     card_val = 0
#     for key in deck.card_values.keys():
#         if card.startswith(key):
#             if get_name == True:
#                 split_card = card.split()
#                 card_name = split_card[0]
#                 return card_name
#             else:
#                 card_val = deck.card_values[key]
#                 return card_val

# print(get_card_val("Ace of Diamonds"))

# new_dealer_val = [[1, 11], 7]

# def testicles(val):
#     for val in new_dealer_val:
#         print(val)
#         if type(val) is list:
#             for n in val:
#                 print(n)
#                 if n+new_dealer_val[1] > 17 and n+new_dealer_val[1] <= 21:
#                     final_dealer_val = n+new_dealer_val[1]
#                     print("\nDealer stands with {}".format(final_dealer_val))
#                     return final_dealer_val  

# print(testicles(new_dealer_val))
final_player_val = "Bust"

if final_player_val in ["Bust", "Win"]:
        print("3",final_player_val)
        