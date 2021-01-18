import demo_random

# number of cards to deal
n = 5

# create tuples with suits and ranks
SUITS = ('♣', '♢', '♡', '♠')
# SUITS = ('\u2660', '\u2661', '\u2662', '\u2663')
RANKS = tuple('2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(','))

# create a deck with list comprehension
deck = [r + s for s in SUITS for r in RANKS]

print(deck)

# shuffle the deck (with random.shuffle())
demo_random.shuffle(deck)

# take 5 cards off the deck (with pop()) and put in a hand
hand = [deck.pop() for __ in range(n)]

# sort the card according to ranking in suits and ranks
hand.sort(key = lambda card: (SUITS.index(card[-1:]), RANKS.index(card[:-1])))

# show the cards in hand
print(*hand)

# check if cards have been removed from deck
print("There are now %d cards in het deck" % len(deck))
