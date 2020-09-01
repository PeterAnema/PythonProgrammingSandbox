import re

filename = 'jongensnamen.txt'

with open(filename) as f:

    # contents = f.read()
    # print(contents)

    # lines = contents.split('\n')

    for line in f:
        line = line.strip()
        if re.search('S.*', line):
            print(line)
