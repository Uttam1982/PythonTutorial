#--------------------------------------------------------------------------------------------
# ?
#--------------------------------------------------------------------------------------------

# Matches zero or one repetitions of the preceding regex.

# Again, this is similar to * and +, but in this case there’s only a match if the preceding 
# regex occurs once or not at all:

#--------------------------------------------------------------------------------------------

import re

# Output: <re.Match object; span=(0, 6), match='foobar'>
print(re.search('foo-?bar','foobar')) # zero dash

# Output : <re.Match object; span=(0, 7), match='foo-bar'>
print(re.search('foo-?bar','foo-bar')) # one dash

# Output  : None
print(re.search('foo-?bar','foo--bar')) # two dash

#--------------------------------------------------------------------------------------------
# Here are some more examples showing the use of all three quantifier metacharacters:

# Output : <re.Match object; span=(0, 6), match='foobar'>
print(re.match('foo[1-9]*bar', 'foobar'))

# Output : <re.Match object; span=(0, 8), match='foo24bar'>
print(re.match('foo[1-9]*bar', 'foo24bar'))

# Output : None
print(re.match('foo[1-9]+bar', 'foobar'))

# Output : <re.Match object; span=(0, 8), match='foo24bar'> 
print(re.match('foo[1-9]+bar', 'foo24bar'))

# Output : <re.Match object; span=(0, 6), match='foobar'>
print(re.match('foo[1-9]?bar', 'foobar'))

# Output : None
print(re.match('foo[1-9]?bar', 'foo24bar'))

#--------------------------------------------------------------------------------------------

