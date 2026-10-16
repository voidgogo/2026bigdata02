import pandas as pd

df2 = pd.read_csv("APPL_price.csv")
s = df2['Close'] > 175
# print(s.sum())  # 1980년 ~ 2022년 자료 중 종가가 175달러 초과한 날의 합계. 22일
sc = s.cumsum()
# print(sc)

# print(s.mul(sc).diff().where(lambda n:n<0).ffill().add(sc, fill_value=0).max())  # 4

# 애플 주가가 종가 기준 175달러를 초과한 연속적인 날짜 중 기간이 가장 길었던 날은 9
# print(s.mul(sc).diff().where(lambda n:n<0).ffill().add(sc, fill_value=0).max())

print(df2[s])