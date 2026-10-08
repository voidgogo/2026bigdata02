import seaborn as sns
import pandas as pd
import numpy as np

df = pd.DataFrame(
    [
        ['A', 1],
        ['A', 1],
        ['A', 1],
        ['B', 10],
        ['B', 10]
    ], columns=['group', 'value']
)
print(df)
print(df.groupby([1,0,1,0,1])['value'].mean())
s = pd.Series([True, False, True, False, True])
print(df.groupby(s)['value'].mean())
