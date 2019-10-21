"""
Kies een willekeurige kaart

@author: Peter
"""

import random

kleur = ('klaver','ruiten','harten','schoppen')
rang = ('2','3','4','5','6','7','8','9','10','Boer','Vrouw','Heer','Aas')

kaarten = [k + ' ' + r for r in rang for k in kleur]

random.shuffle(kaarten)

hand = []
for n in range(5):
    hand.append(kaarten.pop())

print(hand)