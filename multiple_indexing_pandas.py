import pandas as pd

filename = 'multiple_indexing_data.csv'

df = pd.read_csv(filename)

print(df)

df_selection = df[(df['l1']=='w2') & (df['l2']=='f1')]

print(df_selection)

indexes = df_selection.index
values = df_selection['l3'].values

print(list(indexes))
print(list(values))
