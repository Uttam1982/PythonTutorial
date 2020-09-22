#--------------------------------------------------------------------------------------------
# +
#--------------------------------------------------------------------------------------------

# Matches one or more repetitions of the preceding regex.

# This is similar to *, but the quantified regex must occur at least once:

#--------------------------------------------------------------------------------------------

import re

# Output : None
print(re.search('foo-+bar','foobar')) # zero dashes

# Output : <re.Match object; span=(0, 7), match='foo-bar'>
print(re.search('foo-+bar','foo-bar')) # one dash


# Output : <re.Match object; span=(0, 8), match='foo--bar'>
print(re.search('foo-+bar','foo--bar')) # two dashes