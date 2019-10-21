filename = 'meisjesnamen.txt'

with open(filename) as f:

    for linenr, line in enumerate(f, 1):
        print(linenr, line.rstrip('\n'))
