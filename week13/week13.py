import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

df = pd.read_csv('medical_cost.csv')
# print(df.head(3))
# print(df.tail(3))
# print(df.info())

age_bin_list = np.arange(10, 80, 10)
df['age_bin'] = pd.cut(df['age'], bins=age_bin_list, right=False)
# print(df['age_bin'].value_counts())
pivot_df = df.pivot_table(index='age_bin', columns='region', values='charges', aggfunc='median')
# print(pivot_df)

fig, ax = plt.subplots()
sns.heatmap(pivot_df, ax=ax, annot=True)
plt.show()


