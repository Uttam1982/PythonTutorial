#------------------------------------------------------------------------------------
# ^
# \A
#------------------------------------------------------------------------------------
# Anchor a match to the start of <string>.

# When the regex parser encounters ^ or \A, the parser’s current position must 
# be at the beginning of the search string for it to find a match.

#------------------------------------------------------------------------------------

import re

# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search('^foo','foobar'))

# Output : None
print(re.search('^foo','barfoo'))

# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search('\\Afoo','foobar'))

# Output : None
print(re.search('\\Afoo','barfoo'))

print("*"*100)
#------------------------------------------------------------------------------------

# ^ and \A behave slightly differently from each other in MULTILINE mode. 
# You’ll learn more about MULTILINE mode on flags
#------------------------------------------------------------------------------------

s = 'foo\nbar\nbaz'

#Output
# foo
# bar
# baz
print(s)

# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search('^foo', s))
# Output : None
print(re.search('^bar', s))
# Output : None
print(re.search('^baz', s))

print("*"*100)
# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search('^foo', s, re.MULTILINE))
# Output : <re.Match object; span=(4, 7), match='bar'>
print(re.search('^bar', s, re.M))
# Output : <re.Match object; span=(8, 11), match='baz'>
print(re.search('^baz', s,re.M))

#------------------------------------------------------------------------------------
print("*"*100)

s = 'foo\nbar\nbaz'

# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search('\\Afoo', s))
# Output : None
print(re.search('\\Abar', s))
# Output : None
print(re.search('\\Abaz', s))

print("*"*100)

# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search('\\Afoo', s, re.MULTILINE))
# Output : None
print(re.search('\\Abar', s, re.M))
# Output : None
print(re.search('\\Abaz', s,re.M))

#------------------------------------------------------------------------------------



