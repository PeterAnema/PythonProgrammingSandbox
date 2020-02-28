filename = "ca-500.csv"

with open(filename) as f:

    headers = f.readline().rstrip("\n").split(';')
    print(headers)

    for line in f:
        columns = line.rstrip("\n").split(';')

        d = dict(zip(headers, columns))

        if d['city'] in ('Montreal', 'Vancouver'):

            print("{:10} {:15} {:20} {:30}".format(d['first_name'],
                                                   d['last_name'],
                                                   d['city'],
                                                   d['email']))

