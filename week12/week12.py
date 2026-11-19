import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

df1 = pd.read_csv('global_internet_users.csv')

entities = ['South Korea', 'United Kingdom', 'Finland', 'North Korea', 'China', 'India', 'Japan', 'Italy', 'Spain']  # 9개 국가
df1 = df1.loc[df1['Entity'].isin(entities)]

c = px.colors.qualitative.Set2  # 8가지 색상 지원
# c = px.colors.qualitative.Safe
fig = px.scatter(
    data_frame=df1, x='Year', y='No. of Internet Users',
    width=500, height=400, color='Entity', color_discrete_sequence=c

)
fig.show()
