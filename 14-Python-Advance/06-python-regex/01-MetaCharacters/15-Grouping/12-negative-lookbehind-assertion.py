# (?<!<lookbehind_regex>)
#------------------------------------------------------------------------------------------------
# Creates a negative lookbehind assertion.


# (?<!<lookbehind_regex>) asserts that what precedes the regex parser’s current 
# position must not match <lookbehind_regex>:

#------------------------------------------------------------------------------------------------

import re

# Output : None
print(re.search('(?<!foo)bar', 'foobar'))

# Output : <re.Match object; span=(3, 6), match='bar'>
print(re.search('(?<!qux)bar', 'foobar'))




