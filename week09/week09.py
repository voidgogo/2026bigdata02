import pandas as pd

df = pd.read_csv('us_confirmed.csv')
# print(df.info())
df['Date'] = pd.to_datetime(df['Date'])  # str -> datetime
# print(df.info())
# print(df.head())
df = df.set_index('Date').sort_values('Date')  # update
# print(df.head())
# print(df['2020-01':'2020-02'])
# print(df['2021-05':'2021-06'])

df = df.reset_index().set_index('Province/State').sort_index()  # update
# print(df.head())
# print(df.tail())
print(df.index.unique())
states = list(df.index.unique())
print(len(states))  # 미국 주, 연방구역, 자치령, 특수 목적의 배 포함

print(df['Ca':'Cp'])  # California to Connecticut