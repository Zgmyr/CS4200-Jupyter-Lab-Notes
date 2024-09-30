# Question 4:

from global_vars import *
import re

if Bday % 2 == 0:
	print("Birthdy is even - problem 'a'")
else:
	print("Birthday is odd - problem 'b'")

'''
PSEUDOCODE:
1. given some url string (e.g. https://docs.python.org/3/library/re.html#)
2. use re to test for:
	- 5 characters, colon, two slashes (protocol)
	- 1 or more characters followed by a period (subdomain)
	- 1 or more characters followed by a period (second level domain)
	- 2 or more characters (top level domain / extension)
3. return result
'''
# URL to find using RE:
strURL = "Read more about regular expressions at https://docs.python.org/3/library/re.html# !"

# use regular expression r'\w{5}://\w+\.\w+\.\w{2,3}'
results = re.findall(r'\w{5}://\w+\.\w+\.\w{2,3}',strURL)

# print result
print("URL found: ", results)