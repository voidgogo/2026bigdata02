import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import numpy as np

x = np.arange(-2, 10, 1)
y = x**3 - 9*x**2 + x + 4
#y = 9*x**2 + x + 4

fig, ax = plt.subplots()
#sns.regplot(x=x, y=y, ax=ax, order=3)
sns.regplot(
    x=x, y=y, ax=ax, order=3,
    scatter_kws={'s':50}, line_kws={'color':'blue', 'linestyle':'-.'}
)
plt.show()