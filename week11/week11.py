import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df1 = pd.read_csv('global_internet_users.csv')
# print(df1.head(3))
# print(df1.tail(3))
# print(df1.info())
# print(df1.describe())
# print(df1[['Entity', 'Year', 'Cellular Subscription']])
df1_SouthKorea = df1['Entity']=="South Korea"
# print(df1[['Entity', 'Year', 'Cellular Subscription'] & )
# print(df1[df1_SouthKorea])
print(df1.loc[7414:7452,['Entity', 'Year', 'Cellular Subscription']])