import pandas as pd

df1 = pd.read_csv('German_credit.csv')
# print(df1.head())
# print(df1.tail())

# print(df1.info())
# print(pd.cut(df1['Age'], bins=8))
# print(df1.describe())
print(pd.cut(df1['Age'], bins=8).reset_index().groupby('Age').count())
ages = [10, 20, 30, 40, 50, 60, 70, 80]
# print(pd.cut(df1['Age'], bins=ages))  # 초과 ~ 이하, right=True
# print(pd.cut(df1['Age'], bins=ages, right=False))  # 이상 ~ 미만
# print(pd.cut(df1['Age'], bins=ages, right=False).reset_index().groupby('Age').count())

# qcut 함수는 비율대로 구간을 나눔. 단, 중복값 이슈가 존재함
# print(pd.qcut(df1['Age'], q=8).reset_index().groupby('Age').count())
print(pd.qcut(df1['Age'], q=3).reset_index().groupby('Age').count())