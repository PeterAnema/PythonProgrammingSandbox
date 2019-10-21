import random

# number of cards to deal
n = 7

# create tuples with suits and ranks
SUITS = ('♣', '♢', '♡', '♠')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')

# create a deck with list comprehension
deck = [r + s for s in SUITS for r in RANKS]

# shuffle the deck (with random.shuffle())
random.shuffle(deck)

# take 5 cards off the deck (with pop()) and put in a hand
hand = [deck.pop() for __ in range(n)]

# sort the card according to ranking in suits and ranks
hand.sort(key = lambda card: (SUITS.index(card[-1:]), RANKS.index(card[:-1])))

# show the cards in hand
print(*hand)

# check if cards have been removed from deck
print("There are now %d cards in het deck" % len(deck))
