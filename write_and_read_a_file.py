
filename = 'mijnbestand.txt'

with open(filename, 'w') as f:
    f.write('regel1,1,2\n')
    f.write('regel2,5,3\n')
    f.write('regel3,3,2\n')
    f.write('regel4,9,5\n')
    f.write('regel5,2,6\n')
    f.write('regel6,5,7\n')
    f.write('regel7,3,3\n')


with open(filename) as f:
    for line in (line.rstrip() for line in f):
        print(line)
