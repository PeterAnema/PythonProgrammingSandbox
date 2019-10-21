import csv

f_in = open("ca-500.csv", "r")
f_out = open("ca-500-out.tsv", "w")

colnames = ('first_name', 'last_name', 'city', 'email')

reader = csv.DictReader(f_in, delimiter=';', quotechar='"')
writer = csv.DictWriter(f_out, colnames, delimiter='\t', quotechar='', quoting=csv.QUOTE_NONE)

writer.writeheader()

for cols in reader:
   if cols['city'] in 'Montreal':

       print('{:10}{:20}{:30}{:30}'.format(*[cols[fieldname] for fieldname in colnames]))

       writer.writerow({fieldname:cols[fieldname] for fieldname in colnames})

f_out.close()
f_in.close()
