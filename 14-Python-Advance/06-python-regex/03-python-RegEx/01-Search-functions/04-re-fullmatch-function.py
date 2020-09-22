# re.fullmatch(<regex>, <string>, flags=0)
#-----------------------------------------------------------------------------------------------
# Looks for a regex match on an entire string.

# This is similar to re.search() and re.match(), but re.fullmatch() returns 
# a match only if <regex> matches <string> in its entirety:

#-----------------------------------------------------------------------------------------------

import re

# Output : None
print(re.fullmatch(r'\d+', '123foo'))

# Output : None
print(re.fullmatch(r'\d+', 'foo123'))

# Output : None
print(re.fullmatch(r'\d+', 'foo123bar'))

# Output : <re.Match object; span=(0, 3), match='123'>
print(re.fullmatch(r'\d+', '123'))

# Output : <re.Match object; span=(0, 3), match='123'>
print(re.fullmatch(r'\d+$', '123'))

#-----------------------------------------------------------------------------------------------