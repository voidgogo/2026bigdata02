import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = sns.load_dataset('tips')

fig, ax = plt.subplots()
#sns.histplot(df, x='total_bill', ax=ax)
#sns.histplot(df, x='total_bill', ax=ax, bins=8, binwidth=6)  # 계급구간 8
#sns.histplot(df, x='total_bill', ax=ax, hue='time')
sns.histplot(df, x='total_bill', ax=ax, hue='time', multiple='stack')
plt.show()



