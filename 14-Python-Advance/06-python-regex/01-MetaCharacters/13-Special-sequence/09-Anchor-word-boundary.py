#----------------------------------------------------------------------------------------------
# \b
# Anchors a match to a word boundary.
#----------------------------------------------------------------------------------------------
# \b asserts that the regex parser’s current position must be at the beginning or end of a word.

# A word consists of a sequence of alphanumeric characters or underscores ([a-zA-Z0-9_]), 
# the same as for the \w character class:

#----------------------------------------------------------------------------------------------

# At the begining
import re

# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search(r'\bfoo', 'foo bar'))

# Output : None
print(re.search(r'\bfoo', 'barfoo'))

# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search(r'\bfoo', 'foo.bar'))

print('x'*100)

#----------------------------------------------------------------------------------------------
# At the end

# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search(r'foo\b', 'foo bar'))

# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search(r'foo\b', 'foo.bar'))

# Output : None
print(re.search(r'foo\b', 'foobar'))

#----------------------------------------------------------------------------------------------
# Using the \b anchor on both ends of the <regex> 
#----------------------------------------------------------------------------------------------
# will cause it to match when it’s present in the search string as a whole word:

# Output : <re.Match object; span=(4, 7), match='bar'>
print(re.search(r'\bbar\b', 'foo bar baz'))

# Output : <re.Match object; span=(4, 7), match='bar'>
print(re.search(r'\bbar\b', 'foo(bar)baz'))

# Output : None
print(re.search(r'\bbar\b', 'foobarbaz'))



#----------------------------------------------------------------------------------------------
# \B
# Anchors a match to a location that isn’t a word boundary.
#----------------------------------------------------------------------------------------------

# \B does the opposite of \b. It asserts that the regex parser’s current position 
# must not be at the start or end of a word:

import re

# Output : None
print(re.search(r'\Bfoo\B', 'foo'))

# Output : None
print(re.search(r'\Bfoo\B', '.foo.'))

# Output : <re.Match object; span=(3, 6), match='foo'>
print(re.search(r'\Bfoo\B', 'barfoobaz'))