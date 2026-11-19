import pandas as pd

df = pd.read_csv('EV_charge.csv')
print(df.info())
print(df.describe())
print(df.head())
print(df.tail())