import csv
filename = 'ca-500.csv'

try:
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for linenr, row in enumerate(reader):
            if linenr >= 5:
                break
            print(row['first_name'], row['last_name'])

except FileNotFoundError:
    print(f'Cannot find file {filename}')

except Exception as err:
    print(f'Something else went wrong', err)
