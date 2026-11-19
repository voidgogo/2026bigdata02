import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('global_internet_users.csv')
entities = ['South Korea', 'United Kingdom', 'Finland']
df = df.loc[df['Entity'].isin(entities)]

fig, ax = plt.subplots()
sns.lineplot(
    x='Year', y='No. of Internet Users',
    data=df, ax=ax, hue='Entity'
)
sns.scatterplot(
    x='Year', y='No. of Internet Users',
    data=df, ax=ax, hue='Entity', legend=False
)
plt.show()