import numpy as np
import pandas as pd

df1 = pd.read_csv("./bike.csv")
#print(df1.info())
#print(df1.select_dtypes(include="float"))
#print(df1.select_dtypes(exclude="float"))
#print(df1.filter(regex="d..y"))
#print(df1.filter(items=['windspeed', 'season']))
df2 = df1.set_index('datetime')
#print(df2)
print(df2.filter(like='00:00:00', axis=0))