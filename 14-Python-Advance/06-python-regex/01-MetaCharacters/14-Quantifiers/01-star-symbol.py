#--------------------------------------------------------------------------------------------
# Quantifiers
#--------------------------------------------------------------------------------------------

# A quantifier metacharacter immediately follows a portion of a <regex> 
# and indicates how many times that portion must occur for the match to succeed.

#--------------------------------------------------------------------------------------------
# *
#--------------------------------------------------------------------------------------------


# Matches zero or more repetitions of the preceding regex.


#--------------------------------------------------------------------------------------------

import re

# Output : <re.Match object; span=(0, 6), match='foobar'>
print(re.search('foo-*bar','foobar'))  # zero dash

# Output : <re.Match object; span=(0, 7), match='foo-bar'>
print(re.search('foo-*bar','foo-bar'))

# Output : <re.Match object; span=(0, 8), match='foo--bar'>
print(re.search('foo-*bar','foo--bar'))

# Output : <re.Match object; span=(2, 14), match='foo @#$% bar'>
print(re.search("foo.*bar","# foo @#$% bar #"))

#--------------------------------------------------------------------------------------------