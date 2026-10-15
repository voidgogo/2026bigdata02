import pandas as pd

df1 = pd.read_csv("Uber.csv")
# print(df1.head())
# print(df1.tail())

# print(df1.info())
# ValueError: time data "Totals" doesn't match format "%m/%d/%Y %H:%M".
df1['START_DATE*'] = pd.to_datetime(df1['START_DATE*'], errors="coerce")  # str -> datetime
df1['END_DATE*'] = pd.to_datetime(df1['END_DATE*'], errors="coerce")  # str -> datetime
# print(df1['START_DATE*'], df1['END_DATE*'])
# print(df1.info())

# print(df1['START_DATE*'].unique())  # errors="coerce" 옵션 값에 따른 잘못된값 결측치 처리 확인
# print(df1['END_DATE*'].unique())

# print(df1['CATEGORY*'].value_counts())  # 업무용, 개인용
# print(df1['START*'].value_counts())  # 출발지역
# print(df1['STOP*'].value_counts())  # 도착지역

# print(df1['MILES*'].describe())  # float 데이터의 요약통계량. 최대값 오류
# print(df1['MILES*'].sum()-12204.7)  # 전체 운행거리의 합산 값이 마지막행 MILES*열에 포함되어있는 오류 확인
# print(df1[df1['MILES*'] ==  df1['MILES*'].max()])  # 오류가 들어있는 행 출력
df1 = df1.drop(1155)  # 오류행 제거
# print(df1[df1['MILES*'] ==  df1['MILES*'].max()])  # 최대 운행거리했던 행 출력

# print(df1['PURPOSE*'].value_counts())

# 결측치 개수 확인
# print(df1.isnull().sum())  # print(df1.isna().sum())

# print(df1.info())
# df1['DURATION*'] = df1['END_DATE*'] - df1['START_DATE*']  # 운행시간 칼럼 생성
df1['DURATION*'] = (df1['END_DATE*'] - df1['START_DATE*']).dt.total_seconds() / 60  # 분 단위로 기록
# print(df1['DURATION*'])
# print(df1.info())

# print(df1.groupby(['CATEGORY*', 'PURPOSE*'])[['MILES*', 'DURATION*']].count())
print(df1.groupby(['CATEGORY*', 'PURPOSE*'])[['MILES*', 'DURATION*']].agg(['median', 'mean', 'count']))