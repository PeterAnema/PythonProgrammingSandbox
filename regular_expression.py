import re

regex_str = input('Geef een regular expression: ')
regex = re.compile(regex_str)

s = input('Geef een string: ')

matches = regex.findall(s)

if matches:
    print('Found a match:', matches, sep='\n')
else:
    print('Can not find a match!')
