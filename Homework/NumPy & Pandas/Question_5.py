# ==== Question 5: ====

import pandas as pd
from global_vars import *

print(f"d = {d}, m = {m}",end="\n\n")

# a - from list
series1 = pd.Series([d,m,d+m,m-d])
print("Series 1")
print(series1)

# b - five elements
series2 = pd.Series(100*d,range(5))
print("Series 2")
print(series2)

# c - random #s
series3 = pd.Series(np.random.randint(0,100,size=d*10))
print("Series 3")
print(series3)
stats = series3.describe()
print(stats)

# d - temperature
temperature = pd.Series([98.6,98.9,100.2,97.9], index=['Julie','Charlie','Sam','Andrea'])
print(temperature)

# e - dictionary
temp_dict = {'Julie':98.6, 'Charlie':98.9, 'Sam':100.2, 'Andrea':97.9}
series4 = pd.Series(temp_dict)
print(series4)