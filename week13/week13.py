import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv('EV_charge.csv')

#fig = px.box(data_frame=df, x='weekday', y='kwhTotal', width=500, height=400)
# fig = px.box(data_frame=df, x='weekday', y='kwhTotal', width=500, height=400, points='all')

fig = px.box(
    data_frame=df, x='weekday', y='kwhTotal', width=500, height=400,
    category_orders={'weekday': ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']}, color='platform')
fig.show()

# print(df.info())
# print(df.describe())
# print(df.head())
# print(df.tail())]

# print(df.iloc[:, 16:23])  # one-hot encoding, mon~sun

# fig, ax = plt.subplots()
# sns.boxplot(x='weekday', y='kwhTotal', data=df, ax=ax)
# plt.show()

# fig, ax = plt.subplots()
# sns.boxplot(x='weekday', y='kwhTotal', data=df, ax=ax, order=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
# # sns.stripplot(x='weekday', y='kwhTotal', data=df, ax=ax, color='red', alpha=0.2)  # alpha 값(투명도)
# sns.swarmplot(x='weekday', y='kwhTotal', data=df, ax=ax, color='red', alpha=0.2)  # 느림
# plt.show()

fig, ax = plt.subplots()
sns.boxplot(x='weekday', y='kwhTotal', data=df, ax=ax, order=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'], hue='platform')
plt.show()

# print(df['platform'])
# print(df['platform'].value_counts())