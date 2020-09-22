# Python RegEx
#-------------------------------------------------------------------------------------------
# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern. 

#-------------------------------------------------------------------------------------------
# For example

# ^a...s$
# The pattern is: any five character starting with 'a' and ending with 's'


import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)
print(result)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	

#-------------------------------------------------------------------------------------------=
# Python has a module named re to work with RegEx.

import re

pattern = '^a...s$'
test_string = ['abs','alias','abyss','Alias','abacus']


# abs - No match
# alias - Match
# abyss - Match
# Alias - No match
# An abacus -No match

result = [x for x in test_string if re.search(pattern,x)]
print(result)

#-------------------------------------------------------------------------------------------=
