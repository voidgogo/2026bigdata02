import numpy as np
import pandas as pd

df1 = pd.read_csv("./bookings.csv")
# print(df1.info())
# print(df1.describe())  # 수치형 데이터에 대한 요약 통계량
# print(df1.describe(include='str'))  # 문자열 데이터에 대한 요약 통계량(가능한 것만)
# print(df1.describe(exclude='str'))  # 문자열 데이터를 배제한 대한 요약 통계량
# print(df1['Review'].value_counts())  # before
df1.loc[df1['Review'] == 'Superb 9.0', 'Review'] = "Superb"
df1.loc[df1['Review'] == 'Superb ', 'Review'] = "Superb"
df1.loc[df1['Review'] == 'Exceptional 10', 'Review'] = "Exceptional"
df1.loc[df1['Review'] == 'Exceptional ', 'Review'] = "Exceptional"
# print(df1['Review'].value_counts())  # after

# print(df1['Total_Review'].unique())  # before
df1['Total_Review'] = df1['Total_Review'].map(lambda x: str(x).replace('external','').strip())
df1['Total_Review'] = df1['Total_Review'].map(lambda x: str(x).replace('review','').strip())
df1['Total_Review'] = df1['Total_Review'].map(lambda x: str(x).replace(',',''))
# print(df1['Total_Review'].unique())  # after
df1['Total_Review'] = df1['Total_Review'].astype('float')  # 문자열 원소들을 실수형으로 변환
# print(df1['Total_Review'].unique())
# print(df1.describe())  # Total_Review도 요약통계량

quantile = [0, 0.2, 0.4, 0.6, 0.8, 1]
for idx in quantile:
    # q = df1['Total_Review'].quantile(idx, interpolation='lower')
    q = df1['Total_Review'].quantile(idx, interpolation='higher')
    print(f'quantile({idx}) is {q}')