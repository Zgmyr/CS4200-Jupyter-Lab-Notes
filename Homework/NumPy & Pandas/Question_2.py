# ==== Question 2: ====

from global_vars import *
# m = 3, d = 3 from global_vars

# 2D array of shape 2,2
array_1 = np.array([[0,d],
					[m,3]])
print("Array 1:")
print(array_1)
print(f"Shape: {array_1.shape}",end="\n\n")

# 2D array of shape 2,2
array_2 = np.array([[4,2*d],
					[2*m,7]])
print("Array2:")
print(array_2)
print(f"Shape: {array_2.shape}",end="\n\n")

# a - vertical stacking
array_3 = np.vstack((array_1,array_2))
print("Array3:")
print(array_3)
print(f"Shape: {array_3.shape}",end="\n\n")

# b - horizontal stacking
array_4 = np.hstack((array_1,array_2))
print("Array4:")
print(array_4)
print(f"Shape: {array_4.shape}",end="\n\n")

# c - vertical stacking (copy of array_4)
array_5 = np.vstack((array_4,array_4))
print("Array5:")
print(array_5)
print(f"Shape: {array_5.shape}",end="\n\n")

# d - horizontal stacking (copy of array_3)
array_6 = np.hstack((array_3,array_3))
print("Array6:")
print(array_6)
print(f"Shape: {array_6.shape}",end="\n\n")