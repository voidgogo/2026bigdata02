import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df1 = pd.read_csv('weight_height.csv')
criteria = df1['Weight'].quantile(0.9999)  # remove outlier
print(df1.describe())
sns.scatterplot(x='Weight', y='Height', data=df1)
plt.show()
print(criteria)
df2 = df1[df1['Weight'] < criteria]
sns.scatterplot(x='Weight', y='Height', data=df2)
plt.show()