import numpy as np
import pandas as pd

df2 = pd.read_csv("./bookings.csv")
print(df2.info())
# print(df2['Rating'].isna())
# print(df2[df2['Rating'].isna()].head(5))
index = df2[df2['Rating'].isna()].head(5).index
print(index)
print(df2['Rating'].describe())
df2['Rating'] = df2['Rating'].fillna(df2['Rating'].median())  # mean도 가능
print(df2.info())
print(df2['Rating'].head(5))
print(df2.iloc[167:172, 1:4])
print(df2.loc[index, 'Review':'Rating'])