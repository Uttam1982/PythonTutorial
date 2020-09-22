# (?<=<lookbehind_regex>)
#------------------------------------------------------------------------------------------------
# Creates a positive lookbehind assertion.

# (?<=<lookbehind_regex>) asserts that what precedes the regex parser’s 
# current position must match <lookbehind_regex>.

#------------------------------------------------------------------------------------------------
# In the following example, the lookbehind assertion specifies that 'foo' must precede 'bar':

import re

# Output : <re.Match object; span=(3, 6), match='bar'>
print(re.search('(?<=foo)bar','foobar'))


# Output : None
print(re.search('(?<=qux)bar','foobar'))

# The <lookbehind_regex> in a lookbehind assertion must specify a match of fixed length.

# Output : <re.Match object; span=(3, 6), match='def'>
print(re.search('(?<=a{3})def', 'aaadef'))

# Output: re.error: look-behind requires fixed-width pattern
print(re.search('(?<=a+)def', 'aaadef'))