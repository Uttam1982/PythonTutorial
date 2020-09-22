#----------------------------------------------------------------------------------------
# ^ - Caret
#----------------------------------------------------------------------------------------

# The caret symbol ^ is used to check if a string starts with a certain character.

import re

pattern = "^a"

# a	  : 1 match
# abc	: 1 match
# bac	: No match

list_str = ['a','abc','bac','Acb']

result = [x for x in list_str if re.search(pattern,x)]
print(result)

#----------------------------------------------------------------------------------------

import re

pattern = "^ab"

# abc	: 1 match
# acb	: No match (starts with a but not followed by b)

list_str = ['abc','acb','Abc','abbc']

result = [x for x in list_str if re.search(pattern,x)]
print(result)

#----------------------------------------------------------------------------------------