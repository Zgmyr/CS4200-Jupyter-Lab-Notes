# Question 1:

'''
PSEUDOCODE:
1. read line of text & tokenize it
2. pass toeknized text to 3 functions:
	3. reverse(list)
	- returns reversed list
	4. startsWithB(list)
	- form new list from tokens beginning with letter 'b'
	- return this new list
	5. endsInEd(list)
	- form new list from tokens ending with 'ed'
	- return this new list
'''

# Get input & form tokenized list
inputStr = input("Enter a sentence to be processed:")
inputTokens = inputStr.split(" ")

# a - returns a reversed list
def reverseTokens(list):
	return list[::-1]

# print reversed tokens
revTokens = reverseTokens(inputTokens)
revStr = ' '.join(revTokens)
print("Reversed string: ", revStr)

# b - returns only tokens beginning with letter 'b'
def beginsWithB(list):
	# list comprehension - form list of tokens beginning with 'b' (case insensitive)
	tmpList = [token for token in list if token[0].lower() == 'b']
	return tmpList

# print tokens beginning with 'b'
bTokens = beginsWithB(inputTokens)
bStrings = ' '.join(bTokens)
print("Strings beginning with 'b': ", bStrings)

# c - returns only tokens ending with 'ed'
def endsWithEd(list):
	# list comprehension - form list of tokens ending with 'ed' (case insensitive)
	tmpList = [token for token in list if token[-2:].lower() == 'ed']
	return tmpList

# print tokens ending with 'ed'
edTokens = endsWithEd(inputTokens)
edStrings = ' '.join(edTokens)
print("Strings ending with 'ed': ", edStrings)