import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df1 = sns.load_dataset('tips')
# print(df1.head())
# print(df1.tail())
# print(df1.describe())
# print(df1.info())

fig, ax = plt.subplots()
sns.scatterplot(x='total_bill', y='tip', data=df1, ax=ax, hue='smoker', style='time', size='size')
plt.show()