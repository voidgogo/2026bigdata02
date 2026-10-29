import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, np.nan, np.nan, 6, 7, np.nan, np.nan])
print(s)
print(s.interpolate(method="spline", order=1, limit_direction="forward", limit=1))
# print(s.interpolate(method="spline", order=1, limit_direction="backward", limit=2))