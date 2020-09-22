#-------------------------------------------------------------------------------------------
# \d
# \D
#-------------------------------------------------------------------------------------------
# Match based on whether a character is a decimal digit.

# \d matches any decimal digit character. 
# \D is the opposite. It matches any character that isn’t a decimal digit:

# \d is essentially equivalent to [0-9], and 
# \D is equivalent to [^0-9].

#-------------------------------------------------------------------------------------------
import re

# output : <re.Match object; span=(3, 4), match='4'>
print(re.search('\\d','abc4def'))

# output : <re.Match object; span=(3, 4), match='d'>
print(re.search('\\D','123d456'))

#-------------------------------------------------------------------------------------------