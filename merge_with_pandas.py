import sys
import pandas as pd

#filenames = ['merge1.csv','merge2.csv','merge3.csv']
#filename_merged = 'merged.csv'
sep = ';'
missing = '_'

# Get command line arguments
if len(sys.argv) > 1:
    filename_merged = sys.argv[1]
else:
    filename_merged = 'merged.csv'

if len(sys.argv) > 2:
    filenames = sys.argv[2:]
else:
    filenames = ['merge1.csv','merge2.csv','merge3.csv']

# Read and merge dataframes
if filenames:

    df = (pd.read_csv(filename, sep=sep, names=[filename], dtype=str) for filename in filenames)

    result = pd.concat(df, axis=1, sort=True).fillna(missing)

    result.to_csv(sys.stdout, sep=sep, header=None)

