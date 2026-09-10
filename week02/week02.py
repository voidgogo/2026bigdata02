import numpy as np
import pandas as pd

df1 = pd.read_csv("./bike.csv")
#print(df1.loc[df1['season'] == 3, ['season', 'humidity', 'windspeed', 'casual' ,'registered']])
#print(df1.loc[df1['season'] == 3, 'humidity':'registered'])
#print(df1['weather'].value_counts())
#print(df1.loc[(df1['season'] != 4)&(df1['weather'] != 1)])
#temp = df1.loc[(df1['season'] != 4)&(df1['weather'] != 1)]
#print(temp['weather']==1)
print(df1.loc[3, 'humidity'])
