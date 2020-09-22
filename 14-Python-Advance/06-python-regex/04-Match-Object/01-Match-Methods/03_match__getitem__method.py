# match.__getitem__(<grp>)
#--------------------------------------------------------------------------------------------
# Returns a captured group from a match.

# match.__getitem__(<grp>) is identical to match.group(<grp>) and 
# returns the single group specified by <grp>:

#--------------------------------------------------------------------------------------------
import re

m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')

# Output : bar
print(m.group(2))


# Output : bar
print(m.__getitem__(2))

# Output : bar
print(m[2])

# As of Python version 3.6, the re module does implement .__getitem__() for match objects. 
# The implementation is such that match.__getitem__(n) is the same as match.group(n).

m = re.match(
            r'foo,(?P<w1>\w+),(?P<w2>\w+),qux',
            'foo,bar,baz,qux')
# Output : baz
print(m.group('w2'))

# Output : baz
print(m.__getitem__('w2'))

# Output : baz
print(m['w2'])

#--------------------------------------------------------------------------------------------