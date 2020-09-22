# The available regex functions in the Python re module fall into the following three categories:

# Searching functions
# Substitution functions
# Utility functions

# The following sections explain these functions in more detail.
#-----------------------------------------------------------------------------------------------
# Searching Functions
#-----------------------------------------------------------------------------------------------

# Searching functions scan a search string for one or more matches of the specified regex:

#-----------------------------------------------------------------------------------------------
# Function	        Description
#-----------------------------------------------------------------------------------------------
# re.search()	      Scans a string for a regex match
# re.match()	      Looks for a regex match at the beginning of a string
# re.fullmatch()	  Looks for a regex match on an entire string
# re.findall()	    Returns a list of all regex matches in a string
# re.finditer()	    Returns an iterator that yields regex matches from a string


#-----------------------------------------------------------------------------------------------
# re.match(<regex>, <string>, flags=0)
#-----------------------------------------------------------------------------------------------

# Looks for a regex match at the beginning of a string.

# This is identical to re.search(), except that re.search() returns a match 
# if <regex> matches anywhere in <string>, whereas re.match() returns a match 
# only if <regex> matches at the beginning of <string>:

#-----------------------------------------------------------------------------------------------

import re
# Output : <re.Match object; span=(0, 3), match='123'>
print(re.search('\\d+','123abc456'))

# Output : <re.Match object; span=(3, 6), match='123'>
print(re.search('\\d+','abc123def456'))


# Output: <re.Match object; span=(0, 3), match='123'>
print(re.match('\\d+','123abc456'))

# Output: None
print(re.match('\\d+','abc123def456'))

#-----------------------------------------------------------------------------------------------

# The MULTILINE flag does not affect re.match() in this way:

s = 'sam\njoe\nben'

# Output: <re.Match object; span=(0, 3), match='sam'>
print(re.match('^sam',s))

# Output: None
print(re.match('^bar',s))

# Output: None
print(re.match('^bar',s,re.MULTILINE))


