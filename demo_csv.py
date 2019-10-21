filename = 'ca-500.csv'

with open(filename, 'r') as f:

    headers = f.readline().strip().split(';')

    for line in f:

        values = line.strip().split(';')

        d = dict(zip(headers, values))

        if d['city'] == 'Montreal':

            print('%-10s %-10s %-10s %s' % (d['first_name'],
                                            d['last_name'],
                                            d['city'],
                                            d['email']))
