import seaborn as sns
import pandas as pd
import numpy as np

df1 = sns.load_dataset("titanic")
# print(df1.head())
# print(df1.groupby('sex')['survived'].median())
# print(df1.groupby(['sex','class'])['survived'].mean())
# print(df1.groupby(['sex','class'])['survived'].agg(['count','mean','median']))
# print(df1.groupby(['sex','class'])[['survived','age']].agg({'survived':'median','age':'min'}))

def get_IQR(data):
    _3rd = data.quantile(.75)
    _1st = data.quantile(.25)
    return (np.abs(_3rd - _1st) * 1.5)

# print(df1.groupby(['sex','class'])['age'].apply(get_IQR))

df2 = sns.load_dataset('penguins')
# print(df2.isna().sum())  # 각 칼럼 별 결측치 합계
# print(df2.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].mean())

# 결측치 행 추출
print(df2.query('sex.isna()'))
print(df2[df2['sex'].isna()])
print(df2.loc[df2['sex'].isna()])

print(df2.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].apply(lambda x: x.fillna(x.mean()))
)