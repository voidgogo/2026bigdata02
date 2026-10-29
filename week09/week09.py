import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df1 = pd.read_csv('weight_height.csv')
print(df1['Weight'].sort_values())
print(df1[df1['Weight'] > 390].index)  # outlier
print(df1.iloc[2014:2015])
print(df1.iloc[2014])
df1['Weight'] = df1['Weight'].clip(70, 300)  # update df1
print(df1.iloc[2014])  # 390.200000 -> 300
print(df1.iloc[9285])  # 64.700127 -> 70
print(df1.iloc[5360])  # 68.982530 -> 70
sns.scatterplot(x='Weight', y='Height', data=df1)
plt.show()