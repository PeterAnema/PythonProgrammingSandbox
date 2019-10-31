import pandas as pd

df = pd.read_csv("ca-500.csv", sep=';')

df.set_index('email', inplace=True, drop=False)

print(df)

print(df.columns.values)

# df['full_name'] = df['first_name'] + ' ' + df['last_name']
#
# print(df[['full_name','city'],df['city']=='Montreal'])



# print( df.loc[df['city'].isin({'Montreal','Vancouver'}),
#               ['full_name','city','email']] )


