#-----------------------------------------------------------------------------------------------
# re.finditer(<regex>, <string>, flags=0)
#-----------------------------------------------------------------------------------------------

# Returns an iterator that yields regex matches.

#-----------------------------------------------------------------------------------------------

# re.finditer(<regex>, <string>) scans <string> for non-overlapping matches of 
# <regex> and returns an iterator that yields the match objects from any it finds. 
# It scans the search string from left to right and returns matches in the order it finds them:

#-----------------------------------------------------------------------------------------------

import re

it = re.finditer(r'\w+', '...foo,,,bar:%$baz//|')

# Output: 
# <re.Match object; span=(3, 6), match='foo'>
# <re.Match object; span=(9, 12), match='bar'>
# <re.Match object; span=(15, 18), match='baz'>

for i in it:
  print(i)


#-----------------------------------------------------------------------------------------------
# Difference between findall() and finditer()
#-----------------------------------------------------------------------------------------------

# re.findall() and re.finditer() are very similar, but they differ in two respects:

# re.findall() returns a list, whereas re.finditer() returns an iterator.

# The items in the list that re.findall() returns are the actual matching strings, 
# whereas the items yielded by the iterator that re.finditer() returns are match objects.

#-----------------------------------------------------------------------------------------------

