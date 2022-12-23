# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 15:21:19 2022

@author: cleed
"""

suit = suits[2]
rank = 'K'
value = 10
print('Your card is: ' + rank + ' of ' + suit)
suits.append('snakes')

#%%

for suit in suits:
    print(suit)
    
for suit in suits:
    print([suit, ranks[0]])
    
for suit in suits:
    for rank in ranks:
        print([suit, rank])
    
#%%

random.shuffle(cards)
card = cards.pop()
print(card)

def deal():
    card = cards.pop()
    return card

#%%

if rank == 'A':
    value = 11
elif rank == 'J' or 'Q' or 'K':
    value = 10
else:
    rank = value
    
#%%
### prior to first refoctor ###
import random

cards = []
suits = ['spades', 'clubs', 'hearts', 'diamonds']
ranks = ['A', '2', '3','4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

def shuffle():
    random.shuffle(cards)        

def deal(number):
    cards_dealt = [] 
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt
    
shuffle()
cards_dealt = deal(2)
card = cards_dealt[0]
rank = card[1]

if rank == 'A':
    value = 11
elif rank == 'J' or 'Q' or 'K':
    value = 10
else:
    rank = value
    
rank_dict = {'rank': rank, 'value': value}

print(rank_dict['rank'], rank_dict['value'])

#%%
### After First Refactor ###

import random

cards = []
suits = ['spades', 'clubs', 'hearts', 'diamonds']
ranks = [{'rank': 'A', 'value': '11'},
         {'rank': '2', 'value': '2'},
         {'rank': '3', 'value': '3'},
         {'rank': '4', 'value': '4'},
         {'rank': '5', 'value': '5'},
         {'rank': '6', 'value': '6'},
         {'rank': '7', 'value': '7'},
         {'rank': '8', 'value': '8'},
         {'rank': '9', 'value': '9'},
         {'rank': '10', 'value': '10'},
         {'rank': 'J', 'value': '10'},
         {'rank': 'Q', 'value': '10'},
         {'rank': 'K', 'value': '10'},
         ]

for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

def shuffle():
    random.shuffle(cards)        

def deal(number):
    cards_dealt = [] 
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt
    
shuffle()
card = deal(1)[0]

print(card[1]['value'])

#%%
### Deck Class & instance testing ###
import random


class deck: 
    def __init__(self):
        self.cards = []
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = [{'rank': 'A', 'value': '11'},
                 {'rank': '2', 'value': '2'},
                 {'rank': '3', 'value': '3'},
                 {'rank': '4', 'value': '4'},
                 {'rank': '5', 'value': '5'},
                 {'rank': '6', 'value': '6'},
                 {'rank': '7', 'value': '7'},
                 {'rank': '8', 'value': '8'},
                 {'rank': '9', 'value': '9'},
                 {'rank': '10', 'value': '10'},
                 {'rank': 'J', 'value': '10'},
                 {'rank': 'Q', 'value': '10'},
                 {'rank': 'K', 'value': '10'},
                 ]
        
        for suit in suits:
            for rank in ranks:
                self.cards.append([suit, rank])
        
    def shuffle(self):
        random.shuffle(self.cards)        
    
    def deal(self, number):
        cards_dealt = [] 
        for x in range(number):
            card = self.cards.pop()
            cards_dealt.append(card)
        return cards_dealt

deck1 = deck()
deck2 = deck()
deck2.shuffle()
print(deck1.cards)
print(deck2.cards)

#%%

### Deck class with if statement checks ###

import random


class deck: 
    def __init__(self):
        self.cards = []
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = [{'rank': 'A', 'value': '11'},
                 {'rank': '2', 'value': '2'},
                 {'rank': '3', 'value': '3'},
                 {'rank': '4', 'value': '4'},
                 {'rank': '5', 'value': '5'},
                 {'rank': '6', 'value': '6'},
                 {'rank': '7', 'value': '7'},
                 {'rank': '8', 'value': '8'},
                 {'rank': '9', 'value': '9'},
                 {'rank': '10', 'value': '10'},
                 {'rank': 'J', 'value': '10'},
                 {'rank': 'Q', 'value': '10'},
                 {'rank': 'K', 'value': '10'},
                 ]
        
        for suit in suits:
            for rank in ranks:
                self.cards.append([suit, rank])
        
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)        
    
    def deal(self, number):
        cards_dealt = [] 
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt
    
deck1 = deck()
deck2 = deck()
deck2.shuffle()
print(deck1.cards)
print(deck2.cards)

#%%
### Card class first creation ###
class card:
    def __init__(self):
        self.suit = 'hearts'
        self.rank = 'A'
        
#%%
### Card class prior to refactor ###
class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank['rank'] + ' of ' + self.suit
    
#%%

### Deck and Card classes created and talking to each other ###
### made for ease for card rank/value transfer to other games ###
import random


class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank']} + ' of ' + {self.suit}"

class deck: 
    def __init__(self):
        self.cards = []
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = [{'rank': 'A', 'value': '11'},
                 {'rank': '2', 'value': '2'},
                 {'rank': '3', 'value': '3'},
                 {'rank': '4', 'value': '4'},
                 {'rank': '5', 'value': '5'},
                 {'rank': '6', 'value': '6'},
                 {'rank': '7', 'value': '7'},
                 {'rank': '8', 'value': '8'},
                 {'rank': '9', 'value': '9'},
                 {'rank': '10', 'value': '10'},
                 {'rank': 'J', 'value': '10'},
                 {'rank': 'Q', 'value': '10'},
                 {'rank': 'K', 'value': '10'},
                 ]
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(card(suit, rank))
        
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)        
    
    def deal(self, number):
        cards_dealt = [] 
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt
    
card1 = card('heats', {'rank': '7', 'value': '7'})
print(card1)
#%%

###hand class###
class hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer
        
    def add_card(self, card_list):
        self.cards.extend(card_list)
        
deck = deck()
deck.shuffle()

hand = hand()
hand.add_card(deck.deal(2))
print(hand.cards[0], hand.cards[1])

#%%

### hand class ###
class hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer
        
    def add_card(self, card_list):
        self.cards.extend(card_list)
        
    def calculate_value(self):
        self.value = 0
        has_ace = False
    
        for card in self.cards:
            card_value = int(card.rank['value'])
            self.value += card_value
            if card.rank['rank'] == 'A':
                has_ace = True
                
        if has_ace and self.value > 21:
            self.value -= 10
            
    def get_value(self):
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        if self.get_value() == 21:
            return print('Blackjack!')
        
    def display(self):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand: ''')
        for card in self.cards:
            print(card)
            
        if not self.dealer:
            print('Value:', self.get_value())
        print()
        
#%%

### hand class inc. dealer ###

class hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer
        
    def add_card(self, card_list):
        self.cards.extend(card_list)
        
    def calculate_value(self):
        self.value = 0
        has_ace = False
    
        for card in self.cards:
            card_value = int(card.rank['value'])
            self.value += card_value
            if card.rank['rank'] == 'A':
                has_ace = True
                
        if has_ace and self.value > 21:
            self.value -= 10
            
    def get_value(self):
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        if self.get_value() == 21:
            return print('Blackjack!')
        
    def display(self, show_all_dealer_cards = False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand: ''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
            and not show_all_dealer_cards and not self.is_blackjack():
                print('hidden')
            else:
                print(card)
            
        if not self.dealer:
            print('Value:', self.get_value())
        print()
    
#%%

###gmae class pre game over###
class game:        
    def play(self):
        self.game_number = 0
        self.games_to_play = 0
       
        while self.games_to_play <= 0:
            try:
                self.games_to_play = int(input('How many games to play? '))
            except:
                print('Please enter a number')
                
        while self.game_number < self.games_to_play:
            self.game_number =+ 1
            
            self.deck = deck()
            self.deck.shuffle()
            
            player_hand = hand()
            dealer_hand = hand(dealer = True)
            
            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
                
            print()
            print('*' * 30)
            print(f"Game {self.game_number} of {self.games_to_play}")
            print('*' * 30)
            player_hand.display()
            dealer_hand.display()
            
        def check_winner(self, player_hand, dealer_hand, game_over = False):
            if player_hand.get_value > 21:
                print('You busted, dealer wins')
                return True
            elif dealer_hand.get_value > 21:
                print('Dealer busted! You win!')
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print('Double Blackjack! Draw game')    
                return True
            elif player_hand.is_blackjack():
                print('You have Blackjack, you win!')
                return True
            elif dealer_hand.is_blackjack():
                print('Dealer has Blackjack, dealer wins!')
                return True
            return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    