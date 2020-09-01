import re

names = [('Mateusz','Dept A'),
         ('Hayley','Dept B'),
         ('Despina','Dept A'),
         ('Kumar','Dept D'),
         ('Vera','Dept A')]

def f(t):
    return re.match('([dD]ept A|[aA]fd A)', t[1])

filtered = list(filter(f, names))

print(names)
print(filtered)

print(sorted(names, key = lambda e: e[1][-1]))

for s in map(lambda e: e[1] + ': ' + e[0], names):
    print(s)

short_names = [t[0][:2].lower() for t in names]
print(short_names)

departments = ['Dept A', 'Dept B', 'Dept C', 'Dept D']
count_in_department = {d: len(list(filter(lambda t: t[1]==d, names))) for d in departments}

print(count_in_department)
