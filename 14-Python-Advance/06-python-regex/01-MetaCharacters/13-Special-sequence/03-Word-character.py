#-------------------------------------------------------------------------------------------
# \w
# \W
#-------------------------------------------------------------------------------------------

# Match based on whether a character is a word character.
# \w matches any alphanumeric word character. 
# Word characters are uppercase and lowercase letters, digits, and the underscore (_) character, 
# so \w is essentially shorthand for [a-zA-Z0-9_]:

#-------------------------------------------------------------------------------------------

import re

# Output: <re.Match object; span=(3, 4), match='a'>
print(re.search('\\w','#(.a$@&'))

# Output: <re.Match object; span=(3, 4), match='a'>
print(re.search('[a-zA-Z0-9_]','#(.a$@&'))

#-------------------------------------------------------------------------------------------
# \W is the opposite. It matches any non-word character and is equivalent to [^a-zA-Z0-9_]:
#-------------------------------------------------------------------------------------------

# Output: <re.Match object; span=(0, 1), match='#'>
print(re.search('\\W','#(.a$@&'))

# Output: <re.Match object; span=(0, 1), match='#'>
print(re.search('[^a-zA-Z0-9_]','#(.a$@&'))