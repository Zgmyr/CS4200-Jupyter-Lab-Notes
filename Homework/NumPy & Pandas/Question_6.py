# ==== Question 6: ====

import numpy as np
import pandas as pd

# a - DataFrame from dictionary

def generate_random_temps():
	rand_temps = np.random.uniform(90,100,size=3)
	return np.round(rand_temps, 1) 

# create dictionary of temperatures for 3 people using random generated temps
temps = {'Maxine':generate_random_temps(), 'James':generate_random_temps(), 'Amanda':generate_random_temps()}

# convert to DataFrame
temps_DF = pd.DataFrame(temps)
print(temps_DF)

# b - with indexes
temps_index_DF = pd.DataFrame(temps, index=['Morning','Afternoon','Evening'])
print(temps_index_DF,end="\n\n")

# c - Maxine's temps
Maxine_temps = temps_index_DF['Maxine']
print("Maxine's Temps:")
print(Maxine_temps,end="\n\n")

# d - Morning temps
morning_temps = temps_index_DF.loc['Morning']
print("Morning Temps:")
print(morning_temps,end="\n\n")

# e - Morning & Evening
morning_evening_temps = temps_index_DF.loc[['Morning','Evening']]
print("Morning & Evening Temps:")
print(morning_evening_temps,end="\n\n")

# f - Amanda & Maxine
Amanda_Maxine_temps = temps_index_DF[['Amanda','Maxine']]
print("Amanda & Maxine's Temps:")
print(Amanda_Maxine_temps,end="\n\n")

# g - Amanda & Maxine in 'Morning' & 'Afternoon'
Amanda_Maxine_morning_afternoon = temps_index_DF[['Amanda','Maxine']].loc[['Morning','Afternoon']]
print("Amanda & Maxine's Morning/Afternoon Temps:")
print(Amanda_Maxine_morning_afternoon,end="\n\n")

# h - Stats
temp_stats = temps_index_DF.describe()
print(temp_stats)

# i - transpose
print(temps_index_DF.T)

# Sorted by name alpha.
print(temps_index_DF.sort_index(axis=1))