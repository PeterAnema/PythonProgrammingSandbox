filename = 'tellen.txt'

with open(filename, 'a') as f:
    for getal in range(1, 11):
        f.write(f'{getal}\n')

print('File is weggeschreven!')

print('File bestaat nu uit de volgende regels"')

with open(filename) as f:
    for line in f:
        print(line.rstrip('\n'))
