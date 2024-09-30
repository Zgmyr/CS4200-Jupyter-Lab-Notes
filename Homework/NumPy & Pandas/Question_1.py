# ==== Question 1: ====

import numpy as np

'''
Broadcasting: "arrays can be broadcast against each other if their dimensions match or if one of the arrays has a size of 1...
	if one of the arrays has a size of 1 in an axis, then that value will be broadcast along that axis, or duplicated as many
	times as necessary to match the number of elements along that axis in the other array."

source: https://realpython.com/numpy-tutorial/#broadcasting
'''

# Array 1 is a 3D array with 2 planes, 1 row and 4 columns
array1 = np.arange(8).reshape(2,1,4)
print("Array 1:")
print(array1,end="\n\n")

# Array 2 is a 3D array with 1 plane, 2 rows and 4 columns
array2 = np.arange(8).reshape(1,2,4)
print("Array 2:")
print(array2,end="\n\n")

# Adding Array 1 to Array 2
array3 = array1 + array2
print("Array 1 + Array 2:")
print(array3)

'''
Explanation:
	1. Array 2 has only one plane where Array 1 has 2.
	=> Array 2's one plane is broadcast across the two planes of Array 1

	2. Array 1 has only one row where Array 2 has 2 per plane
	=> Array 1's singular row (in each plane) is broadcast across both rows of Array 2 (for each plane)
'''