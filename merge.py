files = ['merge1.csv', 'merge2.csv', 'merge3.csv']
file_merged = 'merged.csv'
sep = ';'
missing = '-'

dicts = []

for file in files:
    with open(file) as f:
        d = {}
        for line in f:
            line = line.rstrip()
            cols = line.split(sep)
            key = cols[0]
            d[key] = sep.join(cols[1:])
        dicts.append(d)

keys = set()
for d in dicts:
    keys.update(d.keys())

d_merged = dict()
for k in keys:
    d_merged[k] = sep.join([d.get(k,missing) for d in dicts])

with open(file_merged, 'w') as f:
    for item in d_merged.items():
        line = sep.join(item)
        f.write(line + '\n')








