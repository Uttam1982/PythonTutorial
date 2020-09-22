# (?!<lookahead_regex>)

# Creates a negative lookahead assertion.

# (?!<lookahead_regex>) asserts that what follows the regex parser’s current 
# position must not match <lookahead_regex>.

#------------------------------------------------------------------------------------------------
import re
# postive lookahead
# Output: <re.Match object; span=(0, 3), match='foo'>
print(re.search('foo(?=[a,b])','foobar'))

# negative lookahead 
# Output: None
print(re.search('foo(?![a,b])','foobar'))

# postive lookahead
# Output: None
print(re.search('foo(?=[a,b])','foo123'))

# negative lookahead 
# Output: <re.Match object; span=(0, 3), match='foo'>
print(re.search('foo(?![a,b])','foo123'))

#------------------------------------------------------------------------------------------------