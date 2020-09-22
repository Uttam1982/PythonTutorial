#--------------------------------------------------------------------------------------------
# Match Object Methods
#--------------------------------------------------------------------------------------------

# The table below summarizes the methods that are available for a match object match:

#--------------------------------------------------------------------------------------------
# Method	                Returns
#--------------------------------------------------------------------------------------------

# match.group()	          The specified captured group or groups from match
# match.__getitem__()	    A captured group from match
# match.groups()	        All the captured groups from match
# match.groupdict()	      A dictionary of named captured groups from match
# match.expand()	        The result of performing backreference substitutions from match
# match.start()	          The starting index of match
# match.end()	            The ending index of match
# match.span()	          Both the starting and ending indices of match as a tuple

#--------------------------------------------------------------------------------------------

# match.group([<group1>, ...])

# Returns the specified captured group(s) from a match.

import re

m = re.search(r'(\w+),(\w+),(\w+)','foo,bar,baz')

# Output : <re.Match object; span=(0, 11), match='foo,bar,baz'>
print(m)

# Output : (foo,bar,baz)
print(m.groups())

# If you call .group() with an argument of 0 or no argument at all, 
# then it returns the entire match:

# Output : foo,bar,baz
print(m.group())

# Output : foo,bar,baz
print(m.group(0))


# Output : foo
print(m.group(1))

# Output : baz
print(m.group(3))

# returns a tuple : ('foo', 'baz')
print(m.group(1, 3)) 

# Output : ('baz', 'baz', 'foo', 'foo', 'bar', 'bar')
print(m.group(3, 3, 1, 1, 2, 2))


# If you specify a group that’s out of range or nonexistent, then .group() 
# raises an IndexError exception:

# Output : IndexError: no such group
# print(m.group(4)) 

# It’s possible for a regex in Python to match as a whole but to contain a group 
# that doesn’t participate in the match. In that case, .group() returns None 
# for the nonparticipating group. Consider this example:

m1 = re.search(r'(\w+),(\w+),(\w+)?','foo,bar,')

# Output : foo
print(m1.group(1))

# Output : bar
print(m1.group(2))

# Output : None
print(m1.group(3))


m = re.match(r'(\w{3},)+', 'foo,bar,baz,qux')

# Output : <re.Match object; span=(0, 12), match='foo,bar,baz,'>
print(m)

# Output : foo,bar,baz,
print(m.group())

# Output : baz,
print(m.group(1))


# In this example, the full match is 'foo,bar,baz,', as shown by the 
# displayed match object. Each of 'foo,', 'bar,', and 'baz,' matches 
# what’s inside the group, but m.group(1) returns only the last match, 'baz,'.


# Remember: Numbered captured groups are one-based, not zero-based.
#--------------------------------------------------------------------------------------------

# If you capture groups using (?P<name><regex>), 
# then match.group(<name>) returns the corresponding named group:

regex = r'(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)'

s = 'sam,joe,rita'

m = re.search(regex,s)

# Output : ('sam', 'joe', 'rita')
print(m.groups())

# Output : sam,joe,rita
print(m.group())

# Output : sam
print(m.group('w1'))

# Output : rita
print(m.group('w3'))

# Output : ('sam', 'rita')
print(m.group('w1', 'w3'))

# Output: ('rita', 'sam', 'sam', 'joe')
print(m.group('w3', 'w1', 'w1', 'w2'))

# Output : IndexError: no such group
print(m.group('w4')) 

#--------------------------------------------------------------------------------------------