# ==== Question 3: ====

from global_vars import *

print(f"Bday = {Bday}")
if Bday % 2 == 0:
	print("Bday is even")
else:
	print("Bday is odd")

# initialize 5x5 array of random integers
randFiveByFive = np.random.randint(low=0,high=99,size=(5,5))
print("Random 5x5 Array (0-99):")
print(randFiveByFive)


'''
Using bincount by row (this gets messy, makes more sense to flatten our array first)

# using bincount (for each row)
for row in enumerate(randFiveByFive):
	# row[0] stores row numbers (for presentation)
	# row[1] stores each row of the 5x5
	bincount = np.bincount(row[1])
	print(f"occurences of indexes in row {row[0]+1}: {bincount}")

'''

# flatten the array & bincount it
flatRand = randFiveByFive.flatten()
bincount = np.bincount(flatRand)
print(f"Occurrences of indexes for 5x5: {bincount}")