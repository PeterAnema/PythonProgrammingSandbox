import re

def readline_generator(filename, pattern):
    compiled_pattern = re.compile(pattern, re.IGNORECASE)
    with open(filename, 'r') as f:
        for line_nr, line in enumerate(f):
            if compiled_pattern.search(line):
                yield line_nr, line.strip()

# ------------------------------------------------------------

filename = 'ca-500.csv'
pattern = 'montreal|toronto'

for line_nr, line in readline_generator(filename, pattern):
    print('{:4d}: {}'.format(line_nr, line))
