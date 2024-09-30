# Question 5:

import re

'''
PSEUDOCODE:
1. create 'counts' dictionary to store each category searched using RE
2. read a string from the user
3. use regular expressions to check for each category from the string & extend to dictionary these instances
	- re.findall(r'\d',str) (digit)
	- re.findall(r'\D',str) (nondigit) (NOTE: this includes whitespaces)
	- re.findall(r'\s',str) (whitespace)
	- re.findall(r'\b\w+\b', str) (words)
4. print results
'''

counts = {'digits':[],
	'non-digits':[],
	'whitespace':[],
	'words':[]}

inputStr = input("Enter a string: ")

# update counts with all instances of digits in the string
digits = re.findall(r'\d',inputStr)
counts['digits'].extend(digits)

# update counts with all instances of non-digits found in the string
nonDigits = re.findall(r'\D',inputStr)
counts['non-digits'].extend(nonDigits)

# update counts with all whitespaces found in the string
whitespaces = re.findall(r'\s',inputStr)
counts['whitespace'].extend(whitespaces)

# update counts with all words found in the string
words = re.findall(r'\b\w+\b',inputStr)
counts['words'].extend(words)

# print results
for category, catList in counts.items():
	print(f'{category} = {len(catList)}')