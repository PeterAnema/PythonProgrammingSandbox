import os
import re

skip = int(input('Hoeveel regels wil je overslaan? : '))
r = input('Waar wil je op zoeken (regex)? : ')
regex = re.compile(r)

with open('log.txt') as f:

    for nr, line in enumerate(f):
        if nr < skip:
            continue
        else:
            if regex.search(line):
                kolommen = line.strip().split('\t')
                if len(kolommen) > 1:
                    print("{:<10}: {}".format(nr, line))
                else:
                    print(line)

