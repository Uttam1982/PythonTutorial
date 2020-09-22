# (?#...)
#---------------------------------------------------------------------------------------
# Specifies a comment.

# The regex parser ignores anything contained in the sequence (?#...):

#---------------------------------------------------------------------------------------

import re

# Output : <re.Match object; span=(4, 11), match='bar baz'>
print(re.search('bar(?#This is a comment) *baz','foo bar baz qux'))


#---------------------------------------------------------------------------------------
# Vertical bar, or pipe (|)

# Specifies a set of alternatives on which to match.


# An expression of the form <regex1>|<regex2>|...|<regexn> matches at most one of 
# the specified <regexi> expressions:
#---------------------------------------------------------------------------------------

# Output: <re.Match object; span=(0, 3), match='bar'>
print(re.search('foo|bar|baz', 'bar'))

# Output : <re.Match object; span=(0, 3), match='baz'>
print(re.search('foo|bar|baz', 'baz'))


# Output : None
print(re.search('sam|ben|jeo', 'sara'))


# Here, foo|bar|baz will match any of 'foo', 'bar', or 'baz'. 
# You can separate any number of regexes using |.

#---------------------------------------------------------------------------------------

# Alternation is non-greedy. The regex parser looks at the expressions separated by | 
# in left-to-right order and returns the first match that it finds. The remaining 
# expressions aren’t tested, even if one of them would produce a longer match

# Output : <re.Match object; span=(0, 3), match='sam'>
print(re.search('sam','samjoe'))

# Output : <re.Match object; span=(3, 6), match='joe'>
print(re.search('joe','samjoe'))

# Output : <re.Match object; span=(0, 3), match='sam'>
print(re.search('sam|joe','samjoe'))

#---------------------------------------------------------------------------------------
# You can combine alternation, grouping, and any other metacharacters to achieve whatever 
# level of complexity you need

# Output : <re.Match object; span=(0, 9), match='samsamsam'>
print(re.search('(sam|joe|ben)+','samsamsam'))

# Output : <re.Match object; span=(0, 12), match='benbenbenben'>
print(re.search('(sam|joe|ben)+','benbenbenben'))

# Output : <re.Match object; span=(0, 9), match='joebensam'>
print(re.search('(sam|joe|ben)+', 'joebensam'))

#---------------------------------------------------------------------------------------