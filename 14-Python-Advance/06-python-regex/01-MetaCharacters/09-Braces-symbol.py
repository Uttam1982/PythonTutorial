#---------------------------------------------------------------------------------------
# {} - Braces
#---------------------------------------------------------------------------------------
# Consider this code: {n,m}. This means at least n, and at most m repetitions of 
# the pattern left to it.

import re

pattern = "a{2,3}"

list_str = ['abc dat','abc daat','aabc daaat','aabc daaaat']

# abc dat	    : No match
# abc daat	  : 1 match (at daat)
# aabc daaat	: 2 matches (at aabc and daaat)
# aabc daaaat	: 2 matches (at aabc and daaaat)


result = [ x for x in list_str if re.search(pattern,x)]
print(result)

#---------------------------------------------------------------------------------------

import re

pattern = "[0-9]{2,4}"

list_str = ['ab123csde','12 and 345673','1 and 2']

# ab123csde	    : 1 match (match at ab123csde)
# 12 and 345673	: 3 matches (12, 3456, 73)
# 1 and 2	      : No match

result = [ x for x in list_str if re.search(pattern,x)]
print(result)

#---------------------------------------------------------------------------------------
