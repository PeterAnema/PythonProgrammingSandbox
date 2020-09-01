"""\
Demonstrating the persistance/serialization of a simple dict

Store a dict to file and reload the dict from the file

Methodes: txt, csv, json and pickle

- retain types: string, int, float
- retain order
"""

groceries = {
    "boter": "1 pakje",
    "kaas": "300gr",
    "eieren": 12,
    "fruit": "1,5kg",
}

# or

from collections import OrderedDict

groceries = OrderedDict([
    ("boter", "1 pakje"),
    ("kaas", "300gr"),
    ("eieren", 12),
    ("fruit", "1,5kg"),
])

# -------------------------------------------------------
# Utility functions

def to_string(value, quotechar = '"'):
    s = str(value)
    if s.isnumeric():
        return s
    else:
        return quotechar + s + quotechar

def from_string(s, quotechar ='"'):
    if str(s).isdigit():
        return int(s)
    elif str(s).isnumeric():
        return float(s)
    else:
        return s.strip(quotechar)


# -------------------------------------------------------
# txt

filename = 'demo_persistence.txt'

delimiter = ': '
quotechar = '"'

with open(filename, 'w') as f:
    for t in groceries.items():
        f.write('%s\n' % delimiter.join(map(to_string, t)))

groceries_restored = OrderedDict()
with open(filename) as f:
    for line in f:
        row = line.rstrip('\n').split(': ')
        groceries_restored[from_string(row[0])] = from_string(row[1])

print('txt: ', groceries_restored)


# -------------------------------------------------------
# csv

filename = 'demo_persistence.csv'

import csv

delimiter = ':'
quotechar = '"'

with open(filename, 'w') as f:
    csv_writer = csv.writer(f,
                            delimiter=delimiter,
                            quotechar=quotechar,
                            quoting=csv.QUOTE_NONNUMERIC)

    for t in groceries.items():
        csv_writer.writerow(t)

groceries_restored = OrderedDict()
with open(filename) as f:
    csv_reader = csv.reader(f,
                            delimiter=':',
                            quotechar='"')

    for row in csv_reader:
        groceries_restored[row[0]] = from_string(row[1])

print('csv: ', groceries_restored)


# -------------------------------------------------------
# json

filename = 'demo_persistence.json'

import json

with open(filename, 'w') as f:
    json.dump(groceries, f)

with open(filename) as f:
    groceries_restored = json.load(f, object_pairs_hook=OrderedDict)

print('json: ', groceries_restored)


# -------------------------------------------------------
# pickle

filename = 'demo_persistence.pickle'

import pickle

with open(filename, 'wb') as f:
    pickle.dump(groceries, f)

with open(filename, 'rb') as f:
    groceries_restored = pickle.load(f)

print('pickle: ', groceries_restored)
