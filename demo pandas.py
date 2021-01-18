import pandas as pd

filename = 'ca-500.csv'
df = pd.read_csv(filename, delimiter=';')
print(df[['first_name', 'last_name']])