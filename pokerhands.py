#!/usr/bin/env python3
import collections
import itertools
import demo_random

SUITS = ('♣', '♢', '♡', '♠')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')

class card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __repr__(self):
        return "%s %s" % (self.rank, self.suit)


class deck(set):
    def __init__(self):
        for rank, suit in itertools.product(RANKS, SUITS):
            self.add(card(rank, suit))
    def get_card(self):
        a_card = demo_random.sample(self, 1)[0]
        self.remove(a_card)
        return a_card
    def get_hand(self, number_of_cards=5):
        if number_of_cards <= len(self):
            hand = [self.get_card() for __ in range(number_of_cards)]
            hand.sort(key=lambda card: (SUITS.index(card.suit), RANKS.index(card.rank)))
            return poker_hand(hand)
        else:
            raise NotImplementedError


class poker_hand():

    def __init__(self, cards):
        self.cards = list(cards)

    def __repr__(self):

        rank_dict = collections.defaultdict(int)
        suit_dict = collections.defaultdict(int)
        for my_card in self.cards:
            rank_dict[my_card.rank] += 1
            suit_dict[my_card.suit] += 1

        # Nothing
        short_desc = "Nothing"

        # Pair
        if len(rank_dict) == 4:
            short_desc = "One pair"

        # Two pair or 3-of-a-kind
        elif len(rank_dict) == 3:
            if 3 in rank_dict.values():
                short_desc ="Three of a kind"
            else:
                short_desc ="Two pair"

        # Full house or 4-of-a-kind
        elif len(rank_dict) == 2:
            if 2 in rank_dict.values():
                short_desc ="Full house"
            else:
                short_desc ="Four of a kind"
        else:

            # Flushes and straights
            straight, flush = False, False
            if len(suit_dict) == 1:
                flush = True
            min_rank = min([RANKS.index(x) for x in rank_dict.keys()])
            max_rank = max([RANKS.index(x) for x in rank_dict.keys()])
            if int(max_rank) - int(min_rank) == 4:
                straight = True

            # Ace can be low
            low_straight = set(("Ace", "2", "3", "4", "5"))
            if not set(rank_dict.keys()).difference(low_straight):
                straight = True
            if straight and not flush:
                short_desc ="Straight"
            elif flush and not straight:
                short_desc ="Flush"
            elif flush and  straight:
                short_desc ="Straight flush"

        enumeration = "  ".join([str(card) for card in self.cards])
        return "%-40s %s" % (enumeration, short_desc)

# --------------------------------------------------------------------

d=deck()
for i in range(10):
    print(d.get_hand())
