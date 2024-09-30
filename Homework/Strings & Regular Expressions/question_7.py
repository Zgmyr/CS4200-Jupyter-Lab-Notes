# Question 7:
# GOAL: use regular expressions to check for a list of weapons from the given quote

import re

'''
PSEUDOCODE:
1. given a list of weapons and a quote
2. construct a regular expression that contains all possible weapons from the list using the '|' operator, treating this as one large capture group
3. use re.findall() to search the existence of this pattern in the quote
'''

# quote from Lord of the Rings
quote = (
	"Aragorn: If by my life or death I can protect you I will. You have my sword."
	" Legolas: And you have my bow. Gimli: And my ax."
)

# list of medieval weapons that we will check for inside the previous quote
listOfWeapons = ['sword',
				'staff',
				'mace',
				'ax',
				'trebuchet',
				'halberd',
				'bow']

# given 'A|B' for regular expressions A and B, "creates a regular expression that will match either A or B"
# source: https://docs.python.org/3/library/re.html#regular-expression-syntax

# construct a pattern using the listOfWeapons (e.g. r'sword|staff|mace' etc)
pattern = r'\b(' + '|'.join(listOfWeapons) + r')\b'

# find all instances of our pattern in the quote
weapons = re.findall(pattern, quote)

# print results
print("Weapons offered to Frodo: ", ', '.join(weapons))