import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

df = pd.read_csv('global_internet_users.csv')
entities = ['South Korea', 'United Kingdom', 'Finland']
df = df.loc[df['Entity'].isin(entities)]

fig = px.line(
    data_frame=df, x='Year', y='No. of Internet Users',
    width=400, height=400, line_dash='Entity'
)
fig.show()
fig = px.line(
    data_frame=df, x='Year', y='No. of Internet Users',
    width=400, height=400,
    color='Entity', symbol='Entity'
)
fig.show()