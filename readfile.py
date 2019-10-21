import os
import re

path = '.'

#filename = 'jongensnamen.txt'
filename = 'meisjesnamen.txt'

outfile = 'outfile.txt'

r = input('Waarop wil je filteren? [regular expression]: ')

regex = re.compile(r, re.IGNORECASE)

os.chdir(path)

f = open(filename, 'r')
f_out = open(outfile, 'w')

for linenr, line in enumerate(f):
    if regex.search(line):

        line_out = ('%4d' % linenr)+ ': ' + line.strip()

        print(line_out)
        f_out.write(line_out + '\n')

f.close()
f_out.close()
