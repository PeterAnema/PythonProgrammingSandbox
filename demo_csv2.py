import csv

filename = 'ca-500.csv'

with open(filename, 'r') as f:

    reader = csv.DictReader(f, delimiter=';')

    for d in reader:

        if d['city'] == 'Montreal':

            print('%-10s %-10s %-10s %s' % (d['first_name'],
                                            d['last_name'],
                                            d['city'],
                                            d['email']))
