#-------------------------------------------------------------------------------------------
# Grouping Constructs and Backreferences
#-------------------------------------------------------------------------------------------

# Grouping constructs break up a regex in Python into subexpressions or groups. 

# This serves two purposes:

# Grouping: 

# A group represents a single syntactic entity. 
# Additional metacharacters apply to the entire group as a unit.

#-------------------------------------------------------------------------------------------
# Capturing: 

# Some grouping constructs also capture the portion of the search 
# string that matches the subexpression in the group. You can retrieve captured 
# matches later through several different mechanisms.

#-------------------------------------------------------------------------------------------
# (<regex>)

# Defines a subexpression or group.

# This is the most basic grouping construct. 
# A regex in parentheses just matches the contents of the parentheses:

#-------------------------------------------------------------------------------------------

import re

# Output: <re.Match object; span=(4, 7), match='bar'>
print(re.search('(bar)','foo bar baz'))

# Output: <re.Match object; span=(4, 7), match='bar'>
print(re.search('bar','foo bar baz'))

# As a regex, (bar) matches the string 'bar', 
# the same as the regex bar would without the parentheses.

#-------------------------------------------------------------------------------------------