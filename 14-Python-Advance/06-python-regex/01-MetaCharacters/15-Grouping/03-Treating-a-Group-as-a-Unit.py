#-------------------------------------------------------------------------------------------
# Treating a Group as a Unit
#-------------------------------------------------------------------------------------------
# A quantifier metacharacter that follows a group operates 
# on the entire subexpression specified in the group as a single unit.

import re

# Output: <re.Match object; span=(4, 7), match='bar'>
print(re.search('(bar)+','foo bar baz'))

# Output: <re.Match object; span=(4, 10), match='barbar'>
print(re.search('(bar)+','foo barbar baz'))

# Output: <re.Match object; span=(4, 16), match='barbarbarbar'>
print(re.search('(bar)+','foo barbarbarbar baz'))

#-------------------------------------------------------------------------------------------

# 'bar+'

# The + metacharacter applies only to the character 'r'.
# 'ba' followed by one or more occurrences of 'r'
# Examples : 'bar', 'barr','barrr'

# (bar)+

# The + metacharacter applies to the entire string 'bar'.
# One or more occurrences of 'bar',
# Examples: 'bar, barbar', 'barbarbar'

#-------------------------------------------------------------------------------------------
# The regex (ba[rz]){2,4}(qux)?
#-------------------------------------------------------------------------------------------
# matches 2 to 4 occurrences of either 'bar' or 'baz', 
# optionally followed by 'qux':

# Output: <re.Match object; span=(0, 12), match='barbazbarqux'>
print(re.search('(ba[rz]){2,4}(qux)?','barbazbarqux'))

# Output: <re.Match object; span=(0, 6), match='barbar'>
print(re.search('(ba[rz]){2,4}(qux)?','barbar'))

#-------------------------------------------------------------------------------------------
# The regex (foo(bar)?)+(\d\d\d)?
#-------------------------------------------------------------------------------------------

# foo(bar)?     : foo optionally followed bar
# (foo(bar)?)+  : one or more occurance of the above
# \d\d\d        : three decimal digit
# (\d\d\d)?     : Zero or one occurance of the above

# Output: <re.Match object; span=(0, 9), match='foofoobar'>
print(re.search('(foo(bar)?)+(\\d\\d\\d)?','foofoobar'))

# Output: <re.Match object; span=(0, 12), match='foofoobar123'>
print(re.search('(foo(bar)?)+(\\d\\d\\d)?','foofoobar123'))

# Output: <re.Match object; span=(0, 9), match='foofoo123'>
print(re.search('(foo(bar)?)+(\\d\\d\\d)+','foofoo123'))

#-------------------------------------------------------------------------------------------