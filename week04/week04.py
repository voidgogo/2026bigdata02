import pandas as pd

s = pd.Series([0, 0, 1, 1, 0, 1, 1, 1, 1, 0])
# print(s)
sc = s.cumsum()  # 누적(cumulate) 합계(sum)
# print(sc)
# print(s.mul(sc))  # 곱셈(multiply)
# print(s.mul(sc).diff())  # 차(difference) : 뒤 원소값에서 앞 원소값을 빼기
# print(s.mul(sc).diff().where(lambda n:n<0))  # 조건 음수 추출. 음수가 아닌 수는 NaN 처리
# print(s.mul(sc).diff().where(lambda n:n<0).ffill())  # 결측값을 앞쪽의 값으로 채움
# print(s.mul(sc).diff().where(lambda n:n<0).bfill())  # 결측값을 뒷쪽의 값으로 채움
# print(s.mul(sc).diff().where(lambda n:n<0).ffill().add(sc, fill_value=0))  # 덧셈, 단 결측값은 0으로 처리
print(s.mul(sc).diff().where(lambda n:n<0).ffill().add(sc, fill_value=0).max())  # 4
