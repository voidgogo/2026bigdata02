import pandas as pd

df = pd.read_csv('product_inspection.csv')
df['date'] = pd.to_datetime(df['date'])  # str -> datetime
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df['inspection_step'].value_counts())
# print(df[df['date'] == '2022-01-02'])
# print(df.groupby('inspection_step')['value'].mean())
# print(df.groupby('inspection_step')['value'].describe())

# feature extraction
df['normalized1'] = df.groupby('inspection_step')['value'].transform(lambda x: (x - x.mean())/x.std())
# print(df['normalized1'])

temp = df.sort_values(['inspection_step','date']).drop_duplicates('inspection_step')
# print(temp)
temp = temp.set_index('inspection_step')['value']
# print(temp)

df = df.set_index('inspection_step')
print(df)

# feature extraction
df['normalized2'] = df['value'] - temp
df = df.reset_index()
print(df)