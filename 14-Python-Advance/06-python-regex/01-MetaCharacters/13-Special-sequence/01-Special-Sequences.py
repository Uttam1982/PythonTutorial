# Special Sequences
#---------------------------------------------------------------------------------------
# Special sequences make commonly used patterns easier to write. 
# Here's a list of special sequences:



#---------------------------------------------------------------------------------------
# \A - Matches if the specified characters are at the start of a string.
#---------------------------------------------------------------------------------------
import re
print("'\\Athe' - Matches if the specified characters are at the start of a string.")

pattern = "\\Athe"

list_str = ['the sun', 'In the sun','theabc']

result = [x for x in list_str if re.search(pattern,x)]
print(result)



#---------------------------------------------------------------------------------------
# \b - Matches if the specified characters are at the beginning or end of a word.
#---------------------------------------------------------------------------------------

import re

print("\\bfoo - Matches if the specified characters are at the beginning of a word.")

pattern_at_the_beginning = "\\bfoo"

list_str = ['football', 'a football','afootball']
result = [x for x in list_str if re.search(pattern_at_the_beginning,x)]
print(result)
#---------------------------------------------------------------------------------------
print("foo\\b - Matches if the specified characters are at end of a word.")

pattern_at_the_end = "foo\\b"

list_str = ['the foo', 'the afoo test','the afootest']
result = [x for x in list_str if re.search(pattern_at_the_end,x)]
print(result)



#---------------------------------------------------------------------------------------
# \B - Opposite of \b. 
# Matches if the specified characters are not at the beginning or end of a word.
#---------------------------------------------------------------------------------------

import re

print("\\Bfoo - Matches if the specified characters are NOT at the beginning of a word.")

pattern_not_at_the_beginning = "\\Bfoo"

list_str = ['football', 'a football','afootball']
result = [x for x in list_str if re.search(pattern_not_at_the_beginning,x)]
print(result)
#---------------------------------------------------------------------------------------

print("foo\\B - Matches if the specified characters are NOT at end of a word.")

pattern_not_at_the_end = "foo\\B"

list_str = ['the foo', 'the afoo test','the afootest']
result = [x for x in list_str if re.search(pattern_not_at_the_end,x)]
print(result)



#---------------------------------------------------------------------------------------
# \d - Matches any decimal digit. Equivalent to [0-9]
#---------------------------------------------------------------------------------------

import re

print("\\d - Matches any decimal digit. Equivalent to [0-9]")

pattern = '\\d'

list_str = ['12abc3', '123', 'Python']

# 12abc3	: 3 matches (at 12abc3)
# Python	: No match

result = [x for x in list_str if re.search(pattern,x)]
print(result)

#---------------------------------------------------------------------------------------
# \D - Matches any non-decimal digit. Equivalent to [^0-9]
#---------------------------------------------------------------------------------------

import re

print("\\D - Matches any non-decimal digit. Equivalent to [^0-9]")

pattern = '\\D'

list_str = ['12abc3', '123', 'Python']

# 12abc3	: 3 matches (at 12abc3)
# 123	    : No match

result = [x for x in list_str if re.search(pattern,x)]
print(result)
