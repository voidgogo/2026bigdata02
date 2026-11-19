import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

df1 = pd.read_csv('global_internet_users.csv')

entities = ['South Korea', 'United Kingdom', 'Finland', 'United States']
df1 = df1.loc[df1['Entity'].isin(entities)]

fig = px.scatter(
    data_frame=df1, x='Year', y='No. of Internet Users', symbol='Entity', symbol_sequence=['cross','star','circle', 'square'],
    width=500, height=400, color='Entity', color_discrete_sequence=px.colors.qualitative.Set2, size='No. of Internet Users'
)
fig.show()

df2 = sns.load_dataset('tips')
fig = px.scatter(
    data_frame=df2, x='total_bill', y='tip', color='smoker', size='size', symbol='time',
    width=600, height=400, color_discrete_sequence=px.colors.qualitative.Vivid
)
fig.show()