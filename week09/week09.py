import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df1 = pd.read_csv('weight_height.csv')
# print(df1.info())
print(df1.describe())
# print(df1.head())
# print(df1.tail())
# print(df1['Gender'].vaue_counts())
df2 = df1.query('Weight < 300')  # remove outlier
print(df1.describe())
print(df2.describe())
sns.scatterplot(x='Weight', y='Height', data=df1)
plt.show()
sns.scatterplot(x='Weight', y='Height', data=df2)
plt.show()

