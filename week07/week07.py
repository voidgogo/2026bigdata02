import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress  # 선형회귀

df1 = pd.read_csv("Uber.csv")
df1['START_DATE*'] = pd.to_datetime(df1['START_DATE*'], errors="coerce")  # str -> datetime
df1['END_DATE*'] = pd.to_datetime(df1['END_DATE*'], errors="coerce")  # str -> datetime
df1 = df1.drop(1155)  # 오류행 제거
df1['DURATION*'] = (df1['END_DATE*'] - df1['START_DATE*']).dt.total_seconds() / 60  # 분 단위로 기록

df1 = df1.dropna()  # 결측행 제거

# s: slope, i: intercept, r: correlation
s, i, r, _, _ = linregress(df1['MILES*'], df1['DURATION*'])  # x축은 운행거리, y축은 운행시간
# print(s, i, r)  # 기울기, 절편, 상관계수(-1~1) 출력. 강한 양의 상관관계.

# print(df1['MILES*'].describe())
# print(df1['DURATION*'].describe())

fig, ax = plt.subplots()
sns.regplot(x=df1['MILES*'], y=df1['DURATION*'], data=df1, ax=ax, line_kws={'label': f'y={s:.2f}x+{i:.2f}, R^2={r**2:.2f}'})
plt.legend()
plt.show()
