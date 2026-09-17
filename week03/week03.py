import numpy as np
import pandas as pd

df2 = pd.read_csv("./bookings.csv")
# print(df2.info())
# print(df2['Review'])
print(df2['Review'].value_counts())
df2.loc[df2['Review'] == "Superb 9.0", "Review"] = "Superb"
df2.loc[df2['Review'] == "Exceptional 10", "Review"] = "Exceptional"
df2.loc[df2['Review'] == "Superb ", "Review"] = "Superb"  # 띄어쓰기 제거
df2.loc[df2['Review'] == "Exceptional ", "Review"] = "Exceptional"  # 띄어쓰기 제거
df2.loc[df2['Review'] == "Good ", "Review"] = "Good"  # 띄어쓰기 제거
df2.loc[df2['Review'] == "Very good ", "Review"] = "Very good"  # 띄어쓰기 제거
df2.loc[df2['Review'] == "Fabulous ", "Review"] = "Fabulous"  # 띄어쓰기 제거
df2.loc[df2['Review'] == "Review score ", "Review"] = "Review score"  # 띄어쓰기 제거

print(df2['Review'].value_counts())

# print(df2[df2['Review'] == 'Review score'])  # 띄어쓰기 주의
print(df2.loc[df2['Review'] == 'Review score', ['Review','Rating']])
# print(df2.loc[df2['Review'] == 'Very good', ['Review','Rating']])
# print(df2.loc[df2['Review'] == 'Good', ['Review','Rating']])
df2.loc[df2['Review'] == 'Review score', 'Review'] = "Good"
print(df2['Review'].value_counts())
print(df2['Total_Review'].unique())
print(df2['Total_Review'].value_counts())
df2['Total_Review'] = df2['Total_Review'].map(lambda x: str(x).replace('external','').strip())
df2['Total_Review'] = df2['Total_Review'].map(lambda x: str(x).replace('review','').strip())
df2['Total_Review'] = df2['Total_Review'].map(lambda x: str(x).replace(',',''))
df2['Total_Review'] = df2['Total_Review'].astype('float')
print(df2['Total_Review'].value_counts())
print(df2['Total_Review'].unique())
print(df2['Total_Review'].describe())