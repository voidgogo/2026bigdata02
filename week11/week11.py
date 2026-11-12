import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df1 = pd.read_csv('global_internet_users.csv')
entities = ['South Korea', 'United Kingdom', 'Finland']
# entities = ['Finland']
df1 = df1.loc[df1['Entity'].isin(entities)]
fig, ax = plt.subplots()
# sns.scatterplot(x='Year', y='No. of Internet Users', data=df1, ax=ax, hue='Entity', hue_order=['South Korea', 'United Kingdom', 'Finland'], palette='dark')
# sns.scatterplot(x='Year', y='No. of Internet Users', data=df1, ax=ax, style='Entity', markers=['o','^','X'], s=50, hue='Entity', palette='pastel')
sns.scatterplot(x='Year', y='No. of Internet Users', data=df1, ax=ax, size='Entity', sizes=(50, 200), hue='Entity', palette='pastel', hue_order=['South Korea', 'United Kingdom', 'Finland'])
plt.show()