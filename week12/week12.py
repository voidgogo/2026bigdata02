import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import plotly.express as px
import statsmodels.api as sm

df1 = sns.load_dataset('tips')

# # s: slope, i: intercept, r: correlation
# s, i, r, _, _ = linregress(df1['total_bill'], df1['tip'])
# print(s, i, r)
#
# fig, ax = plt.subplots()
# sns.regplot(x='total_bill', y='tip', data=df1, ax=ax, ci=None, line_kws={'label': f'y={s:.2f}x+{i:.2f}, R^2={r**2:.2f}'})
# plt.legend()
# plt.show()

fig = px.scatter(data_frame=df1, x='total_bill', y='tip', width=500, height=400, trendline='ols', color='smoker')  # ols: 최소제곱 선형회귀
fig.show()
