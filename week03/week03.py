import numpy as np
import pandas as pd

df1 = pd.read_csv("./bike.csv")

# df1 = df1.rename({'registered':'registered_user','casual':'casual_user'}, axis=1)
df1.rename({'registered':'registered_user','casual':'casual_user'}, axis=1, inplace=True)
# print(df1.head())
# print(df1.info())
# print(df1.describe(include='str'))
# print(df1.describe(include='float'))
print(df1.describe(exclude='int'))