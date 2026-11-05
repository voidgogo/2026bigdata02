import pandas as pd

df = pd.read_csv('product.csv')
print(df.head(7))
# print(df.tail())
# print(df.info())
# print(df.describe())
df['path'] = df.groupby('product_id')['operator'].transform(lambda x: '_'.join(x))
print(df.head(7))
