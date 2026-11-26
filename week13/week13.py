import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv('EV_charge.csv')

print(df.loc[:,['platform','weekday','kwhTotal']])
print(df.loc[df['platform'] == 'web',['platform','weekday','kwhTotal']])

fig = px.box(
    data_frame=df, x='weekday', y='kwhTotal', width=500, height=400,
    category_orders={'weekday': ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']}, color='platform')
fig.show()

fig, ax = plt.subplots()
sns.boxplot(x='weekday', y='kwhTotal', data=df, ax=ax, order=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'], hue='platform')
plt.show()
print(df[df['platform'] == 'web'])



