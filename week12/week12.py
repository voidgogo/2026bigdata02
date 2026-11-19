import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

df1 = sns.load_dataset('tips')

# review week07
# s: slope, i: intercept, r: correlation
s, i, r, _, _ = linregress(df1['total_bill'], df1['tip'])  # x축은 전체지불금액, y축은 팁(미국)
print(s, i, r)  # 기울기, 절편, 상관계수(-1~1) 출력. 강한 양의 상관관계.

fig, ax = plt.subplots()
sns.regplot(x='total_bill', y='tip', data=df1, ax=ax)
plt.show()