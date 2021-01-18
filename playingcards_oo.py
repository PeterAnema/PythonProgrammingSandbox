from demo_random import shuffle

SUITS = ('♣', '♢', '♡', '♠')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')

class Card:
    """A playing card"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s %s' % (self.suit, self.rank)
    def __repr__(self):
        return 'Card("%s", "%s")' % (self.suit, self.rank)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        return SUITS.index(self.suit) < SUITS.index(other.suit) or \
               (self.suit == other.suit and RANKS.index(self.rank) < RANKS.index(other.rank))
    def __gt__(self, other):
        return SUITS.index(self.suit) > SUITS.index(other.suit) or \
               (self.suit == other.suit and RANKS.index(self.rank) > RANKS.index(other.rank))
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)
    
    def __hash__(self):
        return (self.suit, self.rank).__hash__()

class Cards:
    """A set of cards"""

    def __init__(self, cards=()):
        self._cards = list(cards)

    def __str__(self):
        return '   '.join(map(str, self._cards))
    def __repr__(self):
        return '[' + ','.join(map(repr, self._cards)) + ']'

    def __len__(self):
        return len(self._cards)
    def __getitem__(self, key):
        return self._cards[key]
    def __delitem__(self, key):
        del self._cards[key]

    def __iter__(self):
        self.__index = 0
        return self
    def __next__(self):
        self._cards += 1
        if self.__index >= len(self._cards):
            raise StopIteration
        return self._cards[self.__index]

    def pop(self, key=None):
        return self._cards.pop(key) if key else self._cards.pop()


class Deck(Cards):
    """A deck of cards"""

    def __init__(self):
        super().__init__([Card(s,r) for s in SUITS for r in RANKS])

    def __str__(self):
        return 'Deck met %d kaarten' % len(self)
    def __repr__(self):
        return 'Deck() - %d cards' % len(self)

    def shuffle(self):
        shuffle(self._cards)

    def deal(self, n = 1):
        dealt = []
        for i in range(0, n):
            dealt.append( self.pop() )
        return dealt



class Hand(Cards):
    """The cards in your hand"""

    def __init__(self, cards, player='Anoniem'):
        super().__init__(sorted(cards))
        self.__player = player

    def __str__(self):
        return '%s:  %s' % (self.__player,  super().__str__())
    def __repr__(self):
        return 'Hand(%s, %s)' % (super().__repr__(), self.__player)


#-----------------------------------------------------------------------------------------------------------
# Client code

if __name__ == '__main__':

    deck = Deck()
    deck.shuffle()

    print(Hand(deck.deal(13), player='Speler 1'))
    print(Hand(deck.deal(13), player='Speler 2'))
    print(Hand(deck.deal(13), player='Speler 3'))
    print(Hand(deck.deal(13), player='Speler 4'))

