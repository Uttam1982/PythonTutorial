# match.groups(default=None)
#--------------------------------------------------------------------------------------------
# Returns all captured groups from a match.

# match.groups() returns a tuple of all captured groups:
#--------------------------------------------------------------------------------------------

import re

regex = r'(\w+),(\w+),(\w+)'
s = 'foo,bar,baz'

m = re.search(regex,s)
# Output : <re.Match object; span=(0, 11), match='foo,bar,baz'>
print(m)

# Output : ('foo', 'bar', 'baz')
print(m.groups())


m = re.search(r'(\w+),(\w+),(\w+)?', 'foo,bar,')
# Output : <re.Match object; span=(0, 8), match='foo,bar,'>
print(m)

# Output : ('foo', 'bar', None)
print(m.groups())

print(m.groups(default='----'))

#--------------------------------------------------------------------------------------------
# Here, the third (\w+) group doesn’t participate in the match because the 
# question mark (?) metacharacter makes it optional, and the string 'foo,bar,' 
# doesn’t contain a third sequence of word characters. By default, m.groups() 
# returns None for the third group, as shown , you can see 
# that specifying default='---' causes it to return the string '---' instead.

