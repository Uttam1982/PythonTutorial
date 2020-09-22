#----------------------------------------------------------------------------------------
# . - Period
#----------------------------------------------------------------------------------------
# A period matches any single character (except newline '\n').

import re
pattern = ".."
test_data = ['a','ac','acd','acde','\na']

# a     :	No match
# ac    :	1 match
# acd   :	1 match
# acde  :	2 matches (contains 4 characters)

result = [x for x in test_data if re.match(pattern,x)]
print(result)

#----------------------------------------------------------------------------------------




