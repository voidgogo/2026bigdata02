import pandas as pd

df = pd.read_csv('product_inspection.csv')
df['date'] = pd.to_datetime(df['date'])  # str -> datetime
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df['inspection_step'].value_counts())
print(df[df['date'] == '2022-01-02'])