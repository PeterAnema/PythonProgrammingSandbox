filename = 'ca-500.csv'

with open(filename, 'r') as fin:
    with open('out.csv', 'w') as fout:

        headers = fin.readline().rstrip().split(';')

        for line in fin:

            values = line.rstrip().split(';')

            d = dict(zip(headers, values))

            if d['city'] == 'Montreal':

                print('%-10s %-10s %-10s %s' % (d['first_name'],
                                                d['last_name'],
                                                d['city'],
                                                d['email']))

                s = ','.join((d['first_name'],
                            d['last_name'],
                            d['city'],
                            d['email']))
                fout.write(s + '\n')
