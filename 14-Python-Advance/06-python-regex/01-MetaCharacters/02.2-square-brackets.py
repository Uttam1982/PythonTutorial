# []
# Specifies a specific set of characters to match.
#------------------------------------------------------------------------------------------

# Characters contained in square brackets ([]) represent a character class
# —an enumerated set of characters to match from. A character class metacharacter 
# sequence will match any single character contained in the class.

#------------------------------------------------------------------------------------------
import re

match = re.search('ba[artz]','foobarqux')
# Output : <re.Match object; span=(3, 6), match='bar'>
print(match)

match = re.search('ba[artz]','foobazqux')
# Output : <re.Match object; span=(3, 6), match='baz'>
print(match)

# The metacharacter sequence [artz] matches any single 'a', 'r', 't', or 'z' character. 
# In the example, the regex ba[artz] matches both 'bar' and 'baz' (and would also match 
# 'baa' and 'bat').

#------------------------------------------------------------------------------------------

# A character class can also contain a range of characters separated by a hyphen (-), 
# in which case it matches any single character within the range. 
# For example, [a-z] matches any lowercase alphabetic character between 'a' and 'z', inclusive:

match = re.search('[a-z]','F00bar')
# Output : <re.Match object; span=(3, 4), match='b'>  
print(match)


# [0-9] matches any digit character:
match = re.search('[0-9][0-9]','Foo123bar')
# Output: <re.Match object; span=(3, 5), match='12'> 
print(match)


# [0-9a-fA-F] matches any hexadecimal digit character:
match = re.search('[0-9a-fA-F]','---a0---')
# Output : <re.Match object; span=(3, 4), match='a'>
print(match)

# [^0-9] matches any character that isn’t a digit:
match = re.search('[^0-9]','12345foo')
# Output : <re.Match object; span=(5, 6), match='f'>
print(match)

# If a ^ character appears in a character class but isn’t the first character, 
# then it has no special meaning and matches a literal '^' character:
match = re.search('[#:^]','foo^bar:baz#qux')
# Output : <re.Match object; span=(3, 4), match='^'>
print(match)

#------------------------------------------------------------------------------------------
# Note: In the above examples, the return value is always the leftmost possible match. 
# re.search() scans the search string from left to right, and as soon as it locates 
# a match for <regex>, it stops scanning and returns the match.


#------------------------------------------------------------------------------------------
# literal hyphen character '-'
#------------------------------------------------------------------------------------------

# As you’ve seen, you can specify a range of characters in a character class 
# by separating characters with a hyphen. 

# What if you want the character class to include a literal hyphen character? 
# You can place it as the first or last character or escape it with a backslash (\):

#------------------------------------------------------------------------------------------

# Output: <re.Match object; span=(3, 4), match='-'>
print(re.search('[-abc]','123-456'))

# Output: <re.Match object; span=(3, 4), match='-'>
print(re.search('[abc-]','123-456'))

# Output: <re.Match object; span=(3, 4), match='-'>
print(re.search('[ab\\-c]','123-456'))

#------------------------------------------------------------------------------------------
# include a literal ']' in a character class
#------------------------------------------------------------------------------------------

# then you can place it as the first character or escape it with backslash:

# Output: <re.Match object; span=(4, 5), match=']'>
print(re.search('[]]','foo[]'))
# Output: <re.Match object; span=(4, 5), match=']'>
print(re.search('[ab\\]cd]','foo[]'))

#------------------------------------------------------------------------------------------
# Other regex metacharacters lose their special meaning inside a character class
#------------------------------------------------------------------------------------------
# Output: <re.Match object; span=(3, 4), match='*'>
print(re.search('[)*+|]','123*456'))

# Output: <re.Match object; span=(3, 4), match='*'>
print(re.search('[)*+|]','123+456'))

#------------------------------------------------------------------------------------------
