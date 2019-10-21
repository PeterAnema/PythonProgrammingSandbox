filename = r'./ca-500.csv'

out = r'ca-500-filtered.tsv'

with open(out, 'w') as f_out:
    with open(filename) as f:
        headers = f.readline().rstrip('\n').split('";"')
        for linenr, line in enumerate(f, 1):
            line = line.rstrip('\n')
            columns = line.strip('"').split('";"')
            d = dict(zip(headers,columns))
            if d['city'] in ('Montreal','Toronto'):
                print('%3d: %s' % (linenr, columns))
                line_out = '\t'.join(columns)
                f_out.write(line_out + '\n')
