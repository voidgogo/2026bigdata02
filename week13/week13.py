import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('EV_charge.csv')
# print(df.info())
# print(df.describe())
# print(df.head())
# print(df.tail())]

# print(df.iloc[:, 16:23])  # one-hot encoding, mon~sun

# fig, ax = plt.subplots()
# sns.boxplot(x='weekday', y='kwhTotal', data=df, ax=ax)
# plt.show()

fig, ax = plt.subplots()
sns.boxplot(x='weekday', y='kwhTotal', data=df, ax=ax, order=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
plt.show()