import re

filename = 'demo.txt'

with open(filename, 'r') as f:

    for line in f:
        if re.search(';5', line):
            print(line.strip())

