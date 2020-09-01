names = []

while True:
    name = input('Enter a name: ')
    if name:
        names.append(name)
    else:
        break

filename = 'stored_names.txt'

try:

    print('\nStoring names in %s' % filename)
    with open(filename, 'a') as f:
        for name in names:
            f.write('%s\n' % name)

    print('\nReading names:')
    with open(filename) as f:
        for line in f:
            name = line.rstrip('\n')
            print(name)

except OSError:
    print('There was a problem storing the names in a file')







