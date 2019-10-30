filename = 'demo_open.txt'

with open(filename, 'w') as f:

    for linenr in range(1, 11):
        f.write(f'This is line {linenr}\n')

