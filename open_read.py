import re

filenames = ['jongensnamen.txt', 'meisjesnamen.txt']

pattern = 'ine$'

for filename in filenames:
    with open(filename) as f:

        for line in f:
            line = line.rstrip('\n')
            if re.search(pattern, line):
                print(line)

