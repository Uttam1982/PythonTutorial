#------------------------------------------------------------------------------------------
# (?:<regex>)
#------------------------------------------------------------------------------------------

# Creates a non-capturing group.

# (?:<regex>) is just like (<regex>) in that it matches the specified <regex>. 
# But (?:<regex>) doesn’t capture the match for later retrieval:

#------------------------------------------------------------------------------------------
import re

m = re.search('(\\w+),(?:\\w+),(\\w+)','foo,bar,baz')

# Output: <re.Match object; span=(0, 11), match='foo,bar,baz'>
print(m)

# ('foo', 'baz')
print(m.groups())
# 'foo'
print(m.group(1))
# 'baz'
print(m.group(2))


# In this example, the middle word 'bar' sits inside non-capturing parentheses, 
# so it’s missing from the tuple of captured groups. It isn’t retrievable from 
# the match object, nor would it be referable by backreference.

# Why would you want to define a group but not capture it?

