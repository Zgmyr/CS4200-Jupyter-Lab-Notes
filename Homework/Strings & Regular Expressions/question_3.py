# Question 3:

from global_vars import *
from itertools import permutations
from itertools import combinations
import re

'''
PSEUDOCODE:
1. Sentinel-controlled repitition until user enters 6 letter word (using regular expressions r'[a-zA-Z]{6}')
2. create a permutated list of 5-letter strings from user input string (use itertools permutations)
3. return all strings
'''

# get a 6-letter word from the user
print(f'd = {d}... we will use a six letter word (d*2)')

while True:
	inputWord = input("Enter a 6-letter word")
	isSixLetters = re.search(r'\b[a-zA-Z]{6}\b',inputWord)
	if isSixLetters:
		break
	else:
		print("... not a six letter word, try again")

# get list of permutations for all 4 (d-1) letter strings from inputWord 
perms = [''.join(p) for p in permutations(inputWord,d+1)]

# print list of permutations
print(perms)