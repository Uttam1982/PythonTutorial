# re.M
# re.MULTILINE
#-------------------------------------------------------------------------------------------------
# Causes start-of-string and end-of-string anchors to match at embedded newlines.

# By default, the ^ (start-of-string) and $ (end-of-string) anchors match only at 
# the beginning and end of the search string:

#-------------------------------------------------------------------------------------------------

import re


s = 'sam\njoe\nben'

# Output
# sam
# joe
# ben
print(s)

#-------------------------------------------------------------------------------------------------
# the ^ (start-of-string) anchors
#-------------------------------------------------------------------------------------------------

# Output : <re.Match object; span=(0, 3), match='sam'>
print(re.search('^sam',s))

# Output : None
print(re.search('^joe',s))

# Output : None
print(re.search('^ben',s))

#-------------------------------------------------------------------------------------------------
# using re.MULTILINR | re.M
#-------------------------------------------------------------------------------------------------
# Output : <re.Match object; span=(0, 3), match='sam'>
print(re.search('^sam',s,re.MULTILINE))

# Output : <re.Match object; span=(4, 7), match='joe'>
print(re.search('^joe',s,re.MULTILINE))

# Output : <re.Match object; span=(8, 11), match='ben'>
print(re.search('^ben',s,re.M))


#-------------------------------------------------------------------------------------------------
# $ (end-of-string) anchors
#-------------------------------------------------------------------------------------------------

# Output : None
print(re.search('sam$',s))

# Output : None
print(re.search('joe$',s))

# Output : <re.Match object; span=(8, 11), match='ben'>
print(re.search('ben$',s))


#-------------------------------------------------------------------------------------------------
# using re.MULTILINR | re.M
#-------------------------------------------------------------------------------------------------

# Output : <re.Match object; span=(0, 3), match='sam'>
print(re.search('sam$',s,re.MULTILINE))

# Output : <re.Match object; span=(4, 7), match='joe'>
print(re.search('joe$',s,re.MULTILINE))

# Output : <re.Match object; span=(8, 11), match='ben'>
print(re.search('ben$',s,re.M))

#-------------------------------------------------------------------------------------------------

# Note: The MULTILINE flag only modifies the ^ and $ anchors in this way. 
# It doesn’t have any effect on the \A and \Z anchors:


# Output : None
print(re.search('\\Aben',s,re.M))

# Output : None
print(re.search('joe\\Z',s,re.MULTILINE))
