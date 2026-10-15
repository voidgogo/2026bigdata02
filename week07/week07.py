import pandas as pd

df1 = pd.read_csv("Uber.csv")
# print(df1.head())
# print(df1.tail())
# print(df1['MILES*'].sum()-12204.7)

# print(df1.info())
# ValueError: time data "Totals" doesn't match format "%m/%d/%Y %H:%M".
df1['START_DATE*'] = pd.to_datetime(df1['START_DATE*'], errors="coerce")  # str -> datetime
df1['END_DATE*'] = pd.to_datetime(df1['END_DATE*'], errors="coerce")  # str -> datetime
# print(df1['START_DATE*'], df1['END_DATE*'])
# print(df1.info())

# print(df1['START_DATE*'].unique())  # errors="coerce" 옵션 값에 따른 잘못된값 결측치 처리 확인
# print(df1['END_DATE*'].unique())

print(df1['CATEGORY*'].value_counts())