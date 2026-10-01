import numpy as np
import pandas as pd

df1 = pd.read_csv("./bookings.csv")
# print(df1.info())
# print(df1.describe())  # 수치형 데이터에 대한 요약 통계량
# print(df1.describe(include='str'))  # 문자열 데이터에 대한 요약 통계량(가능한 것만)
# print(df1.describe(exclude='str'))  # 문자열 데이터를 배제한 대한 요약 통계량
print(df1['Review'].value_counts())
df1.loc[df1['Review'] == 'Superb 9.0', 'Review'] = "Superb"
df1.loc[df1['Review'] == 'Superb ', 'Review'] = "Superb"
df1.loc[df1['Review'] == 'Exceptional 10', 'Review'] = "Exceptional"
df1.loc[df1['Review'] == 'Exceptional ', 'Review'] = "Exceptional"
print(df1['Review'].value_counts())