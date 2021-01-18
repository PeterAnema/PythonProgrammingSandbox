import demo_random

AANTAL = 100
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUWVXYZ'
NUMBERS = '0123456789'

l = []
for _ in range(AANTAL):
    l.append(';'.join((''.join(demo_random.sample(LETTERS, 3) + demo_random.sample(NUMBERS, 6)),
                       '%d' % demo_random.randint(0, 9999))))

print(*l, sep='\n')