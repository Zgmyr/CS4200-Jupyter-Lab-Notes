# Question 2:
# Re-implementing code from question 1 using regular expressions...
# we do not need to use tokens, nor do we need functions

import re

# Get input
inputStr = input("Enter a sentence to be processed:")


# a - print reversed tokens


# tokenize the input string by one or more whitespaces (r'\s+')
inputTokens = re.split(r'\s+',inputStr)

# print the reversed list (reverse then join)
print(' '.join(inputTokens[::-1]))


# b - print words beginning with 'b'


# 'findall' strings starting with 'b'
# '\b' specifies a whole word beginning with b (eliminating results from words containing 'b' not at the beginning)
# 're.IGNORECASE' includes both words beginning with 'b' as well as 'B'
# source: https://docs.python.org/3/library/re.html
bTokens = re.findall(r'\bb\S*',inputStr, re.IGNORECASE)

# print all strings beginning with 'b'
print(' '.join(bTokens))


# c - print words ending with 'ed'


# 'findall' strings ending with 'ed'
# '\b' used here to specify end of word (word boundary)
# '\w' matches all alphanumeric characters & the underscore
# source: https://docs.python.org/3/library/re.html#regular-expression-syntax
edTokens = re.findall(r'\w*ed\b',inputStr)
print(edTokens)