import pandas as pd

df = pd.read_csv('us_confirmed.csv')
df['Date'] = pd.to_datetime(df['Date'])  # str -> datetime
df = df.set_index('Date').sort_values('Date')
print(df.head())

# print(df['Province/State'].unique())
states = df['Province/State'].unique()[3:6]  # ['Iowa', 'Wisconsin', 'California']
# print(states)
df = df[df['Province/State'].isin(states)]
print(df)