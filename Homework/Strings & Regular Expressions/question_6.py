# Question 6:
# Goal: for all instances of 'I' or 'I'm', swap these words with the words prior to their occurence

import re

'''
PSEUDOCODE:
1. Using re.sub to detect a pattern in the string and replace it (swapping words)
	- create a regular expression pattern that swaps two words (using a capture groups)
	- pattern specified by a word (one or more alphanumeric characters), followed by whitespace, followed by 'I' or 'I'm'
	- group the word into its own capture group, and the pattern 'I' or 'I'm' into its own capture group
	- replacement pattern for re.sub will be r'\2 \1', swapping the positions of the two capture groups
'''

quote = (
"Because not I'm a Vanderbilt, suddenly white I'm trash? "
"grew I up in Bel Air, Warner. Across the street from Aaron Spelling. "
"think I most people would agree that's a lot better than some stinky old Vanderbilt."
)

# Capture Groups:
# capture groups specified with (...) ~ each captured group referenced with \1, \2, \3, etc.
# non-capture groups specified with (?:...) ~ contents treated as group but not referenced like normal capture groups (...)
# source: https://docs.python.org/3/library/re.html#regular-expression-syntax

# Capture group \1: (any given word, or string of one or more alphanumeric charactetrs)
# (\w+)

# Capture group \2: (either the pattern 'I' or 'I'm')
#	we can use non-capture group to optionally (?:...)? select I'm
# (I(?:\'m)?)

# NOTE: these two capture groups will be separated by one or more whitespace characters (e.g. word (space) I'm)

fixedQuote = re.sub(r'(\w+)\s+(I(?:\'m)?)',r'\2 \1',quote)
print(fixedQuote)