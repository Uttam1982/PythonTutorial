# re.findall(<regex>, <string>, flags=0)
#-----------------------------------------------------------------------------------------------

# Returns a list of all matches of a regex in a string.

# re.findall(<regex>, <string>) returns a list of all non-overlapping matches of <regex> 
# in <string>. It scans the search string from left to right and returns all matches in 
# the order found:

#-----------------------------------------------------------------------------------------------

import re

# Output : ['foo', 'bar', 'baz']
print(re.findall(r'\w+','...foo,,,bar:%$baz//|'))

#-----------------------------------------------------------------------------------------------
# If <regex> contains a capturing group, 
# then the return list contains only contents of the group, not the entire match:
#-----------------------------------------------------------------------------------------------

# Output : ['foo', 'bar', 'baz']
print(re.findall(r'#(\w+)#','#foo#---#bar#---#baz#'))

# In this case, the specified regex is #(\w+)#. 
# The matching strings are '#foo#', '#bar#', and '#baz#'. 
# But the hash (#) characters don’t appear in the return list 
# because they’re outside the grouping parentheses.

#-----------------------------------------------------------------------------------------------
# If <regex> contains more than one capturing group, then re.findall() 
# returns a list of tuples containing the captured groups. The length of 
# each tuple is equal to the number of groups specified:

# Output : [('sam', 'joe'), ('ben', 'sara'), ('ali', 'alex')]
print(re.findall(r'(\w+),(\w+)','sam,joe,ben,sara,ali,alex'))

# Output : [('sam', 'joe', 'ben'), ('sara', 'ali', 'alex')]
print(re.findall(r'(\w+),(\w+),(\w+)','sam,joe,ben,sara,ali,alex'))

# In the first example, the regex  contains two capturing groups, 
# so re.findall() returns a list of three two-tuples, each containing two captured matches. 
# In the second example regex contains three groups, so the return value is a list of two 
# three-tuples.
