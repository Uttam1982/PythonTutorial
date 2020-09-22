#--------------------------------------------------------------------------------------------
# re.split(<regex>, <string>, maxsplit=0, flags=0)
#--------------------------------------------------------------------------------------------

# Splits a string into substrings.

# re.split(<regex>, <string>) splits <string> into substrings using <regex> 
# as the delimiter and returns the substrings as a list.

#--------------------------------------------------------------------------------------------

import re

# The following example splits the specified string into substrings 
# delimited by a comma (,), semicolon (;), or slash (/) character, surrounded 
# by any amount of whitespace:

regex = r'\s*[,;/]\s*'

# Output : return a list  
# ['foo', 'bar', 'baz', 'qux']
print(re.split(regex,'foo,bar  ;  baz / qux'))


#--------------------------------------------------------------------------------------------

# If <regex> contains capturing groups, then the return list includes the matching 
# delimiter strings as well:

regex = r'(\s*[,;/]\s*)'

# Output : return a list  
# 'foo', ',', 'bar', '  ;  ', 'baz', ' / ', 'qux']
print(re.split(regex,'foo,bar  ;  baz / qux'))

# This time, the return list contains not only the substrings 'foo', 'bar', 'baz', 
# and 'qux' but also several delimiter strings:

# ','
# ' ; '
# ' / '

#--------------------------------------------------------------------------------------------

# If you need to use groups but don’t want the delimiters included in the return list, 
# then you can use noncapturing groups:

string = 'foo,bar  ;  baz / qux'
regex = r'(?:\s*[,;/]\s*)'

# Output: ['foo', 'bar', 'baz', 'qux']
print(re.split(regex,string))


#--------------------------------------------------------------------------------------------

# If the optional maxsplit argument is present and greater than zero, then re.split() 
# performs at most that many splits. The final element in the return list is the 
# remainder of <string> after all the splits have occurred:

s = 'foo, bar, baz, qux, quux, corge'

# output : ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(re.split(r',\s*',s))

# output : ['foo', 'bar', 'baz, qux, quux, corge']
print(re.split(r',\s*',s, maxsplit=2))  


# Output : ['', '/', 'foo', '/', 'bar', '/', 'baz', '/', '']
print(re.split('(/)', '/foo/bar/baz/'))


# In this case, the <regex> delimiter is a single slash (/) character. 
# In a sense, then, there’s an empty string to the left of the first delimiter 
# and to the right of the last one. So it makes sense that re.split() 
# places empty strings as the first and last elements of the return list.
