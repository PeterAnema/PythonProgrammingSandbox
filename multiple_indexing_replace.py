filename = 'multiple_indexing_data.csv'

with open(filename) as  f:
    header = f.readline().rstrip('\n')
    headers = tuple(header.split(','))

    for line in f:
        line = line.rstrip('\n')
        columns = tuple(line.split(','))

        print(columns)

        converted = tuple([item.replace('f2', 'p2') for item in columns])

        print(converted)