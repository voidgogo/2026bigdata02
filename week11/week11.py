import pandas as pd

df = pd.read_csv('product.csv')
df['path'] = df.groupby('product_id')['operator'].transform(lambda x: '_'.join(x))
df['path'] = df['factory'] + '_' + df['path']
df = df.drop_duplicates('product_id')
df.drop(columns=['factory','process','operator'], inplace=True)
print(df.head())  # week10

df['factory'] = df['path'].map(lambda x: x[0:2])
df['path'] = df['path'].map(lambda x: x[3:])
print(df.head())

df['path'] = df['path'].map(lambda x: x.split('_'))
print(df.head())