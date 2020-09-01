filename = 'demo_open.txt'

with open(filename) as f:

    for line in f:
        print(line.rstrip())

