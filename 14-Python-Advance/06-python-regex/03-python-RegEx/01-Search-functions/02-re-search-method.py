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
# 1. re.search(<regex>, <string>, flags=0)
#-----------------------------------------------------------------------------------------------

# Scans a string for a regex match.

#-----------------------------------------------------------------------------------------------
import re

# output : <re.Match object; span=(3, 6), match='123'>
print(re.search("\\d+",'sam123joe456'))


# output : <re.Match object; span=(3, 6), match='joe'>
print(re.search("[a-z]+",'123joe456sam',re.IGNORECASE))

# Output : None
print(re.search(r'\d+', 'foo.bar'))


# if <string> contains embedded newlines, then the MULTILINE flag causes re.search() 
# to match the caret (^) anchor metacharacter either at the beginning of <string> or 
# at the beginning of any line contained within <string>:

s = 'sam\njoe\nben'

# Output : None
print(re.search('^joe',s))

# Output : <re.Match object; span=(4, 7), match='joe'>
print(re.search('^joe',s,re.MULTILINE))