import pandas as pd

df = pd.read_csv('product.csv')
df['path'] = df.groupby('product_id')['operator'].transform(lambda x: '_'.join(x))
df['path'] = df['factory'] + '_' + df['path']
print(df.head())
df = df.drop_duplicates('product_id')
print(df.head())
df.drop(columns=['factory','process','operator'], inplace=True)
print(df.head())