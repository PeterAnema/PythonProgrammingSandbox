import csv

with open('ca-500.csv') as f1:
    reader = csv.DictReader(f1, delimiter = ',', quotechar = '"')
    fieldnames = reader.fieldnames
    print(fieldnames)
    with open('ca-500-out.csv', 'w') as f2:
        writer = csv.DictWriter(f2, delimiter = ';', quotechar = '"', fieldnames = fieldnames)
        writer.writeheader()
        for linenr, d in enumerate(reader):
            writer.writerow(d)
