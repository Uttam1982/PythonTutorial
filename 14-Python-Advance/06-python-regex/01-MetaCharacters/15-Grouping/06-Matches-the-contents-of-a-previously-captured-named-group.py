#------------------------------------------------------------------------------------------
# (?P=<name>)
#------------------------------------------------------------------------------------------ 
# Matches the contents of a previously captured named group.

# The (?P=<name>) metacharacter sequence is a backreference, 
# similar to \<n>, except that it refers to a named group rather than a numbered group.

# Here again is the example from above, which uses a numbered backreference to match a word, 
# followed by a comma, followed by the same word again:

#------------------------------------------------------------------------------------------
import re

regex = r'(\w+),\1'
m= re.search(regex,'foo,foo')

# Output : <re.Match object; span=(0, 7), match='foo,foo'>
print(m)
# Output: 'foo'
print(m.group(1))

#------------------------------------------------------------------------------------------
# (?P=<name>)

# The following code does the same thing using a named group and a backreference instead:

regex = r'(?P<word>\w+),(?P=word)'
m= re.search(regex,'foo,foo')
# Output : <re.Match object; span=(0, 7), match='foo,foo'>
print(m)
# Output: 'foo'
print(m.group('word'))

# (?P=<word>\w+) matches 'foo' and saves it as a captured group named : word. 
# Again, the comma matches literally. Then (?P=word) is a backreference to the named 
# capture and matches 'foo' again.

#------------------------------------------------------------------------------------------
# Note: The angle brackets (< and >) are required around name when creating a named group 
# but not when referring to it later, either by backreference or by .group():

regex = r'(?P<num>\d+)\.(?P=num)'
m = re.search(regex,'123.123')

# Output : <re.Match object; span=(0, 7), match='123.123'>
print(m)
print(m.group('num')) #123

#------------------------------------------------------------------------------------------



