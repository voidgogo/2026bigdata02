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

print(df1.groupby(['sex','class'])['age'].apply(get_IQR))