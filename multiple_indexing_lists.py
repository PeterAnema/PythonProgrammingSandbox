filename = 'multiple_indexing_data.csv'

data = []
with open(filename) as  f:
    header = f.readline().rstrip('\n')
    headers = tuple(header.split(','))

    for line in f:
        line = line.rstrip('\n')
        columns = tuple(line.split(','))
        data.append(columns)

print('%-5s %-5s %-5s' % headers)
for row in data:
    print('%-5s %-5s %-5s' % row)

indexes = [i for i, t in enumerate(data) if t[0]=='w2' and t[1]=='f1']
values = [data[i][2] for i in indexes]

print(indexes)
print(values)


