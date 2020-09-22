# Special Sequences
#---------------------------------------------------------------------------------------
# Special sequences make commonly used patterns easier to write. 
# Here's a list of special sequences:


#---------------------------------------------------------------------------------------
# \s - Matches where a string contains any whitespace character. 
#---------------------------------------------------------------------------------------
# Equivalent to [ \t\n\r\f\v].

import re

print("\\s - Matches where a string contains any whitespace character. ")

pattern = '\\s'

list_str = ['Python RegEx', 'PythonRegEx']

# Python RegEx	: 1 match
# PythonRegEx	  : No match

result = [x for x in list_str if re.search(pattern,x)]
print(result)

#---------------------------------------------------------------------------------------
# \S - Matches where a string contains any non-whitespace character.
#--------------------------------------------------------------------------------------- 

# Equivalent to [^ \t\n\r\f\v].

import re

print("\\S - Matches where a string contains any non-whitespace character. ")

pattern = '\\S'

list_str = ['Python RegEx', ' ','PythonRegEx']

# Python RegEx	: 1 match
# ' '	          : No match

result = [x for x in list_str if re.search(pattern,x)]
print(result)

#---------------------------------------------------------------------------------------
# \w - Matches any alphanumeric character (digits and alphabets). 
#---------------------------------------------------------------------------------------

# Equivalent to [a-zA-Z0-9_]. By the way, underscore _ is also 
# considered an alphanumeric character.

import re

print("\\w - Matches any alphanumeric character (digits and alphabets).  ")

pattern = '\\w'

list_str = ['123abc', '12&": ;c','ab 123','xyz_123','%"> !','%"> !_']

# '123abc'    : 6 matches(at 123abc)
# '12&": ;c'  : 2 matches( at 12 and c)
# 'ab 123'    : 5 matches (at ab and 123)
# 'xyz_123'   : 7 matches( at xyz_123)
# '%"> !'     : No Match
# '%"> !_'    : 1 match (at _)

result = [x for x in list_str if re.search(pattern,x)]
print(result)

#---------------------------------------------------------------------------------------
# \W - Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]
#---------------------------------------------------------------------------------------

import re

print("\\W - Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]")

pattern = '\\W'

list_str = ['123abc', '12&": ;c','ab 123','xyz_123','%"> !','%"> !_']

# '123abc'    : No matches
# '12&": ;c'  : 5 matches( at &": ;)
# 'ab 123'    : 1 matches (at ab 123)
# 'xyz_123'   : No matches
# '%"> !'     : 5 matches (at %"> !)
# '%"> !_'    : 5 matches (at%"> !)

result = [x for x in list_str if re.search(pattern,x)]
print(result)

#---------------------------------------------------------------------------------------
# \Z - Matches if the specified characters are at the end of a string.
#---------------------------------------------------------------------------------------

import re

print("Python\\Z - Matches if the specified characters are at the end of a string.")

pattern = 'Python\\Z'

list_str = ['I like Python','I like Python Programming','Python is fun.']

result = [x for x in list_str if re.search(pattern,x)]
print(result)

#---------------------------------------------------------------------------------------
