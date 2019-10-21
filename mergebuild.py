import random

AANTAL = 100
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUWVXYZ'
NUMBERS = '0123456789'

l = []
for _ in range(AANTAL):
    l.append(';'.join((''.join(random.sample(LETTERS, 3) + random.sample(NUMBERS, 6)),
                       '%d' % random.randint(0,9999))))

print(*l, sep='\n')