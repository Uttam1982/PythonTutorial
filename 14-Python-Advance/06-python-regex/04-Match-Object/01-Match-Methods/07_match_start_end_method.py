# match.start([<grp>])

# match.end([<grp>])
#--------------------------------------------------------------------------------------------

# Return the starting and ending indices of the match.

# match.start() returns the index in the search string where the match begins, 
# and match.end() returns the index immediately after where the match ends:

#--------------------------------------------------------------------------------------------
import re

s = 'foo123bar456baz'

regex = r'\d+'

m = re.search(regex,s)
# Output : <re.Match object; span=(3, 6), match='123'>
print(m)

# Output : 3
print(m.start())

# Output : 6
print(m.end())

# Output : 123
print(s[m.start() : m.end()])


s = 'foo123bar456baz'
m = re.search(r'(\d+)\D*(?P<num>\d+)', s)

# Output : ('123', '456')
print(m.groups())

# Output : 123
print(m.group(1))

print(m.start(1))
print(m.end(1))

# Output : 456
print(m.group('num'))

print(m.start('num'))
print(m.end('num'))

# A special case occurs when the regex contains a group that doesn’t participate in the match:

m = re.search(r'(\w+),(\w+),(\w+)?', 'foo,bar,')

# Output : ('foo', 'bar', None)
print(m.groups())

# Output : None
print(m.group(3))

# Output : -1 -1
print(m.start(3), m.end(3))

# As you’ve seen previously, in this case the third group doesn’t participate. 
# m.start(3) and m.end(3) aren’t really meaningful here, so they return -1.

