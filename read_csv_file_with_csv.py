import csv
import re

f_in = open("ca-500.csv", "r")
f_out = open("ca-500-out.tsv", "wb")

reader = csv.reader(f_in, delimiter=';', quotechar='')
writer = csv.writer(f_out, delimiter='\t', quotechar='', quoting=csv.QUOTE_NONE)

for cols in reader:
    if re.search(r'\w*@(yahoo\.com|hotmail\.com)', cols[9]):

        print('%-10s%-20s%-30s%-40s%-30s' % tuple([cols[index] for index in (0,1,3,4,9)]))
 
        writer.writerow([cols[index] for index in (0,1,3,4,9)])

f_out.close()
f_in.close()
